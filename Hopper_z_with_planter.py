#!/usr/bin/env python3

import Parameters

Hopper_z_axis_home_position = 0
Hopper_z_axis_ground_position = -25000

Cone_close_position=0
Cone_open_position=250


##########------------------------------------------------------------------To run in position mode-----------------------##########

#Initialize hopper_z axis motor and set it in position mode
Parameters.Set_Motor_operating_mode(Parameters.Hopper_Z_axis_slaveid,Parameters.Position_mode)
print('\n**********Hopper_Z_axis_parameters are**********')
Parameters.Read_Motor_operating_parameters(Parameters.Hopper_Z_axis_slaveid)

#Initialize hopper_cone motor and set it in position mode
#Parameters.Set_Motor_operating_mode(Parameters.Hopper_gripper_slaveid,Parameters.Position_mode)
print('\n**********Hopper_Cone_parameters are**********')
#Parameters.Read_Motor_operating_parameters(Parameters.Hopper_gripper_slaveid)

print (' \n Verify encoder reading is zero and press ENTRE to run in auto mode \n ********Else restart system********')
input()


##########-------------------------------------------Run Hopper in position mode--------------------------------------------##########


# Steps of operation
#1.Hopper is in home position with gripper closed
#2.Hopper moving down/ground position
#3.Hopper Gripper opening
#4.Hopper moving up
#5.Hopper gripper closing
#6.Hopper at home position with gripper closed


while True:
    #Hopper_moving_to_ground_position
    print( ' Hopper_moving_to_ground_position ')
    Parameters.Run_Motor_in_position_mode(Parameters.Hopper_Z_axis_slaveid,Parameters.Hopper_Z_Axis_speed,Parameters.Hopper_Z_Axis_acceleration,Parameters.Hopper_Z_Axis_deacceleration,Hopper_z_axis_ground_position)
    Hopper_z_encoder_reading = Parameters.Read_Encoder_Data(Parameters.Hopper_Z_axis_slaveid)
    while Hopper_z_encoder_reading > Hopper_z_axis_ground_position*0.80:
        print( ' waiting to open cone gripper - current encoder reading is ', Hopper_z_encoder_reading)
        Hopper_z_encoder_reading = Parameters.Read_Encoder_Data(Parameters.Hopper_Z_axis_slaveid)

    #Cone Gripper opening
    print( ' Cone Gripper opened ')
    #Parameters.Run_Motor_in_position_mode(Parameters.Hopper_gripper_slaveid,Parameters.Hopper_Planter_speed,Parameters.Hopper_Planter_acceleration,Parameters.Hopper_Planter_deacceleration,Cone_open_position) 
    
     
    #Hopper_moving_to_home_position
    print( ' Hopper_moving_to_home_position ')
    Parameters.Run_Motor_in_position_mode(Parameters.Hopper_Z_axis_slaveid,Parameters.Hopper_Z_Axis_speed,Parameters.Hopper_Z_Axis_acceleration,Parameters.Hopper_Z_Axis_deacceleration,Hopper_z_axis_home_position)
    Hopper_z_encoder_reading = Parameters.Read_Encoder_Data(Parameters.Hopper_Z_axis_slaveid)
    while Hopper_z_encoder_reading < Hopper_z_axis_ground_position*0.30:
        print( ' waiting to close cone gripper - current encoder reading is ', Hopper_z_encoder_reading)
        Hopper_z_encoder_reading = Parameters.Read_Encoder_Data(Parameters.Hopper_Z_axis_slaveid)
    
    #Cone Gripper Closing
    print( ' Cone_Gripper_closed ')
    #Parameters.Run_Motor_in_position_mode(Parameters.Hopper_gripper_slaveid,Parameters.Hopper_Planter_speed,Parameters.Hopper_Planter_acceleration,Parameters.Hopper_Planter_deacceleration,Cone_close_position)
    
    print( ' Press Entre for next hopping ')
    input()