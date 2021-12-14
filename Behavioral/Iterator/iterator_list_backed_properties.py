class Creature:
	_strength_idx = 0
	_agility_idx = 1
	_intelligence_idx = 2

	def __init__(self, race, name):
		self.race = race
		self.name = name
		self._stats = [10, 10, 10] # list backed OR array backed


	# STATS
	@property # getter
	def stats(self):
		return self._stats

	@stats.setter # setter
	def set_stats(self, l):
		if any(x < 0 for x in l):
			raise ValueError('Cannot use negative numbers.')
		self._stats = l


	# STRENGTH
	@property # getter
	def strength(self):
		return self.stats[Creature._strength_idx]
	
	@strength.setter # setter
	def strength_is(self, value):
		self.stats[Creature._strength_idx] = value


	# AGIILITY
	@property # getter
	def agility(self):
		return self.stats[Creature._agility_idx]
	
	@agility.setter # setter
	def agility_is(self, value):
		self.stats[Creature._agility_idx] = value


	# INTELLIGENCE
	@property # getter
	def intelligence(self):
		return self.stats[Creature._intelligence_idx]
	
	@intelligence.setter # setter
	def intelligence_is(self, value):
		self.stats[Creature._intelligence_idx] = value
	

	# AGGREGATE PROPERTIES
	@property
	def sum_of_stats(self):
		return sum(self.stats)
	
	@property
	def max_stat(self):
		return max(self.stats)
	
	@property
	def avg_stat(self):
		return float(self.sum_of_stats / len(self.stats))


	def __str__(self):
		return f"{self.name} ({self.race}):\n\t"+\
					 f"Strength: {self.strength}\n\t"+\
					 f"Agility: {self.agility}\n\t"+\
					 f"Intelligence: {self.intelligence}\n\t"+\
					 f"Stat Sum: {self.sum_of_stats}\n\t"+\
					 f"Stat Max: {self.max_stat}\n\t"+\
					 f"Stat Avg: {self.avg_stat}"
	

if __name__ == "__main__":
	orc1 = Creature("Orc", "Ikball the Destroyer")

	orc1.strength_is = 500
	print(orc1)

	orc1.set_stats = [5, 5, 5]
	print(orc1)