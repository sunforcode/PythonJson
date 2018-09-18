


class OpFile(object):
    def __init__(self,caseName):
        self.caseName=caseName
        # 对应service,包括broker,matcher等等
        # 在RootObject文件里面fieldsService就是文件名字
def creatClassFile():


    pass

#     def createPfile(self):
#
#      all_case_fun='''
# from common.base import base
#
# class {className}(base):
#
# """
#     def cancelAllOrders(self,marketId):
#         query="""mutation ($marketId: String) {
#   cancelAllOrders(input: {marketUuid: $marketId}) {
#     orders {
#       id
#       __typename
#     }
#     __typename
#   }
# }
# """
#         operationName = None
#         variables = {
#             "marketId":marketId
#             }
#         return self.request(query, operationName, variables)
#
#                 '''.format_map(case)
#                 all_case_fun+=case_fun
#             fw = open(self.case_name+'.py','w',encoding='utf-8')
#             fw.write(all_case_fun)
#
#
#
#
#
#
#
#
#





#     def cancelAllOrders(self,marketId):
#         query="""mutation ($marketId: String) {
#   cancelAllOrders(input: {marketUuid: $marketId}) {
#     orders {
#       id
#       __typename
#     }
#     __typename
#   }
# }
# """
#         operationName = None
#         variables = {
#             "marketId":marketId
#             }
#         return self.request(query, operationName, variables)