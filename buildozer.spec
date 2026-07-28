[app]
title = My Pygame Clicker
package.name = pygameclicker
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,ttf

version = 0.1

# ВОТ ЗДЕСЬ МАГИЯ: заставляем собирать именно Pygame!
requirements = python3,pygame

orientation = portrait
fullscreen = 1

android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
