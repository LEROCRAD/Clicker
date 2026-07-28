[app]
title = Pygame Clicker
package.name = pygameclicker
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,ttf

version = 0.1

requirements = python3,pygame

orientation = portrait
fullscreen = 1

android.archs = arm64-v8a

# Фиксируем API и версии инструментов
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 33.0.2

# Автопринятие лицензий
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
