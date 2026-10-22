import os
import subprocess

BASE = r"D:\IA\MCP\smart-projector-wallpapers"
ADB = r"C:\Users\ddudu\AppData\Local\Microsoft\WinGet\Packages\Google.PlatformTools_Microsoft.Winget.Source_8wekyb3d8bbwe\platform-tools\adb.exe"
IP = "192.168.101.187:5555"

count = 0
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith(".jpg") or f.endswith(".png"):
            local_path = os.path.join(root, f)
            remote_path = f"/sdcard/Android/data/com.omeda.arc/files/wallpapers/{f}"
            cmd = f'"{ADB}" -s {IP} push "{local_path}" "{remote_path}"'
            subprocess.run(cmd, shell=True, capture_output=True)
            count += 1
            print(f"[{count}] Pushed: {f}")

print(f"Total of {count} wallpapers pushed successfully to the projector!")
