import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC98df90d13d90d9adbfccce1c56bb869b"
# Your Auth Token from twilio.com/console
auth_token  = "caa19356dce78bcac210f4020f02d97a"
client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')
        message = client.messages.create(
            to="+5500000000000",
            from_="+19896608763",
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')
        print(message.sid)



