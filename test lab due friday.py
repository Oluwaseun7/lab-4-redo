#AkinnusotuLab_4                           


                            ##2.2

def evaluatesimpleexpression(string):
    
    expr1 = ("12+27")#hardcode an expression
    plus_sign = expr1.find("+") #find the plus sign and lock it to a variable
 
    num_1 = int(expr1 [ :plus_sign])#whatever is before the plus sign, becomes this varible
    num_2 = int(expr1 [plus_sign: ])#whatever is after the plus sign, becomes this varible

    val = num_1 + num_2 #variable for the sum of the two numbers
    return val

string=("12+27")#what the string is

print(evaluatesimpleexpression(string))


##                        #2.3
##
##while (True):
##         #ask the user to input an expression of an specific form
##         expr =input("Please enter an expression with the form ""'number+number' or \"end\" to quit :")
##         #if the expression is equal to end, the program ends
##         if expr == 'end':
##                 print("Done")
##                 break
##         else:
## 
##                 #make the program so that the user can input the expression between parenthesis 
##                 if expr [0] == "(" and expr [len(expr)-1] == ")":
##                         expr = (expr[1:len(expr)-1])
##                 
##                                 # s must contain an operator
##                 plus_sign = expr.find("+")
##                 minus_sign = expr.find("-")
##                 mult_sign = expr.find("*")
##                 div_sign = expr.find("/")
##                 all_signs = max(plus_sign,minus_sign,mult_sign,div_sign)
##                 if all_signs == -1:
##                         print('Invalid Expression')
##                         #made sure we have an operator)
##                         
##                 else:   
##                        #check if we have numbers on either sides of operator
##                         num1Str = expr[:all_signs]
##                         num2Str = expr[all_signs+1:]
##                         
##                         #if we do not have numbers in the expression, the expression has to be invalid
##                 if num1Str.isnumeric() and num2Str.isnumeric():
##                         
##                         num1 = int(expr [ :all_signs])#first number of the expression
##                         num2 = int(expr [all_signs+1: ])#second number of the expression
## 
##                         #here basically I assign the command depending on the sign of the expression
##                         if all_signs == plus_sign:
##                                 result = num1 + num2
##                         elif all_signs == minus_sign:
##                                 result = num1 - num2
##                         elif all_signs == mult_sign:
##                                 result = num1 * num2
##                         else:
##                                 all_signs == div_sign
##                                 result = num1 / num2
## 
##                         if all_signs == plus_sign:
##                                 print(num1Str, '+', num2Str, '=',result)
##                         elif all_signs == minus_sign:
##                                 print(num1Str, '-', num2Str, '=',result)
##                         elif all_signs == mult_sign:
##                                 print(num1Str, '*', num2Str, '=',result)
##                         else:
##                                 all_signs == div_sign
##                                 print(num1Str, '/', num2Str, '=',result)
##                 else:
##                         print('Invalid Expression')

