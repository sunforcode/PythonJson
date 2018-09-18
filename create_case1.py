import xlrd
class GenCasePy(object):
	# queryString  query
	# paramasString 构建的参数集合 "$baseAssets: [String!]!, $quoteAsset: String!"
	# portName  assetPrices 接口名称
	# inputObject
	def __init__(self,queryString,paramasString,portName,inputObject):
		'''
		:param case_file: excel文件名
		:param case_name: 生成的文件名，例如Case_reg
		'''
		self.case_file = case_file
		self.case_name = case_name
		self.


	def createFileClass(self,service):
		all_case_fun = '''
		class %s(object):
	
		''' % self.case_name
		open("%s.py","a+",encoding='utf-8')%service

	def create_py_file(self):

		all_case = self.create_case_file()
		print(all_case)
		for case in all_case:
			case_fun='''
	def {case_id}(*arg,**kwargs):
		title="{title}"
		detail="{detail}"
		step="{step}"

			'''.format_map(case)
			all_case_fun+=case_fun
		fw = open(self.case_name+'.py','w',encoding='utf-8')
		fw.write(all_case_fun)
p = GenCasePy('pany.xlsx','reg_login')
p.create_py_file()