
[app]
title = Aloisio TTS
package.name = aloisio_tts
package.domain = com.aloisio.tts

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,gtts
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# Android specifics
[app]
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
# deixa o bin/ na raiz
