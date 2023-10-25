def add (fn , sn):
    print ('addition=',fn + sn)

def sub (fn ,sn):
    print ('substractin=',fn - sn)

def mul (fn ,sn):
    print ('multipication=',fn * sn)

def div (fn , sn):
    print ('division=',fn / fn )

while True:

    ch = int(input('\nEenter choice:\n1.add\t2.sub\n3.mul\t4.div\n5.exit'))

    if ch == 1:
       print('\naddition')
       fn = int (input('enter first number:'))
       sn = int (input('enter second number:'))

    elif ch == 2:
       print('\substraction')
       fn = int (input('enter first number:'))
       sn = int (input('enter second number:'))

    elif ch == 3:
       print('\nmultipication')
       fn = int (input('enter first number:'))
       sn = int (input('enter second number:'))

    elif ch == 4:
       print('\division')
       fn = int (input('enter first number:'))
       sn = int (input('enter second number:'))

    elif ch == 5:
         print ('\nexisting')
         break

    else :
         print ('\ninvalid')

                  

