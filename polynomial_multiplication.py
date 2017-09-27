polynomial_vector = [] #vector of coefficients in a0 + a1x + a2x^2....anx^n
horner_vector = []
def calculateHornerCoefficient(coefficient_pos,x_value):
   if coefficient_pos == len(polynomial_vector)-1:
      horner_vector.append(polynomial_vector[coefficient_pos])
      return polynomial_vector[coefficient_pos]
   temp = polynomial_vector[coefficient_pos] + calculateHornerCoefficient(coefficient_pos+1,x_value)*x_value
   horner_vector.append(temp)
   return temp

def horner():
   global polynomial_vector,horner_vector
   polynomial_vector = [float(x) for x in raw_input("Enter Coefficients: ").split()]
   x_value = float(raw_input("Enter Value of X: "))
   print calculateHornerCoefficient(0,x_value)
   print horner_vector[::-1]

if __name__ == '__main__':
   horner()
