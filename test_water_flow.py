from water_flow import water_column_height

from water_flow import pressure_loss_from_pipe_reduction

from water_flow import reynolds_number

from water_flow import pressure_loss_from_fittings

from water_flow import pressure_gain_from_water_height

from water_flow import pressure_loss_from_pipe

from pytest import approx
import pytest



def test_water_column_height():
  assert water_column_height(0, 0) == approx(0)
  assert water_column_height(0, 10) == approx(7.5)
  assert water_column_height(25, 0) == approx(25)
  assert water_column_height(48.3, 12.8) == approx(57.9)


def test_pressue_gain_from_water_height():
  assert pressure_gain_from_water_height(0) == approx(0)
  assert pressure_gain_from_water_height(30.2) == approx(295.628, rel = 0.001)
  assert pressure_gain_from_water_height(50) == approx(489.450, rel = 0.001)



def test_pressure_loss_from_pipe():
  assert pressure_loss_from_pipe(0.048692,	0,	0.018,	1.75) == approx(0, rel = 0.001)
  
  assert pressure_loss_from_pipe(0.048692,	200,	0,	1.75) == approx(0, rel = 0.001)
  
  assert pressure_loss_from_pipe(0.048692,	200,	0.018, 0) == approx(0, rel = 0.001)
  
  assert pressure_loss_from_pipe(0.048692,	200,	0.018,	1.75) == approx(-113.008, rel = 0.001)
  assert pressure_loss_from_pipe(0.048692,	200,	0.018,	1.65) == approx(-100.462, rel = 0.001)
  assert pressure_loss_from_pipe(0.28687,	1000,	0.013,	1.65) == approx(-61.576, rel = 0.001)
  assert pressure_loss_from_pipe(0.28687,	1800.75,	0.013,	1.65) == approx(-110.884, rel = 0.001)



def test_pressure_loss_from_fittings():
  assert pressure_loss_from_fittings(0, 3) == approx(0, rel = 0.001)
  assert pressure_loss_from_fittings(1.65, 0) == approx(0, rel = 0.001)
  assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, rel = 0.01)
  assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, rel = 0.01)
  assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, rel = 0.001)





def test_reynolds_number():
  assert reynolds_number(0.048692, 0) == approx(0, rel = 1)
  assert reynolds_number(0.048692, 1.65) == approx(80069, rel = 1)
  assert reynolds_number(0.048692, 1.75) == approx(84922, rel = 1)
  assert reynolds_number(0.28687, 1.65) == approx(471729, rel = 1)
  assert reynolds_number(0.28687, 1.75) == approx(500318, rel = 1)




def test_pressure_loss_from_pipe_reduction():
  assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, rel = 0.001)
  assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, rel = 0.001)
  assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, rel = 0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()

  
  
                                               

