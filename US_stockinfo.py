# 10/15/2020 #小翅膀厨
# -*- coding: utf8 -*-

import re
import urllib.request
from datetime import datetime
import time

#function timer
def timer():
    i = 0
    while i < 60:
        #extract table and rows from website
        with urllib.request.urlopen('https://finance.yahoo.com/most-active') as u2:
            str1 = u2.read().decode('utf-8')
            pattern1 = "<table.+</table>"
            table_string = re.findall(pattern1, str1)
            pattern2 = "<tr.+?</tr>"
            row_list = re.findall(pattern2, str(table_string))
            a_row = row_list
            symbol_pattern = "Symbol.+?<a.+?>(.+?)</a>"
            symbol_txt = re.findall(symbol_pattern, str(a_row))

            #file operation
            fd = open('table.txt', 'w')
            fd.write(table_string[0])  # just one table
            fd.close()

            f1 = open('rows.txt', 'w')
            f1.write(str(row_list))
            f1.close()

            f3 = open('rows.txt', 'r')
            a_row = f3.read()

            # regex pattern
            symbol_pattern = "Symbol.+?<a.+?>(.+?)</a>"
            name_pattern = 'Symbol.+?<a.+?title="(.+?)"\sclass'
            price = 'Symbol.+?<a.+?<span.class=.+?reactid=.+?>(.+?)</span'
            change_pattern = '<tr.+?<td\scolspan=.+?Change"\sdata-reactid=.+?".+?>(.+?)</span>'
            percent_pattern = 'Fz.+?aria-label="%\sChange".+?<span\s.+?data-reactid=.+?>(.+?)</span'
            volume_pattern = 'Volume.+?<span.+?data-reactid=.+?>(.+?)</span>'
            volavg_pattern = 'Avg Vol.+?react-text.+?>(.+?)<!-- /react-text -->'
            market_pattern = 'Market.+?<span.+?data-reactid=.+?>(.+?)</span>'
            pe_pattern = '<tr.+?<td\scolspan=.+?PE\sRatio\s.TTM."\sdata-reactid=.+?".+?>(.+?)<.+?</td>'


            # search using regex
            symbol = re.findall(symbol_pattern, str(a_row))
            stock_name = re.findall(name_pattern, (str(a_row)))
            stock_price = re.findall(price, (str(a_row)))
            stock_change = re.findall(change_pattern, (str(a_row)))
            percent_change = re.findall(percent_pattern,(str(a_row)))
            volume = re.findall(volume_pattern, (str(a_row)))
            volumeavg = re.findall(volavg_pattern, (str(a_row)))
            market_cap = re.findall(market_pattern, (str(a_row)))
            pe_ratio = re.findall(pe_pattern, (str(a_row)))

            # cleanning&formating

            del volume[0]
            del volumeavg[0]
            del market_cap[0]
            #add key entry to the table
            symbol.insert(0,'Symbol')
            stock_name.insert(0,'Name')
            stock_price.insert(0,'Price')
            stock_change.insert(0,'Change')
            percent_change.insert(0,'Percent_Change')
            volume.insert(0,'Volume')
            volumeavg.insert(0,'Aveg_Volume')
            market_cap.insert(0,'Market_Cap')
            pe_ratio.insert(0,'PE_Ratio')

            # recorde time
            now = datetime.now()
            genertime = now.strftime("%d/%m/%Y %H:%M:%S" + " +" + "0000")
            
            # output to table
            with open('table.tab','w') as f4:
                f4.write(genertime+'\n')
                for c in range(len(symbol)):
                    f4.write("{:<16}{:<64}{:<16}{:<16}{:<16}{:<16}{:<16}{:<16}{:<16}\n".format(symbol[c],stock_name[c],stock_price[c],stock_change[c],percent_change[c],volume[c],volumeavg[c],market_cap[c],pe_ratio[c]))

            time.sleep(10)
            i = i+1


timer()
