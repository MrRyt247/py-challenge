current_users = [
    'Alice',
    'John',
    'Kobby',
    'Willis',
    'Vance'
]

new_users = [
    'wiLLis',
    'Metz',
    'Vance',
    'Metz',
    'Ruth'
]

current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'You need to enter a new username. {new_user} has been already used.')
    else:
        print(f'{new_user} is available')
        