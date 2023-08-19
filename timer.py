from pynput import keyboard
import time
import threading


def key_press(key):
    return False


def key_release(key):
    if key == keyboard.Key.space:
        return False


def start_timer():
    global timer_running

    with keyboard.Listener(on_release = key_release) as listener:
        listener.join()
    
    timer_running = True 
    return time.time()


def end_timer():
    global timer_running

    with keyboard.Listener(on_press = key_press) as listener:
        listener.join()
    
    timer_running = False


timer_running = True

def timer():
    start_time = start_timer()
    threading.Thread(target=end_timer).start()

    while timer_running:
        time .sleep(0.1) 
        print(f'\033[H\033[2J{time.time() - start_time:.2f}')
   

timer()     

# import threading
# import time
# from pynput import keyboard

# # Global variables
# start_time = None
# timer_running = False

# def start_timer():
#     global start_time, timer_running
#     start_time = time.time()
#     timer_running = True
#     print("Timer started.")

# def stop_timer():
#     global start_time, timer_running
#     elapsed_time = time.time() - start_time
#     timer_running = False
#     print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds")

# def on_key_press(key):
#     if timer_running:
#         stop_timer()

# def on_key_release(key):
#     if key == keyboard.Key.space:
#         start_timer()

# def key_listener():
#     with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
#         listener.join()

# # Start the key listener in a separate thread
# listener_thread = threading.Thread(target=key_listener)
# listener_thread.start()

# # Your main program can continue running here
# while True:
#     if timer_running:
#         current_time = time.time() - start_time
#         print(f"Timer running: {current_time:.2f} seconds")
#     else:
#         print("Press spacebar to start the timer.")

#     # You can put your main program logic here
