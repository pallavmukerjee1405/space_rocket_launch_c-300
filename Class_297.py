from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
#Set the Hostname, Port & TopicName

broker='broker.emqx.io'
port=1883
topic='topicName/iot'




client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client
#Define the first page of the web application

@app.route('/')
def index():
	return render_template('index.html')

#Define the button page of the web application
@app.route('/main', methods=['POST'])
def main():
	return render_template('main.html')

#Define the Release Orbital Arm button and connect with MQTT server
@app.route('/1', methods=['POST'])
def release():
	release_test()
	return render_template('1.html')
	send_release_data(client)

def release_test():
	client=connect_mqtt()
	client.loop_start()

#Define the Main Engine Test button and connect with MQTT server
@app.route('/2', methods=['POST'])
def engine():
	engine_test()
	return render_template('2.html')
	send_engine_data(client)

def engine_test():
	client=connect_mqtt()
	client.loop_start()

#Define the Activate Hydrogen button and connect with MQTT server
@app.route('/3', methods=['POST'])
def activate():
	activate_test()
	return render_template('3.html')
	send_activate_data(client)

def activate_test():
	client=connect_mqtt()
	client.loop_start()

#Define the Main Engine Ignite button and connect with MQTT server
@app.route('/4', methods=['POST'])
def ignite():
	ignite_test()
	return render_template('4.html')
	send_ignite_data(client)

def ignite_test():
	client=connect_mqtt()
	client.loop_start()

#Define the Hydrogen Vent Arm button and connect with MQTT server
@app.route('/5', methods=['POST'])
def hydrogen():
	hydrogen_test()
	return render_template('5.html')
	send_vent_data(client)

def hydrogen_test():
	client=connect_mqtt()
	client.loop_start()

#Define the Ignite both SRB's button and connect with MQTT server
@app.route('/6', methods=['POST'])
def srb():
	srb_test()
	return render_template('6.html')
	send_srb_data(client)

def srb_test():
	client=connect_mqtt()
	client.loop_start()

def send_release_data(client):
	msg='1'
	result=client.publish(topic,msg)
	status=result[0]
	if status == 0:
		print("Send '{msg}' to topic '{topic}'")

def send_engine_data(client):
	msg='2'
	result=client.publish(topic,msg)
	status=result[0]
	if status == 0:
		print("Send '{msg}' to topic '{topic}'")

def send_activate_data(client):
	msg='3'
	result=client.publish(topic,msg)
	status=result[0]
	if status == 0:
		print("Send '{msg}' to topic '{topic}'")

def send_ignite_data(client):
	msg='4'
	result=client.publish(topic,msg)
	status=result[0]
	if status == 0:
		print("Send '{msg}' to topic '{topic}'")

def send_vent_data(client):
	msg='5'
	result=client.publish(topic,msg)
	status=result[0]
	if status == 0:
		print("Send '{msg}' to topic '{topic}'")

def send_srb_data(client):
	msg='6'
	result=client.publish(topic,msg)
	status=result[0]
	if status == 0:
		print("Send '{msg}' to topic '{topic}'")

if __name__ == "__main__":
    app.run(port=5001)





