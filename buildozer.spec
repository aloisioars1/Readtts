
[app]
title = Aloisio TTS
package.name = aloisiotts
package.domain = com.aloisio.tts

source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy,gtts,android

orientation = portrait
fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.ant = auto

[buildozer]
log_level = 2
