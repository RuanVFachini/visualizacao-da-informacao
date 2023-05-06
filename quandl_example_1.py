import quandl
import pandas as pd
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = '2hWzSQjGnux_zcZA75rA'
tesla = quandl.get('WIKI/TSLA')
ibm = quandl.get('WIKI/IBM')

fig, ax = plt.subplots(2)

ax[0].plot(ibm.index, ibm['Adj. Close'])
#ax[0].ylabel('Preço ($)');

ax[0].set_title('Ações da IBM')

ax[1].plot(tesla.index, tesla['Adj. Close'], 'r')
ax[1].set_title('Ações da Tesla')
#ax[1].ylabel('Preço ($)')

plt.show()
