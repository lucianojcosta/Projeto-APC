import tkinter as tk
from tkinter import ttk

class BitcoinMiningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estação de Mineração de Bitcoin Sustentável")
        self.root.geometry("800x600")

        # Notebook (abas) para organizar as seções
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Abas principais
        self.setup_initial_config_tab()
        self.setup_mining_station_tab()
        self.setup_solar_energy_tab()
        self.setup_cost_comparison_tab()
        self.setup_feasibility_tab()
        self.setup_about_tab()

    def setup_initial_config_tab(self):
        """Configuração Inicial: Região e Orçamento"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Configuração Inicial")

        # Estado/Região
        ttk.Label(frame, text="Selecione o Estado:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.state_combo = ttk.Combobox(frame, values=["SP", "RJ", "MG", "RS", "Outro"])
        self.state_combo.grid(row=0, column=1, padx=10, pady=10)

        # Orçamento
        ttk.Label(frame, text="Orçamento (R$):").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.budget_entry = ttk.Entry(frame)
        self.budget_entry.grid(row=1, column=1, padx=10, pady=10)

    def setup_mining_station_tab(self):
        """Montagem da Estação de Mineração"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Montar Estação")

        # Componentes (Exemplo: GPU, ASIC, Fonte)
        components = ["GPU", "ASIC", "Fonte", "CPU"]
        self.component_vars = {}

        for i, component in enumerate(components):
            ttk.Label(frame, text=f"{component}:").grid(row=i, column=0, padx=10, pady=5, sticky='w')
            var = tk.StringVar()
            self.component_vars[component] = var
            ttk.Combobox(frame, textvariable=var, values=["Modelo A", "Modelo B", "Modelo C"]).grid(row=i, column=1, padx=10, pady=5)

        # Consumo Automático (Placeholder)
        ttk.Button(frame, text="Calcular Consumo", command=self.calculate_consumption).grid(row=len(components), column=0, pady=10)
        self.consumption_label = ttk.Label(frame, text="Consumo: -- kWh/mês")
        self.consumption_label.grid(row=len(components), column=1, pady=10)

    def setup_solar_energy_tab(self):
        """Configuração de Energia Solar"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Energia Solar")

        # Quantidade de Painéis
        ttk.Label(frame, text="Número de Painéis:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.panels_entry = ttk.Entry(frame)
        self.panels_entry.grid(row=0, column=1, padx=10, pady=10)

        # Potência por Painel (kWp)
        ttk.Label(frame, text="Potência por Painel (kWp):").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.power_entry = ttk.Entry(frame)
        self.power_entry.grid(row=1, column=1, padx=10, pady=10)

    def setup_cost_comparison_tab(self):
        """Comparação de Custos"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Comparar Custos")

        # Custo Local de Energia (R$/kWh)
        ttk.Label(frame, text="Custo Local de Energia (R$/kWh):").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.energy_cost_entry = ttk.Entry(frame)
        self.energy_cost_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para Simular
        ttk.Button(frame, text="Simular Custos", command=self.simulate_costs).grid(row=1, column=0, pady=10)
        self.cost_result_label = ttk.Label(frame, text="Resultado: --")
        self.cost_result_label.grid(row=1, column=1, pady=10)

    def setup_feasibility_tab(self):
        """Análise de Viabilidade"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Viabilidade")

        # Placeholder para Resultados
        self.feasibility_label = ttk.Label(frame, text="Status: Não Calculado", background="yellow")
        self.feasibility_label.pack(pady=20)

        # Botão para Verificar Viabilidade
        ttk.Button(frame, text="Verificar Viabilidade", command=self.check_feasibility).pack(pady=10)

    def setup_about_tab(self):
        """Sobre o Projeto"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Sobre")

        info_text = """
        Projeto: Estação de Mineração de Bitcoin Sustentável
        Integrantes: Antenor, Eduardo, Hilber, Luciano
        Tutor: Danilo

        Este projeto simula uma estação de mineração de Bitcoin
        utilizando energia solar, com foco em dados do Brasil.
        """
        ttk.Label(frame, text=info_text, justify=tk.LEFT).pack(padx=10, pady=10)

    # Placeholder para funções de cálculo
    def calculate_consumption(self):
        """Placeholder para cálculo de consumo"""
        self.consumption_label.config(text="Consumo: 1500 kWh/mês")  # Exemplo

    def simulate_costs(self):
        """Placeholder para simulação de custos"""
        self.cost_result_label.config(text="Economia: R$ 500/mês")  # Exemplo

    def check_feasibility(self):
        """Placeholder para verificação de viabilidade"""
        self.feasibility_label.config(text="Viável", background="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitcoinMiningApp(root)
    root.mainloop()