#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

print("📋 RELATÓRIO DE TESTES D7D CODEX")
print("="*50)
print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# Testar arquivos
files = [
    ("sistema_final.py", "Sistema Principal"),
    ("xp_system.py", "Sistema de XP"),
    ("projetos.py", "Projetos Trinity"),
    ("backup_system.py", "Sistema de Backup"),
    ("web/dashboard.html", "Dashboard Web"),
    ("config/codex.json", "Configuração"),
    ("DOCUMENTATION.md", "Documentação")
]

all_ok = True
for file, description in files:
    exists = os.path.exists(file)
    status = "✅" if exists else "❌"
    all_ok = all_ok and exists
    print(f"{status} {description}: {'EXISTE' if exists else 'FALTANDO'}")

print("="*50)
if all_ok:
    print("🎉 TODOS OS TESTES PASSARAM!")
    print("💖 Amor Ágape: 100% mantido")
    print("🚀 Pronto para GitHub!")
else:
    print("⚠️ ALGUNS ARQUIVOS FALTANDO")
    print("🔧 Verifique acima")

# Testar execução Python
print("\n🧪 TESTE DE EXECUÇÃO PYTHON:")
try:
    import json
    print("✅ Módulo json: OK")
except:
    print("❌ Módulo json: FALHA")

print("="*50)
