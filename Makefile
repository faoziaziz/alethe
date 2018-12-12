init:
	sudo python -m pip install -r requirements.txt

jalan:
	python main.py

semua: init jalan
