import pytest
from pytest import mark
from codigo.bytebank import Funcionario
class TestClass:

    # no pytest é obrigatório definir um método começando com teste
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):

        entrada = '13/03/2000' # Given-Contexto
        esperado = 22

        funcionario_test = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_test.idade() # when-acao

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_apenas_carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    def test_quando_descrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 #given
        esperado = 100.0

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus() #when

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000000  # given

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado #then


