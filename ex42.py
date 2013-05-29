## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a class
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name 
		self.name = name

## Cat is-a class
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person has-a class
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a object
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm, what is this strange magic? 
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a object
class Salmon(Fish):
	pass

## Halibut is-a object
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## sputnik is-a Cat
sputnik = Cat("Sputnik")

## elizabeth is-a Person
elizabeth = Person("Elizabeth")

## elizabeth has-a pet
elizabeth.pet = sputnik

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
