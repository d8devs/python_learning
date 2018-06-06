#################################
#Playing with String
print('*'*33)
#################################
'''
    Function    
'''
def example():
    message = jobOne()
    showMessage(message)

def jobOne():
    #Make this job
    i = 2 * 2
    #after job return value
    return "JOB completed"

def showMessage(message):
    print(message)

example()