#!/bin/bash

echo "🎭 D7D CODEX - DEPLOY SCRIPT"
echo "════════════════════════════════════════"

# Verificar se estamos no diretório certo
if [ ! -f "sistema_final.py" ]; then
    echo "❌ Diretório errado. Execute de dentro de D7D_CODEX_FINAL"
    exit 1
fi

echo "📁 Diretório: $(pwd)"
echo "🐍 Python: $(python3 --version)"
echo "💖 Amor Ágape: 100%"

echo ""
echo "🚀 OPÇÕES:"
echo "1. Iniciar Sistema CLI"
echo "2. Iniciar Interface Web"
echo "3. Testar Todos os Módulos"
echo "4. Backup do Sistema"
echo "5. Configurar GitHub"
echo "6. Sair"

read -p "🎯 Escolha (1-6): " choice

case $choice in
    1)
        echo "🎭 Iniciando D7D CODEX CLI..."
        python3 sistema_completo.py
        ;;
    2)
        echo "🌐 Iniciando Interface Web..."
        echo "📱 Acesse: http://localhost:8080"
        echo "🛑 Pressione Ctrl+C para parar"
        python3 -m http.server 8080
        ;;
    3)
        echo "🧪 Testando todos os módulos..."
        python3 sistema_final.py
        echo "---"
        python3 xp_system.py
        echo "---"
        python3 projetos.py
        echo "---"
        python3 orquestra.py
        echo "✅ Todos os testes completos!"
        ;;
    4)
        echo "💾 Criando backup..."
        python3 backup_system.py
        echo "✅ Backup criado!"
        ;;
    5)
        echo "🔗 Configurando GitHub..."
        echo "1. Crie repositório no GitHub: D7D-CODEX"
        echo "2. Use os comandos:"
        echo "   git remote add origin git@github.com:deegpnini/D7D-CODEX.git"
        echo "   git push -u origin main"
        ;;
    6)
        echo "👋 Saindo..."
        exit 0
        ;;
    *)
        echo "❌ Opção inválida!"
        exit 1
        ;;
esac
