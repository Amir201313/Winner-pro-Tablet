[app]

# (str) Title of your application
title = Cornix Winner PRO

# (str) Package name
package.name = cornixwinnerpro

# (str) Package domain (needed for android/ios packaging)
package.domain = com.cornix

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,ttf,TTF,json,kv

# (list) List of directories to include (شامل پوشه‌های فونت و عکس)
source.include_patterns = fonts/*,image/*

# (str) Application versioning
version = 1.0.0

# (int) 0 for non-fullscreen (نوار وضعیت و دکمه‌های گوشی نمایش داده شوند)
fullscreen = 0

# (str) Supported orientation
orientation = all
android.manifest.orientation = fullSensor

# (list) Application requirements (کتابخانه‌های مورد نیاز پایتون)
requirements = python3,kivy,pillow,pyjnius,android,arabic-reshaper,python-bidi

# (str) Source main file
source.main = main.py

# در صورت وجود این فایل‌ها در مخزن، این خطوط فعال باشند:
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/Cornix.png

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,MANAGE_EXTERNAL_STORAGE

# (bool) Auto accept SDK license
android.accept_sdk_license = True

# (int) Target Android API
android.api = 33

# (int) Minimum API supported (21 برای سازگاری حداکثری توصیه می‌شود)
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API
android.ndk_api = 24

# (bool) Use public storage
android.private_storage = False

# (list) The Android archs to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support (اصلاح شده)
android.enable_androidx = True

# (str) The python-for-android branch to use
p4a.branch = master


[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (str) Path to build artifact storage
build_dir = ./.buildozer

# (str) Path to build output
bin_dir = ./bin
