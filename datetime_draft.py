import datetime

t1 = 0
t2 = 0
delta_t = 0

def t1(t):
	t1 = t + datetime.datetime.now()

def t2(t):
	t2 = t + datetime.datetime.now()
	delta_t = t2.microseconds - t1.microseconds
	dt_list.append(delta_t)
	
dt_list = []
counter = 0	
while True:
	
	#GPIO.wait_edge_detected(16)
	input("Start")
	t1(t2)
	#GPIO.wait_edge_detected(16)
	input("Stop")
	t2(t1)
	counter += 1
	if counter == 10
		break


print dt_list