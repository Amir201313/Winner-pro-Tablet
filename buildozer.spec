[app]

# (str) Title of your application
title = Cornix Winner PRO

# (str) Package name
package.name = cornixwinnerpro

# (str) Package domain (needed for android/ios packaging)
package.domain = org.cornix

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,TTF,json

# (list) List of directory to include (let empty to include all the directories)
source.include_patterns = fonts/*,image/*

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,pillow,arabic-reshaper,python-bidi,pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = all

# (bool) Indicate whether the screen should stay on
android.wakelock = False

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup of app data
android.allow_backup = True

# (str) Format of release build (apk instead of aab)
android.release_artifact = apk

# (str) The python-for-android branch to use
p4a.branch = master

# (str) python-for-android git clone url
p4a.source_dir = 


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage
build_dir = ./.buildozer

# (str) Path to build output storage
bin_dir = ./bin
