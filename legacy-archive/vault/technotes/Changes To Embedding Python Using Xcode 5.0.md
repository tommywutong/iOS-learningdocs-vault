---
title: Changes To Embedding Python Using Xcode 5.0
apple_id: DTS40013920
resource_type: Technical Note
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: null
published: '2014-01-30'
source_url: https://developer.apple.com/library/archive/technotes/tn2328/_index.html
archived_at: '2026-07-26T19:54:11.102894Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2328

# Changes To Embedding Python Using Xcode 5.0

This document discusses some changes necessary to properly embed a Python interpreter using Xcode 5.0.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgojsgawugsbrfvke4vcbi4yq)[Embedding the Python Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgojsgawugsbrfvke4vcbi4za)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgojsgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Not only can new Python extensions, written in C/C++/Objective-C, be accessed from Python, but a Python interpreter can also be embedded in a C/C++/Objective-C program, so that the program can run Python code and access Python modules, extensions, etc.

__Note:__ When embedding any scripting language in an application designed to be long lived, it is recommended that rather than relying on a system-provided scripting language, a separate copy of the scripting language should be used and embedded inside the application bundle.  This prevents the application from being affected by changes to the system-provided scripting language, which could be updated or even removed during major system upgrades.

[Back to Top](#)

## Embedding the Python Framework

The [Python Documentation](http://docs.python.org/2.7/extending/embedding.html#compiling-and-linking-under-unix-like-systems) explains how to obtain the necessary compiler and linker flags (though in most cases, only the `-I, -L` and `-l` flags are really necessary).  This works for most Unix-like operating systems, including OS X.

In particular on OS X, Python is packaged in a framework bundle, so that all the Python modules, extensions and header files are in one location.  Multiple versions of Python can also be supported.  This also means that compiling and linking can be simplified when accessed via a framework:

Unix-like system:

- `#include <Python.h>`
- Add a `-I` flag to the complier with the path to the headers.
- To link, we add a `-L/-l` pair of options to link against the libpython2.x.dylib library.

As a framework:

- `#include <Python/Python.h>`
- Then we drag the Python.framework icon into the Xcode sidebar (or equivalently add Python.framework via __Link Binary With Libraries__ in __Build Phases__).

Because Python is a framework, it also resides in the SDK, even though Python (or any scripting language) has difficulties being in two places.  Due to both long-term and recent issues, it was decided to remove Python from the SDK.  This doesn’t affect any regular users or software developers that don’t specify an SDKROOT (either via the SDKROOT environment variable, the -sdk option on some tools, or the -isysroot/-syslibroot options to the compiler/linker).

But if you are using an SDKROOT and/or Xcode (which enforces an SDKROOT), the framework shortcuts will no longer work, so you must go back to using the Unix-like settings:

1) Replace

`#include <Python/Python.h>`

with

`#include <Python.h>`

2) Run (with the appropriate version number if not using 2.7) shown in Listing 1:

__Listing 1__  Getting compiler flags

```
% python2.7-config --cflags
-I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE
```

(the `-I` option is duplicated).  In Xcode, paste the path (without the leading `-I`) into the Header Search Paths setting of the Search Paths section of the Build Settings.  If not using Xcode, add the `-I` option with the path to the compiler flags.

3) Remove the Python.framework icon from the Xcode sidebar, or if not using Xcode, remove “-framework Python” from the linker flags.

4) Run (with the appropriate version number if not using 2.7) shown in Listing 2:

__Listing 2__  Getting linker flags

```
% python2.7-config --ldflags
-L/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config -ldl -framework CoreFoundation -lpython2.7
```

If using Xcode, open the path following the `-L` option in the Finder, and drag the libpython2.7.dylib icon into the Xcode sidebar.  Confirm the dialog box, and now Xcode is set to link against libpython2.7.dylib (by using the same `-L` and `-l` option settings as above).

If not using Xcode, add the `-L` option (with path) and second `-l` option from above to the linker flags.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-30 | Fixed invalid '-' character in Listing 1. |
| 2013-10-30 | New document that discusses how to embed the Python scripting language into your application. |

