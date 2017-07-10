import webiopi

GPIO = webiopi.GPIO

def ServoAngle(iPinServo, iAngle):
    up = int(1500 + (iAngle * 350) / 45)
    down = 20000 - up
    GPIO.pulseMicro(iPinServo, up, down)

PIN_SERVO_x = 23
PIN_SERVO_y = 24

angle_x = 0
angle_y = 0


def setup():
    GPIO.setFunction(PIN_SERVO_x, GPIO.PWM)
    GPIO.setFunction(PIN_SERVO_y, GPIO.PWM)
    ServoAngle(PIN_SERVO_x, angle_x)
    ServoAngle(PIN_SERVO_y, angle_y)

def loop():
    webiopi.sleep(0.5)

@webiopi.macro
def defaultPosition():
    angle_x = 0
    angle_y = 0
    ServoAngle(PIN_SERVO_x,angle_x)
    ServoAngle(PIN_SERVO_y,angle_y)

@webiopi.macro
def up():
    global angle_x
    angle_x += -30
    if angle_x == -150:
        angle_x = -120
    ServoAngle(PIN_SERVO_x, angle_x)

@webiopi.macro
def down():
    global angle_x
    angle_x += 30
    if angle_x == 150:
        angle_x = 120
    ServoAngle(PIN_SERVO_x, angle_x)

@webiopi.macro
def right():
    global angle_y
    angle_y += -30
    if angle_y == -150:
        angle_y = -120
    ServoAngle(PIN_SERVO_y, angle_y)

@webiopi.macro
def left():
    global angle_y
    angle_y += 30
    if angle_y == 150:
        angle_y = 120
    ServoAngle(PIN_SERVO_y, angle_y)

