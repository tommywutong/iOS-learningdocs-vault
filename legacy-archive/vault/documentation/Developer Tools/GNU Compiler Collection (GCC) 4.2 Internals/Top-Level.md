---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Top-Level.html
archived_at: '2026-07-15T07:31:03.008352Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs),
Previous: [Configure Terms](Configure-Terms.md#apple-inxw4ztjm52xezjnkrsxe3lt),
Up: [Source Tree](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu)

---

### 6.2 Top Level Source Directory

The top level source directory in a GCC distribution contains several
files and directories that are shared with other software
distributions such as that of GNU Binutils. It also contains several
subdirectories that contain parts of GCC and its runtime libraries:

**`boehm-gc`**
: The Boehm conservative garbage collector, used as part of the Java
runtime library.

**`contrib`**
: Contributed scripts that may be found useful in conjunction with GCC.
One of these, `contrib/texi2pod.pl`, is used to generate man
pages from Texinfo manuals as part of the GCC build process.

**`fastjar`**
: An implementation of the `jar` command, used with the Java
front end.

**`gcc`**
: The main sources of GCC itself (except for runtime libraries),
including optimizers, support for different target architectures,
language front ends, and testsuites. See [The `gcc` Subdirectory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs), for details.

**`include`**
: Headers for the `libiberty` library.

**`libada`**
: The Ada runtime library.

**`libcpp`**
: The C preprocessor library.

**`libgfortran`**
: The Fortran runtime library.

**`libffi`**
: The `libffi` library, used as part of the Java runtime library.

**`libiberty`**
: The `libiberty` library, used for portability and for some
generally useful data structures and algorithms. See [Introduction](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/libiberty/index.html#Top), for more information
about this library.

**`libjava`**
: The Java runtime library.

**`libmudflap`**
: The `libmudflap` library, used for instrumenting pointer and array
dereferencing operations.

**`libobjc`**
: The Objective-C and Objective-C++ runtime library.

**`libstdc++-v3`**
: The C++ runtime library.

**`maintainer-scripts`**
: Scripts used by the `gccadmin` account on `gcc.gnu.org`.

**`zlib`**
: The `zlib` compression library, used by the Java front end and as
part of the Java runtime library.

The build system in the top level directory, including how recursion
into subdirectories works and how building runtime libraries for
multilibs is handled, is documented in a separate manual, included
with GNU Binutils. See [GNU configure and build system](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/configure/index.html#Top), for details.
