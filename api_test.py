"""
    * short script to test an API
    * by Cornel Remer
        1. get all orders with 'GET-request'
        2. add a new order with 'POST-request'
        3. change 'pizza_id' of new order with 'OUT-request'
        4. delete last order with 'DELETE-request'
    * all responses and http status codes are written to'.\api_testing_protocol.txt'
"""
import requests
import datetime

# function to store response data in 'api_testing_protocol.txt'
def fileWrite(title, r, newfile):
    global url

    if newfile == True:
        f = open("api_testing_protocol.txt", "w")               # open new API test protocoll
        f.write('Date:' + str(datetime.date.today()) + '\n')    # write date of test
        f.write('API testing for: %s' % (url))                  # write test url
    elif newfile == False:
        f = open("api_testing_protocol.txt", "a")             # open existing API test protocoll

    f.write('\n\n' + title + '-request\n')
    f.write('\tStatus Code: %s' % (r.status_code) + '\n')

    if r.status_code in (requests.codes.ok,
                        requests.codes.CREATED):
        f.write('\theaders:\n\t' + str(r.headers) + '\n')
        f.write('\tbody:\n\t' + str(r.json()) + '\n')

    f.close()

url = 'http://127.0.0.1:8000/orders/'                           # test url

# ======= testing 'GET' request =======
r = requests.get(url)
if r.status_code == requests.codes.ok:                          # check response http status code
    fileWrite("GET", r, True)                                   # write response in 'api_testing_protocol.txt'
else:
    fileWrite("GET", r, True)
    r.raise_for_status()

# ======= testing 'POST' request =======
new_order = {'pizza_id': '5',                                   # create new order
             'pizza_size': 'L',
             'customer_name': 'Fritz',
             'customer_address': 'Test Straße 1, 12345 Berlin'}
r = requests.post(url, data=new_order)                          # send post request
if r.status_code == requests.codes.CREATED:                     # check response http status code
    fileWrite("POST", r, False)
    json_str = r.json()
    new_id = json_str['id']                                     # get last order's 'id'
    success = True
else:
    fileWrite("POST", r, False)
    r.raise_for_status()
    success = False

# ======= testing 'PUT' request =======
if success == True:                                             # if new post was created
    url = url + str(new_id) + '/'                               # add last order's 'id' to url
    update = {'pizza_id': '48',                                 # update the ordered pizza id (5 to 48)
              'pizza_size': 'L',
              'customer_name': 'Fritz',
              'customer_address': 'Test Straße 1, 12345 Berlin', }
    r = requests.put(url, data=update)                          # send put request to update the last order
    if r.status_code == requests.codes.ok:                      # check response http status code
        fileWrite("PUT", r, False)
    else:
        fileWrite("PUT", r, False)
        r.raise_for_status()

# ======= testing 'DELETE' request =======
    r = requests.delete(url)                                    # send delete request to delete last order
    if r.status_code == requests.codes.NO_CONTENT:              # check response http status code
        fileWrite("DELETE", r, False)
    else:
        fileWrite("DELETE", r, False)
        r.raise_for_status()