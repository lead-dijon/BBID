import os
import cgi
import datetime


def application(environ, start_response) :
	
	
	display = ''
	for key in environ.keys() :
		display += f"{key} : {environ[key]}\n"
	
	query_string = cgi.parse_qs(environ['QUERY_STRING'])
	
	identifier = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
	arguments = f"-id {identifier}"
	
	if "width" in query_string.keys() :
		width = query_string["width"]
		arguments += f" -w {width[0]}"
	if "height" in query_string.keys() :
		height = query_string["height"]
		arguments += f" -ht {height[0]}"
	if "luminance1" in query_string.keys() :
		luminance1 = query_string["luminance1"]
		arguments += f" -lm {luminance1[0]}"
	if "luminance2" in query_string.keys() :
		luminance2 = query_string["luminance2"]
		arguments += f" {luminance2[0]}"
	if "luminance3" in query_string.keys() :
		luminance3 = query_string["luminance3"]
		arguments += f" {luminance3[0]}"
	if "size1" in query_string.keys() :
		size1 = query_string["size1"]
		arguments += f" -sz {size1[0]}"
	if "size2" in query_string.keys() :
		size2 = query_string["size2"]
		arguments += f" {size2[0]}"
	if "size3" in query_string.keys() :
		size3 = query_string["size3"]
		arguments += f" {size3[0]}"
	if "size4" in query_string.keys() :
		size4 = query_string["size4"]
		arguments += f" {size1[0]}"
	if "size5" in query_string.keys() :
		size5 = query_string["size5"]
		arguments += f" {size2[0]}"
	if "size6" in query_string.keys() :
		size6 = query_string["size6"]
		arguments += f" {size3[0]}"
	if "angle1" in query_string.keys() :
		angle1 = query_string["angle1"]
		arguments += f" -an {angle1[0]}"
	if "angle2" in query_string.keys() :
		angle2 = query_string["angle2"]
		arguments += f" -ax {angle2[0]}"
	if "angle3" in query_string.keys() :
		angle3 = query_string["angle3"]
		arguments += f" -as {angle3[0]}"
	if "texture1" in query_string.keys() :
		texture1 = query_string["texture1"]
		arguments += f" -t {texture1[0].split('-')[1]}"
	if "texture2" in query_string.keys() :
		texture2 = query_string["texture2"]
		arguments += f" {texture2[0].split('-')[1]}"
	if "texture3" in query_string.keys() :
		texture3 = query_string["texture3"]
		arguments += f" {texture3[0].split('-')[1]}"
	if "side11" in query_string.keys() and "side21" in query_string.keys() :
		side11 = query_string["side11"]
		side21 = query_string["side21"]
		arguments += f" -si {side11[0]}_{side21[0]}"
	if "side12" in query_string.keys() and "side22" in query_string.keys() :
		side12 = query_string["side12"]
		side22 = query_string["side22"]
		arguments += f" {side12[0]}_{side22[0]}"
	if "side13" in query_string.keys() and "side23" in query_string.keys() :
		side13 = query_string["side13"]
		side23 = query_string["side23"]
		arguments += f" {side13[0]}_{side23[0]}"
	if "shade11" in query_string.keys() and "shade21" in query_string.keys() :
		shade11 = query_string["shade11"]
		shade21 = query_string["shade21"]
		arguments += f" -sd {shade11[0]}_{shade21[0]}"
	if "shade12" in query_string.keys() and "shade22" in query_string.keys() :
		shade12 = query_string["shade12"]
		shade22 = query_string["shade22"]
		arguments += f" {shade12[0]}_{shade22[0]}"
	if "shade13" in query_string.keys() and "shade23" in query_string.keys() :
		shade13 = query_string["shade13"]
		shade23 = query_string["shade23"]
		arguments += f" {shade13[0]}_{shade23[0]}"
	if "items" in query_string.keys() :
		items = query_string["items"]
		arguments += f" -it {items[0]}"
	if "bar" in query_string.keys() :
		bar = query_string["bar"]
		arguments += f" -b {bar[0]}"
	if "address1" in query_string.keys() :
		address = query_string["address1"]
		arguments += f" -@ {address[0]}"
	display += f"{query_string}\n"
	display += f"arg ={arguments}\n"
	
	
	os.system(f"python3 /home/expe/public_html/bbid/py/bbid_call.py {arguments} &")
	
	
	start_response("301 Moved Permanently", [("Location", f"~expe/bbid/web/results.html?id={identifier}")])
	
	
	return []
