# IoT-based-Fire-Alarm-System-using-Raspberry-Pi-Pico-W
Combining temperature, gas and smoke sensors with Pico W’s connectivity overcomes limitations of single-sensor alarms.​  
End-to-end automation (detection → computation → communication) accelerates emergency response and reduces human error.​  
The low-cost, modular design can be adapted for fire monitoring.

Connect DHT11/22 for temperature/humidity, MQ2 for combustible gases, and
four smoke sensors positioned for 360° coverage; include LEDs for power &
network status.​

Continuously sample sensors at fixed intervals; apply threshold comparisons and
cross-sensor validation logic to confirm genuine fire events and filter out false
positives.​

Upon multi-sensor alarm, compute fire-size score, compose a Telegram message
with sensor values, severity classification and truck-count recommendation.​

Use Pico W’s Wi-Fi to POST via Bot API while simultaneously triggering onboard
buzzer/LED for immediate local warning.​
