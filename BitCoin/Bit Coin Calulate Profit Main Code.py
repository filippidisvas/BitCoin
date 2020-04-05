# b = Buying Price (BitCoin Price)
# s = Current Price 
# i = Investment Amount (change 0.35)

#Change test second

currency = 'Bitcoin'

#-----------Change-----------
b = 6694        #Buying price
s = 6900   # Change to reflec the current price to see your profits
i = 0.35*b      #Change the Bitcoin ammount after purchuse
fee = 5.8       #change after making the trade
#----------Formulas----------


#-------calculate Take Profit Price------------------
# k = target price to have 100$ profit (change the 100 accordingly)

k = i+100+fee
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
print('The percentage of movement of {x} equals with {y}'.format(x=currency,y=per))

print('% movement :',round(per,2),end = ' \n ')
print('-------------------------------------')
print('Profit/Loss:')
print(round(prof,2))
print('--------------------------------------')
print('Net profit/loss:')
print(round(net_profit,2))
print('--------------------------------------')
print('Invested Ammount:')
print(round(i,0))
print('--------------------------------------')
print('Target price to get 100 ')
print(round(target_price,1))
print('--------------------------------------')
print('Target % to get 100')
print(round(((target_perc)-1)*100,2))

print('--------------------------------------')
print('Stop loss %')
print(round(((loss_perc)+1)*100,2))
print('--------------------------------------')
print('Stop loss price')
print(round(loss_price,1))
print('\n------------------------------\nStop '
      'Loss price is: \n{x}$ \n\nStop Loss Perc is: {y}% \n'
      '\n --------------------------------- \n'
      '\n'.format(x=round(loss_price, 1), y=round(((loss_perc) + 1) * 100, 2)))