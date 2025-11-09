import glob
import os
import shutil
import subprocess
import protocol
import pyautogui
import socket

def look_for_dir(location):
    files_list = glob.glob(location)
    return files_list


def delete(file_path):
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError as err:
        return False


def copy(original_file, new_file):
    try:
        shutil.copy(original_file, new_file)
    except FileNotFoundError as err:
        return False


def execute_program(program_path):
    subprocess_code = subprocess.run(program_path)
    if subprocess_code != 0 :
        return False
    else:
        pass


def take_screenshot():
    try:
        image = pyautogui.screenshot()
        image.save(r"screen.jpg")
    except Exception as err:
        print(err)
        return False

def send_screenshot():
    try:
        with open("screen.jpg", "r") as img_file:
            image_data = img_file.read()
        size = len(image_data)
        client_socket.send(str(size) + "#" + image_data.replace(" ", "#"))

    except Exception as err:
        return False
    finally:
        img_file.close()




def run():
    action, arguments = protocol.recv()

    if action == "execute_program":
        pass
    pass


def main():
    if take_screenshot() == False:
        print("failed")



if __name__ == "__main__":
    main()