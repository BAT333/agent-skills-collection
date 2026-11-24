#!/usr/bin/env python3
"""Validador auxiliar, sem dependências, para erros comuns em Agent Skills.

Não substitui o validador oficial `skills-ref validate` nem implementa todo o YAML.
Uso: python scripts/validate_skill.py CAMINHO/DA/SKILL [--strict]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_RE = re.compile(r"(?<![A-Za-z0-9_.-])(?:references|assets|scripts)/[A-Za-z0-9_./-]+")


def read_frontmatter(skill_file: Path) -> tuple[str | None, str | None, list[str]]:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, None, ["SKILL.md deve começar com delimitador YAML '---'."]

    end = text.find("\n---\n", 4)
    if end < 0:
        return None, None, ["Frontmatter YAML não possui delimitador de fechamento '---'."]

    block = text[4:end]
    values: dict[str, str] = {}
    errors: list[str] = []
    for key in ("name", "description"):
        match = re.search(rf"^{key}:\s*(.*?)\s*$", block, flags=re.MULTILINE)
        if not match:
            errors.append(f"Campo obrigatório ausente ou não escalar: {key}.")
            continue
        value = match.group(1).strip()
        if value.startswith(("|", ">")):
            errors.append(f"Campo {key} usa YAML multilinha; valide com `skills-ref` ou um parser YAML.")
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value

    return values.get("name"), values.get("description"), errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verifica erros comuns na estrutura de uma Agent Skill.")
    parser.add_argument("skill_dir", type=Path, help="Diretório que contém SKILL.md")
    parser.add_argument("--strict", action="store_true", help="Trata avisos de tamanho como falhas.")
    args = parser.parse_args()

    root = args.skill_dir.expanduser().resolve()
    skill_file = root / "SKILL.md"
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"ERRO: diretório não encontrado: {root}")
        return 2
    if not skill_file.is_file():
        print(f"ERRO: arquivo obrigatório não encontrado: {skill_file}")
        return 2

    name, description, fm_errors = read_frontmatter(skill_file)
    errors.extend(fm_errors)

    if name is not None:
        if not (1 <= len(name) <= 64) or not NAME_RE.fullmatch(name):
            errors.append("name deve usar 1-64 caracteres ASCII minúsculos, números e hífens simples.")
        if name != root.name:
            errors.append(f"name ({name!r}) deve corresponder ao nome do diretório ({root.name!r}).")

    if description is not None:
        if not (1 <= len(description) <= 1024):
            errors.append("description deve ter entre 1 e 1024 caracteres.")

    content = skill_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    body = content.split("\n---\n", 1)[-1]
    approx_tokens = len(re.findall(r"\S+", body))
    if len(lines) > 500:
        warnings.append(f"SKILL.md tem {len(lines)} linhas; a especificação recomenda menos de 500.")
    if approx_tokens > 5000:
        warnings.append(f"Corpo do SKILL.md tem aproximadamente {approx_tokens} palavras/tokens separados por espaço; considere mover detalhes para references/.")

    for match in RESOURCE_RE.finditer(content):
        relative = match.group(0).rstrip(".,;:)")
        if relative.count("/") > 1:
            warnings.append(f"Referência aninhada; prefira um nível a partir da raiz: {relative}")
        target = (root / relative).resolve()
        if root not in target.parents and target != root:
            errors.append(f"Caminho sai do diretório da Skill: {relative}")
        elif not target.exists():
            errors.append(f"Recurso referenciado não existe: {relative}")

    for resource_dir in ("references", "assets", "scripts"):
        candidate = root / resource_dir
        if candidate.exists() and not candidate.is_dir():
            errors.append(f"{resource_dir} existe, mas não é diretório.")

    for message in warnings:
        print(f"AVISO: {message}")
    for message in errors:
        print(f"ERRO: {message}")

    if errors or (args.strict and warnings):
        print(f"\nFALHOU: {len(errors)} erro(s), {len(warnings)} aviso(s).")
        return 1

    print(f"OK: {root.name} — verificações auxiliares concluídas ({len(warnings)} aviso(s)).")
    print("Observação: este script não substitui `skills-ref validate` nem testes funcionais no cliente-alvo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
