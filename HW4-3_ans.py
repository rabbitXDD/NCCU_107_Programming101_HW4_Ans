import datetime

end = False
notificationList = []
while not end:
    try:
        line = input()
    except EOFError:
        # End of the input
        end = True
        break
    else:
        # For jupyter notebook test
        if line == '-1':
            end = True
            break

        order = line.split(', ') # ['101', '2018/11/21 10:59', 'Waiting']
        current_date = order[1].split()[0] # '2018/11/21'
        time = datetime.datetime.strptime(
            order[1], '%Y/%m/%d %H:%M'
        ) # datetime.datetime(2018, 11, 21, 10, 59)
        status = order[2] # 'Waiting'

        # Dealing with waiting order
        if status == 'Waiting':
            # if order time is Tuesday, check whether after 12:00 or not
            if time.weekday() == 2:
                # Default due time is 12:00 of order time date
                due_time = datetime.datetime.strptime(
                    '{} 12:00'.format(
                        current_date,
                    ), '%Y/%m/%d %H:%M'
                )

                # Order time is Tuesday and after 12:00
                if time - due_time > datetime.timedelta(seconds=1):
                    # Change due time to 12:00 of next Tuesday
                    due_time = time + datetime.timedelta((1 - time.weekday()) %
                                                         7 + 1)
                message = 'Your product will be canceled by {}/{} 12:00 if no payment then.'.format(
                    due_time.month, due_time.day
                )
                notificationList.append((order[0], message))
            else:
                # Find very next Tuesday after order time
                due_time = time + datetime.timedelta((2 - time.weekday()) % 7)
                message = 'Your product will be canceled by {}/{} 12:00 if no payment then.'.format(
                    due_time.month, due_time.day
                )
                notificationList.append((order[0], message))

        # Dealing with paid order
        elif status == 'Paid':
            # if order time is Thursday, check whether after 12:00 or not
            if time.weekday() == 4:
                # Default due time is 12:00 of order time date
                due_time = datetime.datetime.strptime(
                    '{} 12:00'.format(
                        current_date,
                    ), '%Y/%m/%d %H:%M'
                )
                # Order time is Tuesday and after 12:00
                if time - due_time > datetime.timedelta(seconds=1):
                    # Change due time to 12:00 of next Friday
                    due_time = time + datetime.timedelta((3 - time.weekday()) %
                                                         7 + 1)
                message = 'Your product will be shipped by {}/{} at the latest.'.format(
                    due_time.month, due_time.day
                )
                notificationList.append((order[0], message))
            else:
                # Find very next Friday after order time
                due_time = time + datetime.timedelta((4 - time.weekday()) % 7)
                message = 'Your product will be shipped by {}/{} at the latest.'.format(
                    due_time.month, due_time.day
                )
                notificationList.append((order[0], message))
        else:
            pass


# Sort by order number
def sortByOrderNumber(tupleList):
    return tupleList[0]


sorted_list = sorted(notificationList, key=sortByOrderNumber)
for ele in sorted_list:
    print(ele[0])
    print(ele[1])
