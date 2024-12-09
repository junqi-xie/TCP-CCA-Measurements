delay1:
	sudo tc qdisc add dev enp39s0 root netem delay 20ms

delay2:
	sudo tc qdisc add dev enp39s0 root netem delay 40ms

delay3:
	sudo tc qdisc add dev enp39s0 root netem delay 60ms

delay4:
	sudo tc qdisc add dev enp39s0 root netem delay 80ms

loss1:
	sudo tc qdisc add dev enp39s0 root netem delay 20ms loss 0.005%

loss2:
	sudo tc qdisc add dev enp39s0 root netem delay 20ms loss 0.01%

reset:
	sudo tc qdisc del dev enp39s0 root