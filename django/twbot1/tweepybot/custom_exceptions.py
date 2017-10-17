class ExceptionErrorOnLoadingImg(Exception):
	def __init__(self, message, errors):
		super(ExceptionErrorOnLoadingImg, self).__init__(message)
		self.errors = errors