# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:31:12 2019

@author: Owner1








if a product is out of stock -> then it will not be in the inventory health report








-lowest general price 
  -FBM may have shipping depending on case
  -Want to know the lowest price with (IF)(Shipping)
  
-Cheapest is "the box" chosen by amazon 
 -even if the prime price is 10 cents more than FBM price '
 
 
 -manage inventory report ******************
 - get general number of sellers regardless of type


"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itertools import islice
from datetime import date, timedelta
import datetime
import csv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import yaml
import re
from dateutil import parser

#from fake_useragent import UserAgent


    
def write_to_csv(master_list_this_run, file, fieldnames = None):
    with open(file, mode='w') as f:
        if isinstance(master_list_this_run[-2], list):
#          print('list')
          csv_writer = csv.writer(f, delimiter=',', lineterminator='\n')
          if fieldnames != None:
            csv_writer.writerow(fieldnames)
          for i in master_list_this_run:
            csv_writer.writerow(i)

        
        elif isinstance(master_list_this_run[-2], dict): 
          print('big dict')
          dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
          dict_writer.writeheader()
          for i in master_list_this_run:
#            try:
            dict_writer.writerow(i)
#            except:
#              print(i, 'error')
#          dict_writer.writeheader()
  
          
#        print('length  ', len(master_list_this_run))
        
        
            
    f.close()
        
    

def parse_price(string):
  price = 0
  prices=[i for i in (re.sub(r'[^0-9.\t]', ' ', string)).split(' ') if i != '']
  for i in prices:
    price += float(i)
    
  return price
  
parse_price('CAD$ 59.84\n+ CAD$0.00\nMatch price')

def build_file_name(name):
    today = str(date.today())
    return name + "_" + today + '.csv'




if __name__ == "__main__":
  
    start_url = r"https://sellercentral.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral.amazon.ca%2Fhome&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=sc_ca_amazon_v2&openid.mode=checkid_setup&language=en_CA&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=sc_ca_amazon_v2&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.O4woSvEuJKBUWdGtHh11IF04p--4GHSKVBWi4Hi6KdGANcAGJ1TjSw.pEeK4SLEUR1N6-V5.HFyWskLho2ZHoTiJkphHSgRpH3YI2rIYeKcLNq5myaOhzs5V9FBQEToizULL4Fh3NXqy1jpACXidH7KKbmMBeTtrsvFfiPxw5kCZZeArqpGua76UP0TugDcrtVMOuKo8S5OluU9X2KfymZbWi1ZGPP_LPWqtUJ5RDxRTCGIX7t6VDeqNJxOV2ya48zdWGdgaB8w-OsT_Lz6hWiL1h7d-v9n1q-Ne2dmMjbEPpjG3dTZpP5Z-FGB9wSPXRxzzFtd-5T9Ngg47ANyjYM3WE_ULNqbWCPXBZutmdE_y5bts9PcV9GiNut3B8SqEwQ-7Lpxv1R85i8DX5KXnCaccN91hv4IoSPLR2gcvFyDSvmggG_6PuRhMRS7VqMnEOhnp1_0E7D3NiiDDEq5DTKzzaeU5_gChTOACnpyY8MYWhp0FCyIxNLlmL9Xzih7jSs9-ka80VG0BV19kwHgaIYjbVvHug4_LusMKHn8zslujSZL_tDs4UPEZw8LgbZOetOjOiWoO9o9p9L5P2qVcB5lUK2Bem1612fF01vH8SDlwdc_qHfQHKa9ZNLgKZ1mMAy5fPoA4yxMfJb8CjIeCGIWecbVHIWTcE3T7e6dJY98gBiAW4wDDxUUY74PSz8sq9qSHW4RJLOE0gSV9TUOdUEjVjlnKIYRm2fCmb75cxNGXgTGORo4_No8sTE_clIZ9k9AFoHXdDBOlxXeU4VeKdqO9gygBLnrRekOF1GCzLGJRAdNZl5_MLrIYNMLOTDAfoGIQ9OcfIV-pdQj8umvRUVZ_NYugI7oPN1SoQRvADFKpOMU4zLLTCkXrijQOMXGjzbNZ.4rlFZj0wz6Iz12O6u3Ul9g"
    
    opts = Options()
    opts.add_argument("--user-data-dir=/home/galensprout/.config/google-chrome")
    
    driver = webdriver.Chrome(options=opts)
    driver.get(start_url)
    
    #============================================================================================================#
    
   
      #do password
    password_signin = driver.find_element_by_xpath("//input[@type='password']")
    
    password_signin.send_keys("***************")
    
    try: 
        email_signin = driver.find_element_by_xpath("//input[@type='email']")
        email_signin.send_keys("*******************")
    except:
        pass
      
    
    password_signin.submit()
    
    #===================================================================================#
  

      #add in if statement for two step verification 
      
      
    #===================================================================================#

    #======Begin internal scraping =====================================================#
    

    fulfills_url = "https://sellercentral.amazon.ca/hz/inventory/view/FBAKNIGHTS/ref=xx_fbamnginv_dnav_xx?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%2C%22sortedColumnId%22%3A%22date%22%7D;search:;pagination:1;"

    inv_health_url = r'https://sellercentral.amazon.ca/gp/ssof/reports/search.html#orderAscending=&recordType=INVENTORY_HEALTH&noResultType=&merchantSku=&fnSku=&FnSkuXORMSku=&reimbursementId=&orderId=&genericOrderId=&asin=&lpn=&shipmentId=&hazmatStatus=&inventoryEventTransactionType=&fulfillmentCenterId=&transactionItemId=&inventoryAdjustmentReasonGroup=&eventDateOption=1&fromDate=mm%2Fdd%2Fyyyy&toDate=mm%2Fdd%2Fyyyy&startDate=&endDate=&fromMonth=1&fromYear=2019&toMonth=1&toYear=2019&startMonth=&startYear=&endMonth=&endYear=&specificMonth=1&specificYear=2019'
    
    driver.get(inv_health_url)
    
    inv_health_length_row = 18
    
    next_button = (WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='tiny']//a"))))[-1]
    
    stop_condition = False
    master_health = []
    while stop_condition == False:
      
      
      try:
        inv_health_cells_this_page = driver.find_elements_by_xpath("//tbody//tr[@align='left']//td")
        inv_health_cells_this_page = [i.text for i in inv_health_cells_this_page]  
      except:
        sleep(3)
        inv_health_cells_this_page = driver.find_elements_by_xpath("//tbody//tr[@align='left']//td")
        inv_health_cells_this_page = [i.text for i in inv_health_cells_this_page]  
      
      i = 0
      page_table = []
      for cell in inv_health_cells_this_page: 
        if i % inv_health_length_row == 0:
          page_table.append([])
        try:
          page_table[-1].append(cell)
        except StaleElementReferenceException:
          try:
            inv_health_cells_this_page = driver.find_elements_by_xpath("//tbody//tr[@align='left']//td")
            page_table[-1].append(cell)
          except:
            inv_health_cells_this_page = driver.find_elements_by_xpath("//tbody//tr[@align='left']//td")
            page_table[-1].append(cell)

            
            
        i+=1
        
      print(page_table)
      
      for row in page_table:
        master_health.append(row)
      
      next_button = driver.find_elements_by_xpath("//td[@class='tiny']//a")[-1]
      
      if next_button.text == "Next":
          next_button.click()
          del inv_health_cells_this_page
      else:
        #last page and next is not present
        stop_condition = True
        #replace with next steps
        pages = next_button.text
        print(pages, " pages found")
        print(len(master_health))
#hello  
  
    headers = ['Merchant SKU','FNSKU','Title','Condition','Total Unsellable Quantity','Total Sellable Quantity','Sellable Age 271-365 days','Sellable Age 365+ days','Est. Long-Term Storage Units (6+ Months)','Est. Long Term Storage Units','Est. Long-Term Storage Fee (6+ Months)','Est. Long Term Storage Fee','Removal Units Requested','Units Shipped Last 30 days','Weeks of Cover Trailing 30 days','Your Price','Lowest New AFN Price','Lowest Used AFN Price']
    
    master_health = [dict(zip(headers, c)) for c in master_health]
    
    write_to_csv(master_health, build_file_name('inventory health'), fieldnames=headers)
    
    #==============================================================================================================#
    
    
#    driver.get(fulfills_url)
#    
    fulfills_table = []
    
    driver.get('https://sellercentral.amazon.ca/inventory/ref=xx_invmgr_dnav_xx?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%7D;search:;pagination:1;')
    
    #scrape each product 
      #build link to the page with all prices 
        #get lowest overall price
           #get number of prices found => number of sellers
             
           
           #bandaid with already written code for context
           
    

    
    #==============================================================================================================#
    idx = 1
    
    stop_condition = False
    while stop_condition == False:
    
      sleep(10)
      page_rows = driver.find_elements_by_xpath("//tbody//tr[@class='mt-row']")
 
      
      from_delayed = [yaml.load(row.get_attribute('data-delayed-dependency-data'), Loader=yaml.FullLoader)['MYIService'] for row in page_rows]      
      from_normal = [yaml.load(row.get_attribute('data-row-data'), Loader=yaml.FullLoader) for row in page_rows]
      
      #get sales rank and lowest price 
      sales_ranks = [re.sub('[^0-9]', '', elem.text) for elem in driver.find_elements_by_xpath("//td[@data-column='sales_rank']")]
      lpl = [parse_price(elem.text) for elem in driver.find_elements_by_xpath("//td[@data-column='lowPrice']")]
      
      price_inputs = driver.find_elements_by_xpath("//div[@data-column='price']//input[@maxlength='23']")
      
      your_price = [float(i.get_attribute('value')) for i in price_inputs]
      your_shipping = [parse_price(i.text) for i in driver.find_elements_by_xpath("//td[@data-column='price']")]
      your_price_tot = [x + y for x, y in zip(your_price, your_shipping)]
      
      
      j=0
      while j < len(lpl):
        if lpl[j] == 'Lowest':
          print('yes')
          lpl[j] = your_price_tot[j]  
        
        j+=1
 
      i=0
      while i < len(page_rows):
        computed = {
          'index': idx, 
          'rank': sales_ranks[i],
          'lowest_price': lpl[i],
#          'link_to_rank': 'https://www.amazon.ca/dp/' + from_delayed[i]['Asin'] + '?ref=myi_title_dp',
          'link_to_num_sellers': 'https://www.amazon.ca/gp/offer-listing/'+ from_delayed[i]['Asin']+ '/ref=dp_olp_new?ie=UTF8&condition=new'
          } 
        print(i)
        
        row = {**computed, **from_delayed[i], **from_normal[i], } 
        
        fulfills_table.append(row)
        idx+=1
        i+=1
        
        
      
      
      try:
        next_page = driver.find_element_by_xpath("//li[@class='a-last']//a[@href='#next']")
        next_page.click()
      except:
        try:
          is_end_of = driver.find_element_by_xpath("//li[@class='a-disabled a-last']")
          stop_condition = True
        except:
          print('I dunno')
    
    
    for item in fulfills_table: 
      driver.get(item['link_to_num_sellers']) #worth it? 
      num_tot_sellers = len(driver.find_elements_by_xpath("//span[@class='a-size-large a-color-price olpOfferPrice a-text-bold']")) #change xpath
      num_prime_sellers = len(driver.find_elements_by_xpath("//i[@class='a-icon a-icon-prime']"))
 
            
#              
#      except: 
#        print('hello')
#        try:
#          unavail = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-price']") 
#          result = 'amazon total stock = 0'       
#          
#        except:
#          try:
#            doge = driver.find_element_by_xpath("//img[@id='d']")
#            result = 'product not listed on Amazon'
#          
#          except:
#            result = 'product not found'
#            
 
      
 
      item['num_total_sellers'] = num_tot_sellers
      item['num_prime_sellers'] = num_prime_sellers
      del item['link_to_num_sellers']
#      del item['link_to_rank']
    
    print(fulfills_table)
    fieldnames = fieldnames=[str(i) for i in fulfills_table[3].keys()]+['fnsku','inboundQuantity']
    write_to_csv(fulfills_table, build_file_name('fba report'), fieldnames=fieldnames)  

#=================================================================================================================#
    
    #merge fulfills_table and master health
    
    #cases:
      #not in master_health -> will also have values for prime_sellers, etc. 
      #but wont have the headers for master health -> append as 0
        #in both -> wont have 'results'
    
    for ff_item in fulfills_table:
      match_found = False
      for h_item in master_health:
        if ff_item['Sku'] == h_item['Merchant SKU']:
          ff_item = {**ff_item, **h_item}
          match_found = True
      
      if match_found == False:
        h_item_placeholder = dict(zip(headers, ['NA, q=0' for i in headers]))
        ff_item = {**ff_item, **h_item_placeholder}
        
        
    tax_url = "https://sellercentral.amazon.ca/gp/tax/tax-library.html/ref=xx_taxlib_dnav_xx"
    driver.get(tax_url)
    
    driver.find_element_by_xpath("//a[@name='Generate a tax report']").click()
    
    date_elems = driver.find_elements_by_xpath("//input[@class='hasCal hasDatepicker']")
    
    todays_date = datetime.datetime.today() -timedelta(days=3)
    td_day = todays_date.day
    td_mon = todays_date.month
    td_year = todays_date.year
    
    nty_day_ago = todays_date - timedelta(days=87)
    
    nty_day = nty_day_ago.day
    nty_mon = nty_day_ago.month
    nty_year = nty_day_ago.year
    
    date_elems[0].send_keys(str(nty_mon)+'/'+str(nty_day)+'/'+str(nty_year))
    date_elems[1].send_keys(str(td_mon)+'/'+str(td_day)+'/'+str(td_year))
    
    driver.find_element_by_id("txdlInvoiceNotice").click()
    sleep(2)
    driver.find_element_by_xpath("//a[@name='Generate']").click()
    
    dtbl = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    filename = '/home/galensprout/Downloads/' + str(nty_year)+dtbl[nty_mon - 1]+str(nty_day)+'-'+str(td_year)+dtbl[td_mon - 1]+str(td_day + 1)+'_CustomSalesTax.csv'
    
    sleep(5)
    ready = False
    while ready == False:
      try:
        print([i.text for i in driver.find_elements_by_xpath("//td")[0:10]])
        status = driver.find_elements_by_xpath("//td")[5].text
        assert status == 'Download tax report'
        ready = True
      except:
        
        sleep(60)
        driver.refresh()
        
    driver.find_elements_by_xpath("//a[@name='Download tax report']")[0].click()
    
    sleep(10)
    
    tax_data=[]
    
#    filename= '/home/galensprout/Downloads/2019Jul20-2019Oct19_CustomSalesTax.csv'
    with open(filename, mode = 'r') as f:
      reader=csv.DictReader(f)
      for line in reader:
        if line['ASIN'] != '':  
          tax_data.append(line)

    unique_asin = []
#    print(nty_day_ago)
    for entry in tax_data:
      if [entry['ASIN']] not in unique_asin:
        unique_asin.append([entry['ASIN']])  
        
    tracker_obj = [0 for i in range(92)]
    for asin in unique_asin:
      asin += tracker_obj
    
    print(unique_asin)
    
    for asin_arr in unique_asin:    
      for entry in tax_data:  

        if entry['ASIN'] == asin_arr[0]:
          day = (parser.parse(entry['Posted_Date'].split('+')[0]) - nty_day_ago).days + 3
          if day > len(asin_arr):
            print(day)
            print(entry)
          else:
            asin_arr[day] += int(entry['Quantity'])
#          if day > len(asin_arr):
#          print('ima day', day)
#          else:
#          asin_arr[day] += int(entry['Quantity'])
            
        
          
          asin_arr[2] += int(entry['Quantity'])
          if 60 < day < 90:
            asin_arr[1] += int(entry['Quantity'])
            
    keys = ['ASIN', '30 Day', '90 day'] + ['Day %s' % i for i in range(1,91)]
    
    unique_dicts = []
    for asin in unique_asin:
      unique_dicts.append(dict(zip(keys, asin)))
    
    print(unique_dicts[0])
    
    print(len(keys))
    print(len(unique_asin[-1]))
    
    write_to_csv(unique_dicts, 'tax_file_test.csv', fieldnames=keys)
    
    
    #======================================MERGE============================================================================#
    
    po_data = []
    for f_item in fulfills_table:
      for t_item in unique_dicts:
        if t_item['ASIN'] == f_item['Asin']:
          new_item = {**f_item, **t_item}
          del new_item['Type']
          del new_item['decimalSeperator']
          del new_item['price']
          del new_item['asin']
          del new_item['sku']
          del new_item['productType']
          del new_item['ASIN']
          del new_item['index']
          po_data.append(new_item)
    
    
    for item in po_data:
      item['Days_Of_Supply'] = ''
    #report calculations
      #days of supply = #inventory-level / no. bought per 30 days 
      
    
      #buy box price = lowest ;; formatting bs
      
      #fees = winning_price * 0.2 + 6
      
      #Buy box price net margin = winning_price - fees - Price to genesis (also called price)
        #margin = this/winning_price
      
      #pricetoGenesis = ASIN with Repo -> UPC -> UPC with 'V price lists' -> GenPrice ,, add to dict; display
      
    
    
    #Not finished yet
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    