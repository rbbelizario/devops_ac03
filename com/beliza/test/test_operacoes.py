class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x


 def test_two(self):
        x = "hello"
        assert hasattr(x, "check")









def quociente_resto(x, y):
    quociente = x // y
    resto = x % y
    return (quociente, resto)

print("Quociente e resto: ", quociente_resto(9, 4))
