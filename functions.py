import os


def cls():
    """
    Limpa a tela.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_dados_hospede(hospede):
    """
    Print dados do hospede.
    """
    print(f"""id: {hospede['id']}\tnome: {hospede['nome']}\tcpf: {hospede['cpf']}\tTipo do quarto: {hospede['qtdePessoas']}\tTipo quarto: {hospede['tipoQuarto']}
    \tQtde. dias: {hospede['numDias']}\tValor: {hospede['valor']}\tStatus: {hospede['status']}""")


def verifica_valor_do_quarto(tipoQuarto, qtdePessoas, dias):
    """
    Calculando valores
    """
    if(tipoQuarto.upper() == 'S'):
        return dias * (qtdePessoas * 100) 
    if(tipoQuarto.upper() == 'D'):
        return dias * (qtdePessoas * 200) 
    if(tipoQuarto.upper() == 'P'):
        return dias * (qtdePessoas * 300)


def procurar_reserva_pelo_cpf(lista_hospedes, cpf):
    reservas_pelo_hospede = []

    for hospede in lista_hospedes:
        if hospede['cpf'] == cpf:
            reservas_pelo_hospede.append(hospede)

    return reservas_pelo_hospede

def listar_reservas_por_status(lista_hospedes, status):
    reservas = list(filter(lambda x: x['status'] == status, lista_hospedes))
    return reservas
