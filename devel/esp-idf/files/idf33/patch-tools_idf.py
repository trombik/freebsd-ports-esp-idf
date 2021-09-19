--- tools/idf.py.orig	2021-09-19 04:31:06 UTC
+++ tools/idf.py
@@ -59,7 +59,7 @@ elif os.name == 'nt':  # other Windows
     MAKE_CMD = "mingw32-make"
     MAKE_GENERATOR = "MinGW Makefiles"
 else:
-    MAKE_CMD = "make"
+    MAKE_CMD = "gmake"
     MAKE_GENERATOR = "Unix Makefiles"
 
 GENERATORS = \
