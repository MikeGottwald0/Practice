print('''This is an income tax calculator.\n
Without tax cuts or breaks, this is the amount the IRS expects from\n
YOU in taxes this year.\n''')

while True:
  print('Please enter your ANNUAL income last year.')
  i = input()
  try:
    i = int(i)
  except:
    print('Please enter a number.')
    continue
  if i <1:
    print('Please enter a positive number')
    continue
  break
  
if i >= 1 and i <=9325 :
    tax = 0.1 * i
    print(tax)
else if i >= 9326 and i <= 37949:
    if i == 9326:
        print(933)
        break
     else:
        temp = i - 9326
        tax = (temp * 0.15) + 933
        print(tax)
else if i >= 37950 and i <= 91899:
    if i == 37950:
        print(5227)
        break
     else:
        temp = i - 37950
        tax = (temp * 0.25) + 5227
        print(tax)
 else if i >= 91900 and i <= 191649:
    if i == 91900:
        print(18714)
        break
     else:
        temp = i - 91900
        tax = (temp * 0.28) + 18714
        print(tax)
else if i >= 191650 and i <= 416699:
    if i == 191650:
        print(46644)
        break
     else:
        temp = i - 191650
        tax = (temp * 0.33) + 46644
        print(tax)
else if i >= 416700 and i <= 418399:
    if i == 416700:
        print(120911)
        break
     else:
        temp = i - 416700
        tax = (temp * 0.35) + 120911
        print(tax)
else if i >= 418400:
        tax = (temp * 0.40) + 121506
        print(tax)
