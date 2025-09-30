from flask import Flask, render_template, redirect, url_for
from pi_servo_hat import PiServoHat
import time

# Initialize Flask app
app = Flask(__name__)

# Create an instance of the PiServoHat class
servo_hat = PiServoHat()
servo_hat.restart()

# Define the servo channels
base_servo_channel = 0
lower_arm_servo_channel = 1
upper_arm_servo_channel = 2
gripper_servo_channel = 10

# Function to move the servos
def move_servo(channel, position):
    servo_hat.move_servo_position(channel, position - 90)
    time.sleep(1)  # Allow time for the movement
    print(f"Servo on channel {channel} moved to {position}.")

def stop_servo(channel):
    move_servo(channel, 140)  # Stop command
    print(f"Servo on channel {channel} stopped.")

# Flask route to control base servo
@app.route('/base_left')
def move_left_base():
    move_servo(base_servo_channel, 170)
    stop_servo(base_servo_channel)
    return redirect(url_for('index'))

@app.route('/base_right')
def move_right_base():
    move_servo(base_servo_channel, 120)
    stop_servo(base_servo_channel)
    return redirect(url_for('index'))

# Flask route to control lower arm servo
@app.route('/lower_arm_up')
def move_up_lower_arm():
    move_servo(lower_arm_servo_channel, 120)
    stop_servo(lower_arm_servo_channel)
    return redirect(url_for('index'))

@app.route('/lower_arm_down')
def move_down_lower_arm():
    move_servo(lower_arm_servo_channel, 170)
    stop_servo(lower_arm_servo_channel)
    return redirect(url_for('index'))

# Flask route to control upper arm servo
@app.route('/upper_arm_up')
def move_up_upper_arm():
    move_servo(upper_arm_servo_channel, 120)
    stop_servo(upper_arm_servo_channel)
    return redirect(url_for('index'))

@app.route('/upper_arm_down')
def move_down_upper_arm():
    move_servo(upper_arm_servo_channel, 170)
    stop_servo(upper_arm_servo_channel)
    return redirect(url_for('index'))

# Flask route to control gripper
@app.route('/gripper_open')
def open_gripper():
    move_servo(gripper_servo_channel, 200)
    return redirect(url_for('index'))

@app.route('/gripper_close')
def close_gripper():
    move_servo(gripper_servo_channel, 170)
    return redirect(url_for('index'))

# Main Flask route to render the control interface
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
