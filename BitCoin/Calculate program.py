b = input('Give Bitcoin Buying price: ')
s = input('Give Current Bitcoin Price:  ')
l = input('Give the BitCoin Amount that you purchased:  ')
l1 = input('Give the Amount you wish to earn:  ')
fee = input('Give Transaction Fee if known:  ')

b=float(b)
fee=float(fee)
s=float(s)
l=float(l)
l1=float(l1)

i = l*b      #Change the Bitcoin ammount after purchuse

#----------Formulas----------

currency= "Bitcoin"
#-------calculate Take Profit Price------------------
# k = target price to have 100$ profit (change the 100 accordingly)

k = i+l1+fee
target_perc =((k-i)/i)+1
target_price = (target_perc*b)


#------------Calculate Stop Loss Price based on profit target-------------------

loss_perc = ((target_perc-1)/2)-1
loss_price = loss_perc*b

#----------------------------------------


per = ((s-b)/b)*100
prof= (per*i)/100
net_profit = prof-fee

print('\nThe percentage of movement equals with: %1.2f' %per,'%')
print('\nThe percentage of movement of the {} curency is {:1.2f}%'.format(currency, per))


print('\n% movement :',round(per,2),end = ' \n ')
print('\n-------------------------------------')
print('\nProfit/Loss:')
print(round(prof,2))
print('\n--------------------------------------')
print('Net profit/loss:')
print(round(net_profit,2))
print('--------------------------------------')
print('Invested Ammount:')
print(round(i,0))
print('--------------------------------------')
print('Target price to get {}'.format(l1))
print(round(target_price,1))
print('--------------------------------------')
print('Target % to get {}'.format(l1))
print(round(((target_perc)-1)*100,2))

print('--------------------------------------')
print('Stop loss %')
print(round(((loss_perc)+1)*100,2))
print('--------------------------------------')
print('Stop loss price')
print(round(loss_price,1))
print("\n------------------------------\nStop Loss price is: {x}$ \n\nStop Loss Perc is: {y}% \n\n --------------------------------- \n\n".format(x=round(loss_price,1), y=round(((loss_perc)+1)*100,2)))