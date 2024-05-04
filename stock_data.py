import yfinance as yf
import pickle

tsla = yf.Ticker('TSLA')

# 1st recommendation
print(tsla.recommendations["To Grade"].value_counts().keys()[0])

# 2nd recommendation
# print(tsla.recommendations["To Grade"].value_counts().keys()[1])

# with open('/tmp/script.out', 'wb+') as tmp_file:
#     pickle.dump({'test':'ok'}, tmp_file)