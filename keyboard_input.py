import subprocess
import time
import random
import string

def adb(cmd):
    subprocess.run(["adb"] + cmd, check=True)

def random_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

for i in range(100):
    print(f"[{i+1}/100] Launching Chrome...")
    adb(["shell", "am", "start", "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
    time.sleep(4)

    print("Tapping on address bar...")
    adb(["shell", "input", "tap", "540", "150"])
    time.sleep(1)

    test_string = random_text()
    print(f"Typing random string: {test_string}")
    adb(["shell", "input", "text", test_string])
    time.sleep(1)

    print("Clearing input field...")
    for _ in range(len(test_string)):
        adb(["shell", "input", "keyevent", "67"])  # KEYCODE_DEL
        time.sleep(0.1)

    time.sleep(1)
    print("Returning to home screen.")
    adb(["shell", "input", "keyevent", "3"])
    time.sleep(2)
