import thirdparty_py_lib

'''
best part:
    easist line to get the envrionment we need
    no worry for checking and context manager, everything will be handled
    when the program is finished
    * maybe we can manually close a bag
    * dont be too greedy, make some restriction on assumption of this language
    - this language is never meant for libray, each file is just an atomic operation
'''
load ~/bags/example.bag as bag1 # do the examination here
load ../example2.bag as bag2 

'''
1. bag1 has msg like this:
  root_msg:
    meta
    available
    child_msg:
      some_array:
        item1:
          core
        item2:
          core
    other_msg:
      item

  msg should be treated as certain wrappered object
'''

# core idea:
# parsing this line to go direct to the msg object 
msg target_msg = bag1.root_msg.child_msg.some_array.0 
msg target_msg_2 = bag2.root_msg.some_array

# HOW TO Define the align
# als only save the signature to a variable, while msg is the object itself 
# the purpose is to somehow save the name-chain
# along with the above, make avoiding long verbose name possible
als bag1.root_msg.child_msg.some_array to _array
als bag1.root_msg.child_msg to _child
# _array = bag1.root_msg.child_msg.some_array.signature

target_msg = _array.msg

# we also need to know what obj we're operating on clearly
# Nah, can't really do that

#np result_container := target_msg.signature
#np result_2_container := target_msg_2.signature

intermedia_signature = target_msg.core.signature # equavilent object with the next line
intermedia_signature = _array.signature
intermedia_signature_2 = bag1.root_msg.available.signature


'''
2. we're only trying to retrive the msg and nothing else
   we probably can cut and save part of bag
'''
bag cut_bag = bag1[idx]->[filter_callback]


'''
3. mutual bag interactions
    how about an agent?
    register to the agent and communicate!
'''
@Agent1
bag1
  
@Agent1
bag2

@Agent2
bag1

@Agent1
def compute(sig1, sig2, ts1, ts2, other_sig, *, params) -> (result1, result2):
    if sig1.timestamp > th:
        result1 = sig1.value * sig2.value
        result2 = sig1.value - sig2.value
    
    


pipe multiple_data

@multiple_data
def compute(sig1, sig2):
    '''
    sig1 = intermedia_signature
    sig2 = target_msg.signature
    '''
    result = sig1.value * sig2.value
    if result > 0.1:
         

def sync():
    pass

go Agent1



'''
* 4. data reorganise/ data filter logic
  if it's too complicated, give a easy way to handle it in python way
'''

 
result_container.save{./data/, npy, untitled}


