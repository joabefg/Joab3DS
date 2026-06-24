def sacar(saldo, valor):
    '''
    sacar(saldo, valor): Saca dinheiro da conta
        saldo: Valor atual na conta
        valor: Valor a ser sacado
        return: Retorna o Saldo após a retirada
    '''
    if valor <= 0:
        raise ValueError("Valor inválido")
    
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    
    return saldo - valor