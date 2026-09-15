#Proje#
import codecs
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
# DOSYA YOLLARI
distance_time = r''
velocity_time = r''
acceleration_time = r''
#Distance#
distance_graph = codecs.open(distance_time, mode='r', encoding="utf-8", errors="ignore")
df_distance = pd.read_csv(distance_graph)
df_distance_graph = (df_distance)
cols = df_distance.columns.tolist()
time = df_distance[cols[0]].values
distance = df_distance[cols[1]].values
fig, ax = plt.subplots()
distance_line, = ax.plot(time, distance, "w-", label='distance(m)')
def update(num, time, distance, distance_line):
  distance_line.set_data(time[:num], distance[:float])
  ax.set_xlabel("time: " + str(time[num]) + "" + "distance: " + str(distance[float]))
  return distance_line
ani_d = animation.FuncAnimation(fig, update, frames=len(time), fargs=[time, distance, distance_line], interval=len(time)*10)
plt.tick_params(
axis='x', # degisiklikleri yapacagimiz eksen
which='both', # hem ana hem de ikincil cizgiler etkilenir
bottom=False, # alt kenar cizgilerini kapatir
top=False, # ust kenar cizgilerini kapatir
labelbottom=False # alt etiketi kapatir
)
ax.set_ylabel('time')
plt.legend(fancybox=True, loc='upper left')
ax.set_facecolor('k')
plt.show()
#Velocity#
velocity_graph = codecs.open(velocity_time, mode='r', encoding="utf-8", errors="ignore" )
df_velocity = pd.read_csv(velocity_graph)
df_velocity_graph = (df_velocity)
cols = df_velocity.columns.tolist()
time = df_velocity[cols[0]].values
velocity= df_velocity[cols[1]].values
fig, ax = plt.subplots()
velocity_line, = ax.plot(time, velocity, "w-", label='velocity(m/s)')
def update(num, time, velocity, velocity_line):
  velocity_line.set_data(time[:num], velocity[:float])
  ax.set_xlabel("time: " + str(time[num]) + "" + "velocity: " + str(velocity[float]))
  return velocity_line
ani_v = animation.FuncAnimation(fig, update, frames=len(time), fargs=[time, velocity, velocity_line], interval=len(time)*10)
plt.tick_params(
axis='x', 
which='both', 
bottom=False, 
top=False, 
labelbottom=False 
)
ax.set_ylabel('time')
plt.legend(fancybox=True, loc='upper left')
ax.set_facecolor('k')
plt.show()
#Acceleration#
acceleration_graph = codecs.open(acceleration_time, mode='r', encoding="utf-8", errors="ignore" )
df_acceleration = pd.read_csv(acceleration_graph)
df_acceleration_graph = (df_acceleration)
cols = df_acceleration.columns.tolist()
time = df_acceleration[cols[0]].values
acceleration = df_acceleration[cols[1]].values
fig, ax = plt.subplots()
acceleration_line, = ax.plot(time, velocity, "w-", label='acceleration(m/s^2)')
def update(num, time, acceleration, acceleration_line):
  acceleration_line.set_data(time[:num], acceleration[:float])
  ax.set_xlabel("time: " + str(time[num]) + "" + "acceleration: " + str(acceleration[float]))
  return acceleration_line
ani_a= animation.FuncAnimation(fig, update, frames=len(time), fargs=[time, acceleration, acceleration_line], interval=len(time)*10)
plt.tick_params(
axis='x', 
which='both', 
bottom=False, 
top=False, 
labelbottom=False 
)
ax.set_ylabel('time')
plt.legend(fancybox=True, loc='upper left')
ax.set_facecolor('k')
plt.show()
