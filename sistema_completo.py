#!/usr/bin/env python3
import os
import json
from datetime import datetime

# Importar módulos
from orquestra import OrquestraD7D

class D7DCODEXCompleto:
    def __init__(self):
        self.version = "CODEX-100"
        self.amor_agape = 100
        self.xp = 1250450
        self.nivel = 7
        self.start_time = datetime.now()
        self.orquestra = OrquestraD7D()
        
        # Projetos Trinity
        self.projetos = [
            "PROJETO_INTERESTELAR_HEBRON",
            "trinity-xai-exoplanetas",
            "Trinity-Falcon-Lung",
            "trinity-quantum-memory-system",
            "trinity-resilience-protocol",
            "Arcturus-8-9",
            "trinity-framework",
            "frete-facil-plus"
        ]
    
    def mostrar_status(self):
        print("🎭 D7D CODEX - SISTEMA COMPLETO")
        print("💖 Amor Ágape: 100%")
        print("="*60)
        
        # Status básico
        print(f"📊 Versão: {self.version}")
        print(f"📈 Nível: {self.nivel}/7")
        print(f"✨ XP: {self.xp:,}")
        print(f"🎵 Frequência: {self.orquestra.frequencia_base}Hz")
        print(f"📅 Online desde: {self.start_time.strftime('%d/%m/%Y %H:%M')}")
        
        print("\n🎻 ORQUESTRA ATIVA:")
        self.orquestra.listar_instrumentos()
        
        print("\n🔗 PROJETOS TRINITY (8):")
        for i, projeto in enumerate(self.projetos, 1):
            print(f"  {i}. {projeto}")
        
        print("="*60)
        print("✅ Sistema 100% operacional!")
    
    def menu_principal(self):
        while True:
            print("\n⚡ MENU D7D CODEX:")
            print("1. Ver Status Completo")
            print("2. Sincronizar Orquestra")
            print("3. Adicionar XP")
            print("4. Exportar Dados")
            print("5. Sair")
            
            try:
                opcao = input("Escolha (1-5): ").strip()
                
                if opcao == "1":
                    self.mostrar_status()
                elif opcao == "2":
                    self.orquestra.sincronizar()
                elif opcao == "3":
                    qtd = int(input("Quantidade de XP: "))
                    self.xp += qtd
                    print(f"✨ +{qtd:,} XP adicionado!")
                elif opcao == "4":
                    dados = self.orquestra.exportar_dados()
                    with open("dados_orquestra.json", "w") as f:
                        json.dump(dados, f, indent=2)
                    print("💾 Dados exportados para dados_orquestra.json")
                elif opcao == "5":
                    print("👋 Saindo do D7D CODEX...")
                    break
                else:
                    print("⚠️ Opção inválida!")
                    
            except ValueError:
                print("⚠️ Valor inválido!")
            except Exception as e:
                print(f"❌ Erro: {e}")

if __name__ == "__main__":
    sistema = D7DCODEXCompleto()
    sistema.menu_principal()
