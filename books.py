def add_book(books):
  str = 'Введите название и автор через пробел, или q для выхода'
  while True:
    try:
      title, author = input(str).split()
    except:
      print('Повторите ввод')
      break
