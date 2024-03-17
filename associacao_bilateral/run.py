from modulos import Casa, Pessoa

# casa da ana é uma instância de Casa()
casa_da_ana = Casa()
casa_de_jacquard = Casa()

ana = Pessoa("Ana")

ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(ana)

proprietario_ana = casa_da_ana.get_proprietario()

proprietario_ana.se_apresentar()
ana.apresentar_local()
