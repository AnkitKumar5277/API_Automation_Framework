# Contains common utilities
# read data from Excel file
# read data from the csv,json file
# set the headers --->application/json,application/xml
class Utils(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Contet-Type": "application/xml"
        }
        return headers

    def put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Contet-Type": "application/json",
            "Authorisation": "Basic" + str(basic_auth_value)
        }
        return headers

    def put_patch_delete_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token)
        }
        return headers
