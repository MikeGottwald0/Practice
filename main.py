def tax_bracket(i):
  switcher = {
          (0 - 9325): 'ten',
          (9326 - 37950): 'fifteen',
          (37951 - 91900): 'twenty_five',
          (91901 - 191650): 'twenty_eight',
          (191651 - 416700): 'thirty_three',
          (416701 - 418400): 'thirty_five',
          (i > 418401): 'forty'
  }
  return switcher.get(i,"Invalid value for anual income!")

def ten():
  tax = 0.1*i
  print(tax)
def fifteen():
  if i == 9326:
    print(933)
  else:
    temp = i - 9325
    tax = (0.15 * temp) + 933
    print(tax)
def twenty_five():
  if i == 37950:
    print(5227)
  else:
    temp = i - 5227
    tax = (0.25 * temp) + 5227
    print(tax)
def twenty_eight():
  if i == 91900:
    print(18714)
  else:
    temp = i - 18714
    tax = (0.28 * temp) + 18714
    print(tax)
def thirty_three():
  if i == 191650:
    print(46644)
  else:
    temp = i - 46644
    tax = (0.33 * temp) + 46644
    print(tax)
def thirty_five():
  if i == 416700:
    print(120911)
  else:
    temp = i - 120911
    tax = (0.35 * temp) + 120911
    print(tax)
def forty():
  if i == 418400:
    print(121506)
  else:
    temp = i - 121506
    tax = (0.40 * temp) + 121506
    print(tax)


print('''This is an income tax calculator.\n
Without tax cuts or breaks, this is the amount the IRS expects from\n
YOU in taxes this year.\n''')

while True:
  print('Please enter your ANNUAL income last year.')
  i = input()
  tax_bracket(i)
  try:
    i = int(i)
  except:
    print('Please enter a number.')
    continue
  if i < 1:
    print('Please enter a positive number')
    continue
  break

  

