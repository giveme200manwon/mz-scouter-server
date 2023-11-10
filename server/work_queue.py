class WorkQueue:
	def __init__(self) -> None:
		self.queue = []

	def addQueue(self, work) -> int:
		self.queue.append(work)
		return len(self.queue)

	def popQueue(self):
		if len(self.queue) == 0:
			return {}
		return self.queue.pop(0)
