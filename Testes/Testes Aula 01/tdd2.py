def atacar(forca, arma):
    return forca + arma

# ataque simple
def test_atacar_normal():
    try:
        assert atacar(10,5) == 15
        print("✅ O teste passou!")
    except AssertionError:
        print("❌ O teste atacar normal falhou!")

test_atacar_normal()