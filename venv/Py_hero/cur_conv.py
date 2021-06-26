# Built A Currency Converter
# Take Input
# Convert using Predefined Rate
# Out Put Result in welformated Sentense


conv_rates = {'USD': 74.23, 'GBP': 103.06, 'CAD': 60.39, 'CHF': 80.95, 'AUD': 56.32, 'INR': 1}

usr_amt = int(input('Manu Note Wakha Mera Mode banay: '))
usr_cur = input('Oye Kera Mall haiga tery Kol: ')

if usr_cur == 'USD':
    conv_cur = usr_amt * conv_rates['USD']
elif usr_cur == 'GBP':
    conv_cur = usr_amt * conv_rates['GBP']
elif usr_cur == 'CAD':
    conv_cur = usr_amt * conv_rates['CAD']
elif usr_cur == 'CHF':
    conv_cur = usr_amt * conv_rates['CHF']
elif usr_cur == 'AUD':
    conv_cur = usr_amt * conv_rates['AUD']
elif usr_cur == 'INR':
    conv_cur = usr_amt * conv_rates['INR']
else:
    print(f'Sorry, Dorr Jan, Mainy Nai chahidey tery paisy')

print(f'Conversion Done: For {usr_amt} {usr_cur} you will get {conv_cur}')