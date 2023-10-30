pressure = 998.2
gravity = 9.80665
water_vecocity = 0.0010016

def water_column_height(tower_height, tank_height):
    height = tower_height + (3*tank_height)/4
    return height


def pressure_gain_from_water_height(height):
  
  pressure_gain = (pressure * gravity  * height)/1000
  return pressure_gain



def pressure_loss_from_pipe(pipe_diameter,
  pipe_length, friction_factor, fluid_velocity):
  
  pressure_loss = -(friction_factor * pressure * pipe_length * fluid_velocity*fluid_velocity) /(2000 * pipe_diameter)
  return pressure_loss



def pressure_loss_from_fittings(
  fluid_velocity, quantity_fittings):
  
  pressure_loss_fittings = -0.04 * pressure * fluid_velocity * fluid_velocity  * quantity_fittings/2000
  
  return pressure_loss_fittings

p = pressure_loss_from_fittings(0 , 3)
q = pressure_loss_from_fittings(1.65 , 0)
r = pressure_loss_from_fittings(1.65 , 2)
s = pressure_loss_from_fittings(1.75 , 2)
t = pressure_loss_from_fittings(1.75 , 5)
print(p)
print(q)
print(r)
print(s)
print(t)


def reynolds_number(hydraulic_diameter, fluid_velocity):
  
  reynolds = pressure * hydraulic_diameter * fluid_velocity / water_vecocity
  return reynolds




def pressure_loss_from_pipe_reduction(larger_diameter,
  fluid_velocity, reynolds_number, smaller_diameter):
  
  constant_k = (0.1+50/reynolds_number)* ((larger_diameter/smaller_diameter)**4 -1)
  pipe_reduction = -(constant_k * pressure * fluid_velocity * fluid_velocity) /2000
  return pipe_reduction


