task_in_mind = int(input("How many tasks in mind? : "))
lista = []
for i in range(task_in_mind):
  query = input("What do you want to perform? (Add/view/remove) a task : ").lower()
  if query == 'add':
    task = input("What's on your mind? : ")
    lista.append(task)
  elif query == 'view':
    for entries in lista:
      print(entries)
  elif query == 'remove':
    entry = int(input("What item do you want to remove? (Answer in indices)"))
    del lista[entry]
  else:
    print("Invalid entry!")