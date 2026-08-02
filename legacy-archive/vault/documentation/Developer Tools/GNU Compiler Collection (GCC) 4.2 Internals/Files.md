---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Files.html
archived_at: '2026-07-15T07:31:01.852254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [GGC Roots](GGC-Roots.md#apple-i5duglksn5xxi4y),
Up: [Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny)

---

### 20.3 Source Files Containing Type Information

Whenever you add `GTY` markers to a source file that previously
had none, or create a new source file containing `GTY` markers,
there are three things you need to do:

1. You need to add the file to the list of source files the type
   machinery scans. There are four cases:
   1. For a back-end file, this is usually done
      automatically; if not, you should add it to `target_gtfiles` in
      the appropriate port's entries in `config.gcc`.
   2. For files shared by all front ends, add the filename to the
      `GTFILES` variable in `Makefile.in`.
   3. For files that are part of one front end, add the filename to the
      `gtfiles` variable defined in the appropriate
      `config-lang.in`. For C, the file is `c-config-lang.in`.
   4. For files that are part of some but not all front ends, add the
      filename to the `gtfiles` variable of _all_ the front ends
      that use it.
2. If the file was a header file, you'll need to check that it's included
   in the right place to be visible to the generated files. For a back-end
   header file, this should be done automatically. For a front-end header
   file, it needs to be included by the same file that includes
   `gtype-lang.h`. For other header files, it needs to be
   included in `gtype-desc.c`, which is a generated file, so add it to
   `ifiles` in `open_base_file` in `gengtype.c`.

   For source files that aren't header files, the machinery will generate a
   header file that should be included in the source file you just changed.
   The file will be called `gt-path.h` where path is the
   pathname relative to the `gcc` directory with slashes replaced by
   -, so for example the header file to be included in
   `cp/parser.c` is called `gt-cp-parser.c`. The
   generated header file should be included after everything else in the
   source file. Don't forget to mention this file as a dependency in the
   `Makefile`!

For language frontends, there is another file that needs to be included
somewhere. It will be called `gtype-lang.h`, where
lang is the name of the subdirectory the language is contained in.
