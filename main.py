clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if clien_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already is in the client\'s list')

def list_clients():
    global clients
    print(clients)

def _add_coma():
    global clients
    clients += ','

def _print_welcome():
    print('WELCOME TO SPARTAN SALES')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print('[D]elete client')

if __name__ == "__main__":
    
    _print_welcome()
    command = input('Type option: ')

    if command == 'C' or command == 'c':
        clien_name = input('What is the client name? ')
        create_client(clien_name)
        list_clients()
    elif command == 'D' or command == 'd':
        pass
    else: 
        print('Invalid command')
