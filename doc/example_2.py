import xml.etree.ElementTree as Et
import matplotlib.pyplot as plt
from hz import load


# features
# easy retriving
# call_back computation
# filter
# save as npy or csv file
# 

root = Et.parse("./config/pair.xml").getroot()

brake_config = root.find("./group[@name='brake_test']")
base_path = brake_config.find("./meta/base_path").text



def run(pair_id):
    front_car = base_path + brake_config.find("./*[@id='%s']/front" % pair_id).text
    back_car = base_path + brake_config.find("./*[@id='%s']/back" % pair_id).text
    fusion_id = brake_config.find("./*[@id='%s']/fusion" % pair_id).text
    t1 = front_car + "@/topic/name/"
    t2 = back_car + "@/topic/name/"
    t3 = back_car + "@/fusion"
    m1 = front_car + "@/topic/name @ msgname.msgname.name.0.1.name"
    m2 = t1 + "x:/othername/[]/sdf[]/" # xpath extension support
    hz.mark(compute, msg1, msg2, *, arg1, arg2)

    

@Pipe
def compute(m1, m2):
    return m1 * m2


@Pipe
def filter(m3, t1, t2, *, args):
    {reg1, reg2}
    if reg1.notset:
        if t1 > args:
            reg1.set(t1)
    if m3.avialable:
        return m3 * 2


for i in range(1, 8):
    run(i)
hz.run()