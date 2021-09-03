class Soma:


    def calcula(array):
        result = 0
        for numero in array:
            result = result + numero
        return result

array = [5,4,3]
resultado = Soma.calcula(array)
print(resultado)