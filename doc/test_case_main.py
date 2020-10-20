import xml.etree.ElementTree as Et
import matplotlib.pyplot as plt
import hz

root = Et.parse("./config/pair.xml").getroot()

brake_config = root.find("./group[@name='brake_test']")
base_path = brake_config.find("./meta/base_path").text

def run(pair_id):
    front_car = base_path + brake_config.find("./*[@id='%s']/front" % pair_id).text
    back_car = base_path + brake_config.find("./*[@id='%s']/back" % pair_id).text
    fusion_id = brake_config.find("./*[@id='%s']/fusion" % pair_id).text
    hz.exec("test_case.hz", front_car, back_car, * , fusion_id) 

for i in range(1, 8):
    run(i)


