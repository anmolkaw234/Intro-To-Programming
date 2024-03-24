import os
import json

def write_to_file(addrbook):
  with open('addrbook.txt', 'w') as f:
    for name in addrbook:
      f.write(name + '\n')
      f.write(addrbook[name]['address'] + '\n')
      f.write(addrbook[name]['phone'] + '\n')
      f.write(addrbook[name]['email'] + '\n')


def read_from_file():
  addrbook = {}
  if os.path.exists('addrbook.txt'):
    with open('addrbook.txt', 'r') as f:
      lines = f.readlines()
      i = 1
      while i < len(lines):
        name = lines[i-1].strip()
        address = lines[i].strip()
        phone = lines[i+1].strip()
        email = lines[i+2].strip()
        addrbook[name] = {'address': address, 'phone': phone, 'email': email}
        i += 4
    return addrbook
  

def insert_entry(addrbook):
  name = input("Enter name: ")
  address = input("Enter address: ")
  phone = input("Enter phone number: ")
  email = input("Enter email: ")
  addrbook[name] = {'address': address, 'phone': phone, 'email': email}


def delete_entry(addrbook):
  name = input("Enter name: ")
  if name in addrbook:
    del addrbook[name]
  else:
    print("No such name found.")


def find_by_name(addrbook):
  name = input("Enter partial name: ")
  matching_names = []
  for n in addrbook:
    if name in n:
      matching_names.append(n)
  return matching_names


def find_by_phone_or_email(addrbook):
  search_term = input("Enter phone number or email: ")
  matching_entries = []
  for name in addrbook:
    if search_term == addrbook[name]['phone'] or search_term == addrbook[name]['email']:
      matching_entries.append(name)
  return matching_entries


def main():
  addrbook = read_from_file()
  while True:
    print("1. Insert a new entry")
    print("2. Delete an entry")
    print("3. Find all matching entries by name")
    print("4. Find an entry by phone number or email")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
      insert_entry(addrbook)
    elif choice == '2':
      delete_entry(addrbook)
    elif choice == '3':
      names = find_by_name(addrbook)
      for name in names:
        print(name)
    elif choice == '4':
      names = find_by_phone_or_email(addrbook)
      for name in names:
        print(name)
    elif choice == '5':
      write_to_file(addrbook)
      break
    else:
      print("Invalid choice.")
      


main()

