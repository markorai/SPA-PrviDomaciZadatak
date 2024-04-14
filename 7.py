class Student:
  def __init__(self,ime,prezime,godina,prosjek):
    self.ime = ime
    self.prezime = prezime
    self.godina = godina
    self.prosjek = prosjek
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self,head = None):
    self.head = head
  
  def print_list(self):
    current = self.head
    while current:
      print("Ime:" + current.ime + ", Prezime:" + current.prezime + ", Godina:" + str(current.godina) + ", Prosjek:" + str(current.prosjek)  )
      current = current.next
  
  def append(self,new_node):
    if self.head:
      current = self.head

      while current.next:
        current = current.next
      
      current.next = new_node
      new_node.prev = current

    else:
      self.head = new_node

  def izracunaj_prosjek(self,godina):
    zbir_prosjeka = 0
    br_studenata_na_godini = 0
    current = self.head
    while current: 
      if current.godina == godina:
          zbir_prosjeka += current.prosjek
          br_studenata_na_godini += 1
      current = current.next
    
    return zbir_prosjeka / br_studenata_na_godini

  
  def stampaj_prethodne_obrnutno(self,index):
    if self.head is None:
      return None
    if self.head.next is None:
      return self.head
    
    counter = 1
    current = self.head
    while counter < index-1 and current.next:
      current = current.next
      counter += 1
    
    while current:
      print("Ime:" + current.ime + ", Prezime:" + current.prezime + ", Godina:" + str(current.godina) + ", Prosjek:" + str(current.prosjek)  )
      current = current.prev
    





  


student1 = Student("Marko","Marković",1,9.9)
student2 = Student("Janko","Janković",1,8.9)
student3 = Student("Ivan","Ivanović",1,7.9)
student4 = Student("Jovan","Jovanović",2,6.9)
student5 = Student("Rade","Radović",2,7.5)

studenti = DoublyLinkedList()

studenti.append(student1)
studenti.append(student2)
studenti.append(student3)
studenti.append(student4)
studenti.append(student5)

#print("Ukupan prosjek na 1. godini studija: " + str(studenti.izracunaj_prosjek(1))) 
#studenti.stampaj_prethodne_obrnutno(4)