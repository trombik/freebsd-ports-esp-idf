--- tools/idf_tools.py.orig	2021-09-19 04:14:05 UTC
+++ tools/idf_tools.py
@@ -122,6 +122,8 @@ PLATFORM_FROM_NAME = {
     'Darwin-x86_64': PLATFORM_MACOS,
     # pretend it is x86_64 until Darwin-arm64 tool builds are available:
     'Darwin-arm64': PLATFORM_MACOS,
+    # pretend it is linux-amd64
+    'FreeBSD-amd64': PLATFORM_LINUX64,
     # Linux
     PLATFORM_LINUX64: PLATFORM_LINUX64,
     'linux64': PLATFORM_LINUX64,
