import math

# preload
load arg[0] as bag1
load arg[1] as bag2

fusion_id = arg[2]


# pipeline logic
t1 = bag1["/msd/vehicle_reporter/vehicle_status"]
t2 = bag2["/msd/vehicle_reporter/vehicle_status"]
t3 = bag2["/msd/perception/fusion_polygon"]
t4 = bag4["/msd/endpoint/state_report"]

# align
start_ts = max(t1.timestamp, t2.timestamp, t3.timestamp, t4.timestamp)
TIME = 20

@pipe.{"./data", "npy", "wheel"}
def wheel_speed(t4, *, start_ts, TIME) -> [brake_info, back_wheel_speed]:
    {_real_start_ts, _setted}
    if not _setted:
        if t4.time_stamp.to_sec() >= start_ts:
            _real_start_ts <- t4.time_stamp.to_sec()
            _setted <- True
    else:
        als t4.brake_report.available to flag
        als t4.brake_report.brake_report_data.pedal_ouput to pedal 
        als t4.wheel_speed_report to speed
        als speed.available to s_flag
        als speed.wheel_speed_report_data to wheel_data
        
        if flag:
            pedal -> brake_info
            
        if s_flag:
            speeds = [wheel_data.front_left, wheel_data.front_right, wheel_data.rear_left, wheel_data.rear_right]
            sum(speeds)/4.0 -> back_wheel_speed
 

run pipe
