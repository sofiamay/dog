SEGMENT_LENGTH = 16

class Board():
	def __init__(self, numplayers: int):
		self.numplayers = numplayers
		self.ring_size = SEGMENT_LENGTH * numplayers
		self.main_ring = [None for i in range(self.ring_size)]
		self.num_in_kennel = [4 for player in range(numplayers)]
		self.homes = [[None, None, None, None] for player in range(numplayers)]

	def __str__(self):
		out = '{} player board ({} spaces):\n{}\n'.format(self.numplayers, self.ring_size, self.__printhelper(self.main_ring))
		for i in range(self.numplayers):
			out += "Player {}: Kennel: {} Home: {}\n".format(i+1, self.num_in_kennel[i], self.__printhelper(self.homes[i]))
		return out

	def __printhelper(self, value):
		return " ".join([str('_' if v is None else v) for v in value])

	def homeOwner(self, index):
		if index % SEGMENT_LENGTH == 0:
			return (index // SEGMENT_LENGTH) + 1
		return None

	def isOwnerOccupied(self, index):
		owner = self.homeOwner(index)
		if owner is None:
			return False
		return self.main_ring[index] == owner

	def placeAtLocation(self, player, index):
		current_occupant = self.main_ring[index]
		if current_occupant is not None:
			self.num_in_kennel[current_occupant] += 1
		self.main_ring[index] = player

	def canMakeReverseMove(self, player, start_index, distance):
		if self.main_ring[start_index] != player:
			return False
		for i in range(distance):
			index_to_check = (start_index + self.ring_size - (1 + i)) % self.ring_size
			if self.isOwnerOccupied(index_to_check):
				return False
		return True

	def makeReverseMove(self, player, start_index, distance):
		if not self.canMakeReverseMove(player, start_index, distance):
			return False
		self.main_ring[start_index] = None
		destination = (start_index + self.ring_size - distance) % self.ring_size
		self.placeAtLocation(player, destination)
		return True

	def canMakeNormalMove(self, player, start_index, distance):
		if self.main_ring[start_index] != player:
			return False
		for i in range(distance):
			index_to_check = (start_index + 1 + i) % self.ring_size
			if self.isOwnerOccupied(index_to_check):
				return False
		return True

	def makeNormalMove(self, player, start_index, distance):
		if not self.canMakeNormalMove(player, start_index, distance):
			return False
		self.main_ring[start_index] = None
		destination = start_index + distance % self.ring_size
		self.placeAtLocation(player, destination)
		return True

	def canMakeSwapMove(self, player, first_piece_position, second_piece_position):
		return main_ring[first_piece_position] == player and not self.isOwnerOccupied(first_piece_position) and not self.isOwnerOccupied(second_piece_position)

	def makeSwapMove(self, player, first_piece_position, second_piece_position):
		if not self.canMakeSwapMove(player, first_piece_position, second_piece_position):
			return False
		main_ring[first_piece_position] = main_ring[second_piece_position]
		main_ring[second_piece_position] = player
		return True

	def canMakeComeoutMove(self, player):
		start_space_index = player * SEGMENT_LENGTH
		return self.num_in_kennel[player] > 0 and not self.isOwnerOccupied(start_space_index)

	def makeComeoutMove(self, player, distance):
		if not self.canMakeComeoutMove(player):
			return False
		start_space_index = player * SEGMENT_LENGTH
		final_location = start_space_index + distance - 1
		self.num_in_kennel[player] -= 1
		self.placeAtLocation(player, final_location)
		return True
		
	def canMakeIntoHomeMove(self, player, start_index, distance):
		start_space_index = player * SEGMENT_LENGTH
		if self.isOwnerOccupied(start_space_index):
			return False
		final_location = (start_index + distance % self.ring_size) - start_space_index
		if final_location > 4 or final_location < 1:
			return False
		for i in range(0, final_location):
			if self.homes[player][i] != None:
				return False
		return True

	def makeIntoHomeMove(self, player, start_index, distance):
		if not self.canMakeIntoHomeMove(player, start_index, distance):
			return False
		start_space_index = player * SEGMENT_LENGTH
		final_location = (start_index + distance % self.ring_size) - (start_space_index + 1)
		self.main_ring[start_index] = None
		self.homes[player][final_location] = player
		return True

	def canMakeInsideHomeMove(self, player, start_index, distance):
		home = self.homes[player]
		final_location = start_index + distance
		if final_location >= len(home):
			return False
		for i in range(start_index+1, final_location+1):
			if 


	def canMakeSplitMoves(self, player, homeMoves, normalMoves):
		trialHome = self.homes[player].copy()
		trialMain = self.main_ring.copy()
		for [start_index, distance] in homeMoves:
			if 





NUM_PLAYERS = 4

board = Board(NUM_PLAYERS)

print(board)
board.makeComeoutMove(0, 13)
print(board)
board.makeComeoutMove(1, 1)
print(board)
board.makeReverseMove(1, 16, 4)
print(board)
board.makeIntoHomeMove(1,12,8)
print(board)
