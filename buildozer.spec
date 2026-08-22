[app]

# عنوان برنامه
title = Cornix Winner PRO

# نام بسته برنامه
package.name = cornixwinnerpro

# دامنه بسته (بدون کاراکتر خاص)
package.domain = org.cornix

# فایل اصلی اجرایی
source.dir = .

# پسوندهایی که باید در فایل APK گنجانده شوند (شامل عکس‌ها و فونت‌ها)
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,TTF,json

# الگوهای فایل‌هایی که باید نادیده گرفته شوند
source.exclude_patterns = license,Makefile,*.pyc,*.pyo,.git/*,.github/*,bin/*

# نسخه برنامه
version = 1.0.0

# پیش‌نیازهای پایتونی برنامه
requirements = python3,kivy==2.3.0,pillow,arabic-reshaper,python-bidi,pyjnius

# جهت صفحه (عمودی/افقی)
orientation = portrait,landscape

# تمام دسترسی‌های لازم برای ذخیره فایل، اسکرین‌شات و اشتراک‌گذاری
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,MANAGE_EXTERNAL_STORAGE

# اجازه دسترسی به حافظه به شیوه قدیمی برای اندروید 10 به بالا
android.request_legacy_external_storage = True

# مشخصات API اندروید
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# فعال‌سازی دسترسی‌های بک‌اند پایتون-فور-اندروید
android.allow_backup = True

# تنظیمات خروجی فایل
[buildozer]

# سطح لاگ (2 برای دیباگ کامل)
log_level = 2

# مسیر ذخیره بیلدها
bin_dir = ./bin
