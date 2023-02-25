#! /usr/bin/env python3

class Validator:
	valid_characters = '0123456789abcdefghijklmnopqrstuvwxyz'

	"""
		Validates a given vanilla siteswap
	"""
	def validate(self, siteswap: str) -> bool:
		if not self.num_balls(siteswap): return False
		if self.collisions(siteswap): return False
		return True

	"""
		Print the details of a given siteswap
			Number of objects, Period
	"""
	def print_details(self, siteswap: str) -> None:
		if not self.validate(siteswap):
			print(f"Invalid siteswap:  {siteswap}")
			return
		print(f"Siteswap:          {siteswap}")
		print(f"Number of objects: {self.num_balls(siteswap):0.0f}")
		print(f"Period:            {len(siteswap)}")
		print()

	"""
		Calculates the number of balls required to juggle a given siteswap
		Return None if the number is not whole or any character is invalid
	"""
	def num_balls(self, siteswap: str) -> int:
		try:
			total = sum(self._char_to_beats_(b) for b in siteswap)
		except TypeError: # Invalid character
			return None
		num_balls = total/len(siteswap)
		if num_balls%1: # Non-int number of balls
			return None
		return num_balls

	"""
		Returns True is a collision occurs for a given siteswap
	"""
	def collisions(self, siteswap: str) -> bool:
		landing = set((pos+self._char_to_beats_(b))%len(siteswap) for pos, b in enumerate(siteswap))
		return len(landing) != len(siteswap)

	"""
		Converts 1 character in the siteswap to the number of beats that character represents
			'1' -> 1
			'a' -> 10
		Invalid characters return None
	"""
	def _char_to_beats_(self, char: str) -> int:
		if not char in self.valid_characters:
			return None 
		try:
			return int(char)
		except ValueError:
			return ord(char) - ord('a') + 10

class MultiplexValidator:
	vanilla_characters = '0123456789abcdefghijklmnopqrstuvwxyz'
	multiplex_open = '['
	multiplex_close = ']'
	multiplex_characters = multiplex_open + multiplex_close

	def __init__(self):
		self.vanilla_validator = Validator()

	"""
		Validates a given multiplex siteswap
	"""
	def validate(self, siteswap: str) -> bool:
		if not any(c in siteswap for c in self.multiplex_characters): return self.vanilla_validator.validate(siteswap)
		if not self._valid_string_(siteswap): return False
		if not self.num_balls(siteswap): return False
		if self.collisions(siteswap): return False
		return True

	"""
		Print the details of a given siteswap
			Number of objects, Period
	"""
	def print_details(self, siteswap: str) -> None:
		if not self.validate(siteswap):
			print(f"Invalid siteswap:  {siteswap}")
			print()
			return
		print(f"Siteswap:          {siteswap}")
		print(f"Number of objects: {self.num_balls(siteswap):0.0f}")
		print(f"Period:            {self.period(siteswap)}")
		print()

	"""
		Calculates the number of balls required to juggle a given siteswap
		Return None if the number is not whole or any character is invalid
	"""
	def num_balls(self, siteswap: str) -> int:
		total = 0
		period = self.period(siteswap)
		for s in siteswap:
			try:
				total += self._char_to_beats_(s)
			except TypeError:
				continue
		num_balls = total/period
		if num_balls%1: # Non-int number of balls
			return None
		return num_balls

	"""
		Returns True is a collision occurs for a given siteswap
	"""
	def collisions(self, siteswap: str) -> bool:
		period = self.period(siteswap)

		required_landings = [0 for _ in range(period)]
		opened = False
		beat = 0
		for s in siteswap:
			if s == self.multiplex_open:
				opened = True
			elif s == self.multiplex_close:
				opened = False
				beat += 1
			elif opened:
				required_landings[beat] += 1
			else:
				required_landings[beat] += 1
				beat += 1

		actual_landings = [0 for _ in range(period)]
		opened = False
		beat = 0
		for s in siteswap:
			if s == self.multiplex_open:
				opened = True
			elif s == self.multiplex_close:
				opened = False
				beat += 1
			elif opened:
				actual_landings[(self._char_to_beats_(s)+beat)%period] += 1
			else:
				actual_landings[(self._char_to_beats_(s)+beat)%period] += 1
				beat += 1

		return required_landings != actual_landings

	def period(self, siteswap: str) -> int:
		period = 0
		opened = False
		for s in siteswap:
			if s == self.multiplex_open:
				opened = True
				period += 1
			elif s == self.multiplex_close:
				opened = False
			elif not opened:
				period += 1
		return period

	"""
		Converts 1 character in the siteswap to the number of beats that character represents
			'1' -> 1
			'a' -> 10
		Invalid characters return None
	"""
	def _char_to_beats_(self, char: str) -> int:
		if not char in self.vanilla_characters:
			return None 
		try:
			return int(char)
		except ValueError:
			return ord(char) - ord('a') + 10

	"""
		Returns True if every character is valid and all opening square brackets are closed
		There should also be at least 1 throw contained in any brackets
	"""
	def _valid_string_(self, siteswap):
		opened = False
		n_balls_multiplexed = 0
		for c in siteswap:
			if c == self.multiplex_open:
				if opened: return False
				opened = True
			elif c == self.multiplex_close:
				if not opened or n_balls_multiplexed == 0: return False
				opened = False
				n_balls_multiplexed = 0
			elif not c in self.vanilla_characters:
				return False
			elif opened:
				n_balls_multiplexed += 1
		return not opened