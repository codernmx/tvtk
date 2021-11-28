#!/d:\\learn_tvtk\\chapter python3.7.7
# -*- coding: utf-8 -*-


from traits.api import Delegate, HasTraits, Instance, Int, Str, on_trait_change

# class Parent(HasTraits):
# 	last_name = Str("zhang")
# class Child(HasTraits):
# 	"""docstring for Child"""
# 	name = Str
# 	doing = Str
# 	age = Int
# 	# father = Instance(Parent)
# 	# last_name = Delegate("father")

# 	def __str__(self):
# 		return "%s<%x>" % (self.name, id(self))
# 	def _age_changed(self, old, new):
# 		print("Age changed from %s to %s " % (old, new))
# 	def _anytrait_changed(self, name, old, new):
# 		print("anytraits changed: %s.%s from %s to %s " % (self, name, old, new))
		
# def log_trait_changed(obj, name, old, new):
# 	print("log: %s.%s from %s to %s " % (obj, name, old, new))

# def test01():
# 	z = Child(name = "zhangsan", age = 4)
# 	l = Child(name = 'lisa', age = 1)
	
# 	z.on_trait_change(log_trait_changed, name = "doing")

from traits.api import Event
class Child(HasTraits):
	name = Str("zhangsan")
	age = Int(4)
	Infoupdated = Event
	@on_trait_change("name,age")
	def _Info_changed(self):
		self.Infoupdated = True
	def _Infoupdated_fired(self):
		self.reprint()
	def reprint(self):
		print("reprint infomation %s , %s" % (self.name, self.age))

# if __name__=="__main__":
# 	test02()
