---
title: Compiling X11 / OpenGL applications on Mac OS X  v.10.5 Leopard
apple_id: DTS10004518
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2007-10-30'
source_url: https://developer.apple.com/library/archive/qa/qa1567/_index.html
archived_at: '2026-07-18T02:32:18.564259Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1567

# Compiling X11 / OpenGL applications on Mac OS X v.10.5 Leopard

## Q:  At compile time I am getting "ld: cycle in dylib re-exports with `/usr/X11R6/lib/libGL.dylib`" How can I properly build my application?

A: While building X11 / OpenGL applications like this:


```
gcc glxgears.c -o glxgears -I/usr/X11R6/include -L/usr/X11R6/lib -lGL -lX11
```

Some developers might experience the following error:


```
ld: cycle in dylib re-exports with /usr/X11R6/lib/libGL.dylib
collect2: ld returned 1 exit status
```


The linker on Mac OS X v.10.5 searches -L paths for indirect libraries and in doing so it finds two copies of `libGL.dylib`. One in /usr/X11/lib and the other in `/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries` and this causes a cycle.

This is a side effect of various linker improvements in Leopard, which we may be able to mitigate in a future release.

You can overcome this problem by providing the `-dylib_file` option to the linker. The `-dylib_file` option is described as:


```
-dylib_file install_name:file_name
   Specifies that a dynamic shared library is in a different location than its standard location.
   Use this option when you link with a library that is dependent on a dynamic library, and the
   dynamic library is in a location other than its default location. install_name specifies the path
   where the library normally resides. file_name specifies the path of the library you want to use
   instead. For example, if you link to a library that depends upon the dynamic library libsys
   and you have libsys installed in a nondefault location, you would use this option:
   -dylib_file /lib/libsys_s.A.dylib:/me/lib/libsys_s.A.dylib.
```

For this specific issue the -dyld_file option should be used like this:


```
-dylib_file \
/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib:\
/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib
```

A full compile line for an application might look like this:


```
gcc glxgears.c -o glxgears -I/usr/X11R6/include -L/usr/X11R6/lib -lGL -lX11 -dylib_file \
/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib:\
/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-10-30 | New document that trying to compile X11 / OpenGL application on Mac OS X v.10.5 result on "ld: cycle in dylib re-exports with /usr/X11R6/lib/libGL.dylib"" |

