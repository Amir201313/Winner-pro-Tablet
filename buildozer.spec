[app]

# عنوان برنامه
title = Cornix Winner PRO

# نام پکیج و دامنه
package.name = cornixwinnerpro
package.domain = org.cornix

# فایل اصلی
source.dir = .

# پسوندهای مجاز برای گنجانده شدن در برنامه
source.include_exts = py,png,jpg,jpeg,ttf,TTF,json

# پوشه‌هایی که باید حتماً اضافه شوند (فونت‌ها و عکس‌ها)
source.include_patterns = fonts/*,image/*

# نسخه برنامه
version = 1.0.0

# پکیج‌ها و کتابخانه‌های مورد نیاز پایتون
requirements = python3,kivy==2.3.0,pillow,arabic-reshaper,python-bidi

# جهت صفحه (پشتیبانی از چرخش)
orientation = portrait,landscape

# آیکون و اسپلش (اختیاری)
# icon.filename = %(source.dir)s/image/bat.jpg

[buildozer]

# سطح لاگ
log_level = 2

# محل خروجی فایل‌ها
bin_dir = ./bin

# تنظیمات اندروید
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# دسترسی‌های اندروید مورد نیاز (وای‌فای، سوکت، حافظه)
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,READ_MEDIA_IMAGES
