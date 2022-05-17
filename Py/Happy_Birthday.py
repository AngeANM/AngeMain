import threading
import time
bday='''

  _    _                           __  ___ _______ _    _ 
 | |  | |                         /_ |/ _ \__   __| |  | |
 | |__| | __ _ _ __  _ __  _   _   | | (_) | | |  | |__| |
 |  __  |/ _` | '_ \| '_ \| | | |  | |> _ <  | |  |  __  |
 | |  | | (_| | |_) | |_) | |_| |  | | (_) | | |  | |  | |
 |_|  |_|\__,_| .__/| .__/ \__, |  |_|\___/  |_|  |_|  |_|
              | |   | |     __/ |                         
              |_|   |_|    |___/    

  ____  _      _   _         _             
 |  _ \(_)    | | | |       | |            
 | |_) |_ _ __| |_| |__   __| | __ _ _   _ 
 |  _ <| | '__| __| '_ \ / _` |/ _` | | | |
 | |_) | | |  | |_| | | | (_| | (_| | |_| |
 |____/|_|_|   \__|_| |_|\__,_|\__,_|\__, |
                                      __/ |
                                     |___/ 
                                                     
  _______         __  __ ______ 
 |__   __|       |  \/  |  ____|
    | | ___      | \  / | |__   
    | |/ _ \     | |\/| |  __|  
    | | (_) |    | |  | | |____ 
    |_|\___/     |_|  |_|______|
                                
  _____                 _                      _   _                                              _____                _             
 |  __ \               | |                    | | | |                   /\                       / ____|              (-)            
 | |  | | _____   _____| | ___  _ __   ___  __| | | |__  _   _         /  \   _ __   __ _  ___  | |     __ _ _ __  ___ __ _ __  ___  
 | |  | |/ _ \ \ / / _ \ |/ _ \| '_ \ / _ \/ _` | | '_ \| | | |       / /\ \ | '_ \ / _` |/ _ \ | |    / _` | '_ \/ __| | '_ \ / _ \ 
 | |__| |  __/\ V /  __/ | (_) | |_) |  __/ (_| | | |_) | |_| |      / ____ \| | | | (_| |  __/ | |___| (_| | | | \__ \ | | | | (_) |
 |_____/ \___| \_/ \___|_|\___/| .__/ \___|\__,_| |_.__/ \__, |     /_/    \_\_| |_|\__, |\___|  \_____\__,_|_| |_|___/_|_| |_|\___/ 
                               | |                        __/ |                      __/ |                                           
                               |_|                       |___/                      |___/                                            

                                                                                                                         
                                                                                                                                                                    
                                                                                                                                                                    
'''
def task1():
	for letter in bday:
		time.sleep(0.01)
		print(letter, end='')

def task2():
 playsound('HappyBirthday.mp3')

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

# starting threads
t1.start()
t2.start()