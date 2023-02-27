

def checkBrackets(brack):
    leftb1=brack.count('{')
    rightb1=brack.count('}')
    leftb2=brack.count('[')
    rightb2=brack.count(']')
    leftb3=brack.count('(')
    rightb3=brack.count(')')
   

    if leftb1==rightb1:
       if leftb2==rightb2:
            if leftb3==rightb3:
                
                print('valid')


    if leftb1 != rightb1:
        print('invalid')
    if leftb2 != rightb2:
        print('invalid')
    if leftb3 != rightb2:
        print('invalid')


checkBrackets('{}[]({()()})')   
