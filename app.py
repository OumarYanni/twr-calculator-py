import pandas as pd

# Load dataset from external file
data = pd.read_json('data.json')

# Sort data by Date
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')

# Initialize columns for Equity Avant and Apres
data['Valeur totale portefeuille AVANT event'] = 0.0
data['Valeur totale portefeuille APRES event'] = 0.0

# Initialize the first "Avant" value
data.loc[data.index[0], 'Valeur totale portefeuille AVANT event'] = data.loc[data.index[0], 'Flux de trésorerie (net_amount)']
data.loc[data.index[0], 'Valeur totale portefeuille APRES event'] = data.loc[data.index[0], 'Flux de trésorerie (net_amount)']

# Calculate the values for each subsequent row
for i in range(1, len(data)):
    data.loc[data.index[i], 'Valeur totale portefeuille AVANT event'] = data.loc[data.index[i - 1], 'Valeur totale portefeuille APRES event']
    data.loc[data.index[i], 'Valeur totale portefeuille APRES event'] = (
        data.loc[data.index[i], 'Valeur totale portefeuille AVANT event'] +
        data.loc[data.index[i], 'Flux de trésorerie (net_amount)']
    )

# Display the results
print(data[['Date', "Type d'Activité (activity_type)", 'Valeur totale portefeuille AVANT event', 'Valeur totale portefeuille APRES event']])
