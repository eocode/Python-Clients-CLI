import sys
import csv

CLIENT_TABLE = 'clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _iniitialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    with open(CLIENT_TABLE, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    print('uid | name | company | email | position')
    print('*' * 50)

    for idx, client in enumerate(clients):
        name = client['name']
        company = client['company']
        email = client['email']
        position = client['position']
        print(f'{idx} | {name} | {company} | {email} | {position}')


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        _not_client_exist_message()


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _not_client_exist_message():
    print('Client is not in client\'s list')


def _print_welcome():
    print('WELCOME TO SPARTAN SALES')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name, message='What is the client {}?'):
    field = None
    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


if __name__ == "__main__":
    _iniitialize_clients_from_storage()

    _print_welcome()
    
    command = input('Type option: ').upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')

    _save_clients_to_storage()