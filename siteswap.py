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