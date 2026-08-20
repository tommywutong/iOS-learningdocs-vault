---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Header-Dirs.html
archived_at: '2026-07-15T07:31:00.018716Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny),
Previous: [Collect2](Collect2.md#apple-inxwy3dfmn2de),
Up: [Top](index.md#apple-krxxa)

---

## 17 Standard Header File Directories

`GCC_INCLUDE_DIR` means the same thing for native and cross. It is
where GCC stores its private include files, and also where GCC
stores the fixed include files. A cross compiled GCC runs
`fixincludes` on the header files in `$(tooldir)/include`.
(If the cross compilation header files need to be fixed, they must be
installed before GCC is built. If the cross compilation header files
are already suitable for GCC, nothing special need be done).

`GPLUSPLUS_INCLUDE_DIR` means the same thing for native and cross. It
is where `g++` looks first for header files. The C++ library
installs only target independent header files in that directory.

`LOCAL_INCLUDE_DIR` is used only by native compilers. GCC
doesn't install anything there. It is normally
`/usr/local/include`. This is where local additions to a packaged
system should place header files.

`CROSS_INCLUDE_DIR` is used only by cross compilers. GCC
doesn't install anything there.

`TOOL_INCLUDE_DIR` is used for both native and cross compilers. It
is the place for other packages to install header files that GCC will
use. For a cross-compiler, this is the equivalent of
`/usr/include`. When you build a cross-compiler,
`fixincludes` processes any header files in this directory.
