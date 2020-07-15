from vlan_inventory.models import VLAN
from django.contrib.auth.models import User


def run():
    print('Checking users...')
    user = User.objects.filter(username='pietjepuk').exists() or \
                  User.objects.create_superuser('pietjepuk', 'pietjepuk@example.com', 'secret123').save()
    print('Checking users... DONE')


    print('Updating users...')
    user = User.objects.filter(username='pietjepuk').update(first_name='Pietje', last_name='Puk')
    print('Updating users... DONE')


    print('Adding Switches...')
    vlan = VLAN.objects.get_or_create(name='2222', description='VLAN voor applicatie Inkoop')
    vlan = VLAN.objects.get_or_create(name='5041', description='VLAN voor applicatie Finance')
    vlan = VLAN.objects.get_or_create(name='9933', description='VLAN voor applicatie Purchasing')
    vlan = VLAN.objects.get_or_create(name='9934', description='VLAN voor applicatie Security')
    print('Adding Switches... DONE')
