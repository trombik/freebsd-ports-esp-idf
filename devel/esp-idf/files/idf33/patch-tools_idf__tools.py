--- tools/idf_tools.py.orig	2021-09-19 04:28:59 UTC
+++ tools/idf_tools.py
@@ -112,6 +112,8 @@ PLATFORM_FROM_NAME = {
     'osx': PLATFORM_MACOS,
     'darwin': PLATFORM_MACOS,
     'Darwin-x86_64': PLATFORM_MACOS,
+    # FreeBSD
+    'FreeBSD-amd64': PLATFORM_LINUX64,
     # Linux
     PLATFORM_LINUX64: PLATFORM_LINUX64,
     'linux64': PLATFORM_LINUX64,
