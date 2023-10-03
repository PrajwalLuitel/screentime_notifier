# from plyer import notification
import time
import tkinter as tk
from tkinter import messagebox


def send_notification(title, message, time_duration):
    """
    This is the module that sends user notification to the device

    Arguments:
    title : String : The title of the notification
    message: String : Message content of the notification
    time_duration: Integer : The duration in minutes that the notification should be followed
    
    return: 
    none
    """
    messagebox.showinfo(title="Welcome user !", message=f"You will now be notified every {time_duration} minutes to take a rest from your screen")
    while True:
        time.sleep(120)
        time.sleep(time_duration*60) # interval calculated in seconds
        messagebox.showinfo(title, message)

        # notification.notify(
        #     title=title,
        #     message=message,
        #     app_name = "Screentime Notifier",
        #     timeout = 120
        # )
        


if __name__ == '__main__':
    # setting up the information in the notifier
    title = "Hello User"
    message = "I think you should take a couple of minutes rest, you've been on screen continuously. \n\n\tTake a 2 minutes break ! You deserve it !"

    # sending out notification
    send_notification(title, message, time_duration=30)

    root = tk.Tk()
    root.title("Dialog Box Example")

    button = tk.Button(root, text="Show Dialog", command=send_notification)
    button.pack()
    
    root.mainloop()