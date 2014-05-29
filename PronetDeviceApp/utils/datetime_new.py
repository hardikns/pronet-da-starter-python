from datetime import datetime, timedelta

class datetime(datetime):
	def epoch(self):
		return long(self.strftime('%s%f'))/1000

	@staticmethod
	def fromEpoch(epoch_int):
		if not isinstance(epoch_int, (int, long)):
			raise Exception ('Input should be of type int or long')
		return datetime.fromtimestamp(epoch_int/1000) + timedelta(milliseconds=epoch_int%1000)
