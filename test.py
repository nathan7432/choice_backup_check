import pandas

class Error(Exception):
    """Base class for other exceptions"""
    pass


class IncorrectHeadersError(Error):
    """Raised when the input value is too small"""
    pass

invoice_total = input("Input Invoice Total")
file_name = input("Input File Name")

df2 = pandas.read_csv(file_name)

df = pandas.read_csv('testcsv.csv', index_col='item')
# print(df)

# df2 = pandas.read_csv('netweekly-csv.csv')

correct_headers = ['Wk#', 'Partner', 'Client', 'SSL', 'Job Dte(dd/mm/yyyy)', 'Choice Pro#', 'Invoice#', 'Inv Dte(dd/mm/yyyy)', 'Category', 'Qty', 'Wght', 'Job Time(Military hh:mm)', 'Origin/Destination', 'FOB$', 'CIF$', 'AWB#', 'Kilo/Mile (One Way)', 'Hndlng Base Chg', 'Hndlng Exc Pcs Chg', 'Hndlng OCPU/WC', 'Transp Base Chg(G Tkt)', 'Transp Exc Mls Chg(G Tkt)', 'Fuel Chg', 'Aft. Hrs/weekend/holiday', 'Wait Time', 'Secrty/Tolls Chg', ' 3rd Party/Freight Transp.Chg(Z Tkt) ', ' Freight Fuel Surchg ', 'Cust. Clr', 'Duty', 'Imp/ Exp Vat', 'GST', 'Consump Tax', 'IOR Chg', 'Broker Chg', 'Cust. Storg Chg', 'Permit/ License Chg', 'K1 Form Chg', 'Layout Fee', 'Wire Chg', 'Labor Chg', 'Labor # hrs', 'Total Charge', 'Comments', 'difference']
sum_columns = ['Hndlng Base Chg', 'Hndlng Exc Pcs Chg', 'Hndlng OCPU/WC', 'Transp Base Chg(G Tkt)', 'Transp Exc Mls Chg(G Tkt)', 'Fuel Chg', 'Aft. Hrs/weekend/holiday', 'Wait Time', 'Secrty/Tolls Chg', ' 3rd Party/Freight Transp.Chg(Z Tkt) ', ' Freight Fuel Surchg ', 'Cust. Clr', 'Duty', 'Imp/ Exp Vat', 'GST', 'Consump Tax', 'IOR Chg', 'Broker Chg', 'Cust. Storg Chg', 'Permit/ License Chg', 'K1 Form Chg', 'Layout Fee', 'Wire Chg', 'Labor Chg']

df2['difference'] = df2['Total Charge'] - df2[sum_columns].sum(axis=1)
if list(df2) != correct_headers:
    raise IncorrectHeadersError
else:
    print("Headers Correct")
# if df2['difference'].sum() > .001:
#     raise error

# if invoice_total != df2['Total Charge'].sum():
#     raise TotalPDFError

