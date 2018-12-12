# special character
valid_username = ['_', '-']


def email_checker(address):
    # ex. lara-98@codeta.com
    try:
        username = address.split('@')[0] # lara-98
        rest = address.split('@')[1] # codeta.com
        row = rest.split('.')
        websitename = row[0] # codeta
        extension = row[1] # com

        # Check if there is country code
        if len(row) > 2:
            country_code = row[2]
        else:
            country_code = ''

        # Check each character of username is alphabet, number or special character
        for ele in username:
            if not ele.isalpha():
                if not ele.isnumeric():
                    if not ele in valid_username:
                        return 'Invalid'
            elif not ele.islower():
                return 'Invalid'

        # Check each character of websitename is alphabet, number
        for ele in websitename:
            if not ele.isalpha():
                if not ele.isnumeric():
                    return 'Invalid'
            elif not ele.islower():
                return 'Invalid'

        # Check extension length
        if len(extension) > 3:
            return 'Invalid'

        # Check country code length
        if country_code:
            if not len(country_code) == 2:
                return 'Invalid'

        return 'Valid'
    except:
        return 'Invalid'


iteration = int(input())
for ele in range(iteration):
    email = input()
    print(email_checker(email))