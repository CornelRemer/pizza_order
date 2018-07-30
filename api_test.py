"""
    * short script to test an API
    * by Cornel Remer
        1. get all orders with 'GET-request'
        2. add a new order with 'POST-request'
        3. change 'pizza_id' of new order with 'OUT-request'
        4. delete last order with 'DELETE-request'
        5. safe responses and http status code in '.\api_testing_protocol.txt'
"""
import requests
import datetime

f = open("api_testing_protocol.txt", "w")                       # open API test protocoll
url = 'http://127.0.0.1:8000/orders/'                           # URL

f.write('Date:' + str(datetime.date.today()) + '\n')            # write date of test
f.write('API testing for: %s' % (url))                          # write test url

# ======= testing 'GET' request =======
f.write('\n\n' + 'GET-request \n')
r = requests.get(url)                                           # send get request
if r.status_code == requests.codes.ok:                          # check response http status code
    f.write('\tStatus Code: %s' % (r.status_code) + '\n')
    f.write('\theaders:\n\t' + str(r.headers) + '\n')
    f.write('\tbody:\n\t' + str(r.json()) + '\n')
else:
    f.write('\t Status Code: %s' % (r.status_code) + '\n')

# ======= testing 'POST' request =======
f.write('\n' + 'POST-request \n')
new_order = {'pizza_id': '5',                                   # create new order
             'pizza_size': 'L',
             'customer_name': 'Fritz',
             'customer_address': 'Test Straße 1, 12345 Berlin'}
r = requests.post(url, data=new_order)                          # send post request
if r.status_code == 201:                                        # check response http status code
    f.write('\tStatus Code: %s' % (r.status_code) + '\n')
    f.write('\theaders:\n\t' + str(r.headers) + '\n')
    f.write('\tbody:\n\t' + str(r.json()) + '\n')
    json_str = r.json()
    id = json_str['id']                                         # get last order's 'id'
    success = True
else:
    f.write('\t Status Code: %s' % (r.status_code) + '\n')
    success = False

# ======= testing 'PUT' request =======
if success:
    f.write('\n\n' + 'PUT-request \n')
    url = url + str(id) + '/'                                   # add last order's 'id' to url
    update = {'pizza_id': '48',                                 # update the ordered pizza id (5 to 48)
              'pizza_size': 'L',
              'customer_name': 'Fritz',
              'customer_address': 'Test Straße 1, 12345 Berlin', }
    r = requests.put(url, data=update)                          # send put request to update the last order
    if r.status_code == 200:                                    # check response http status code
        f.write('\tStatus Code: %s' % (r.status_code) + '\n')
        f.write('\theaders:\n\t' + str(r.headers) + '\n')
        f.write('\tbody:\n\t' + str(r.json()) + '\n')
    else:
        print("Status Code: %s" % (r.status_code))
    
# ======= testing 'DELETE' request =======
    f.write('\n\n' + 'DELETE-request \n')
    r = requests.delete(url)                                    # send delete request to delete last order
    f.write('\tStatus Code: %s' % (r.status_code) + '\n')
    
f.close()                                                       # close API test protocoll