from bmi.imc import Imc


def test_calculo_imc_deve_retornar_dict():
    imc = Imc(101, 175)
    assert isinstance(imc.calculate_bmi(), dict)
    assert isinstance(imc.calculate_bmi(), dict)
