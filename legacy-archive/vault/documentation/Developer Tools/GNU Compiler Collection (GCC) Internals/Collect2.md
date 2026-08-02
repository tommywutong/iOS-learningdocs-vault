---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Collect2.html
archived_at: '2026-07-15T07:30:59.381363Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Header Dirs](Header-Dirs.md#apple-jbswczdfoiwui2lsom),
Previous: [Fragments](Fragments.md#apple-izzgcz3nmvxhi4y),
Up: [Top](index.md#apple-krxxa)

---

## 16 `collect2`

GCC uses a utility called `collect2` on nearly all systems to arrange
to call various initialization functions at start time.

The program `collect2` works by linking the program once and
looking through the linker output file for symbols with particular names
indicating they are constructor functions. If it finds any, it
creates a new temporary ``.c`' file containing a table of them,
compiles it, and links the program a second time including that file.

The actual calls to the constructors are carried out by a subroutine
called `__main`, which is called (automatically) at the beginning
of the body of `main` (provided `main` was compiled with GNU
CC). Calling `__main` is necessary, even when compiling C code, to
allow linking C and C++ object code together. (If you use
`-nostdlib`, you get an unresolved reference to `__main`,
since it's defined in the standard GCC library. Include `-lgcc` at
the end of your compiler command line to resolve this reference.)

The program `collect2` is installed as `ld` in the directory
where the passes of the compiler are installed. When `collect2`
needs to find the _real_ `ld`, it tries the following file
names:

- `real-ld` in the directories listed in the compiler's search
  directories.
- `real-ld` in the directories listed in the environment variable
  `PATH`.
- The file specified in the `REAL_LD_FILE_NAME` configuration macro,
  if specified.
- `ld` in the compiler's search directories, except that
  `collect2` will not execute itself recursively.
- `ld` in `PATH`.

“The compiler's search directories” means all the directories where
`gcc` searches for passes of the compiler. This includes
directories that you specify with `-B`.

Cross-compilers search a little differently:

- `real-ld` in the compiler's search directories.
- `target-real-ld` in `PATH`.
- The file specified in the `REAL_LD_FILE_NAME` configuration macro,
  if specified.
- `ld` in the compiler's search directories.
- `target-ld` in `PATH`.

`collect2` explicitly avoids running `ld` using the file name
under which `collect2` itself was invoked. In fact, it remembers
up a list of such names—in case one copy of `collect2` finds
another copy (or version) of `collect2` installed as `ld` in a
second place in the search path.

`collect2` searches for the utilities `nm` and `strip`
using the same algorithm as above for `ld`.
