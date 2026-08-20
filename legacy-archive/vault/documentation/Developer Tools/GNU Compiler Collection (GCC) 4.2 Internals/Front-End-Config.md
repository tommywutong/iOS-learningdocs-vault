---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Front-End-Config.html
archived_at: '2026-07-15T07:31:01.910436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Front End Directory](Front-End-Directory.md#apple-izzg63tufvcw4zbniruxezldorxxe6i),
Up: [Front End](Front-End.md#apple-izzg63tufvcw4za)

---

##### 6.3.8.2 The Front End `config-lang.in` File

Each language subdirectory contains a `config-lang.in` file. In
addition the main directory contains `c-config-lang.in`, which
contains limited information for the C language. This file is a shell
script that may define some variables describing the language:

**`language`**
: This definition must be present, and gives the name of the language
for some purposes such as arguments to `--enable-languages`.

**`lang_requires`**
: If defined, this variable lists (space-separated) language front ends
other than C that this front end requires to be enabled (with the
names given being their `language` settings). For example, the
Java front end depends on the C++ front end, so sets
``lang_requires=c++`'.

**`subdir_requires`**
: If defined, this variable lists (space-separated) front end directories
other than C that this front end requires to be present. For example,
the Objective-C++ front end uses source files from the C++ and
Objective-C front ends, so sets ``subdir_requires="cp objc"`'.

**`target_libs`**
: If defined, this variable lists (space-separated) targets in the top
level `Makefile` to build the runtime libraries for this
language, such as `target-libobjc`.

**`lang_dirs`**
: If defined, this variable lists (space-separated) top level
directories (parallel to `gcc`), apart from the runtime libraries,
that should not be configured if this front end is not built.

**`build_by_default`**
: If defined to ``no`', this language front end is not built unless
enabled in a `--enable-languages` argument. Otherwise, front
ends are built by default, subject to any special logic in
`configure.ac` (as is present to disable the Ada front end if the
Ada compiler is not already installed).

**`boot_language`**
: If defined to ``yes`', this front end is built in stage 1 of the
bootstrap. This is only relevant to front ends written in their own
languages.

**`compilers`**
: If defined, a space-separated list of compiler executables that will
be run by the driver. The names here will each end
with ``\$(exeext)`'.

**`stagestuff`**
: If defined, a space-separated list of files that should be moved to
the `stagen` directories in each stage of bootstrap.

**`outputs`**
: If defined, a space-separated list of files that should be generated
by `configure` substituting values in them. This mechanism can
be used to create a file `language/Makefile` from
`language/Makefile.in`, but this is deprecated, building
everything from the single `gcc/Makefile` is preferred.

**`gtfiles`**
: If defined, a space-separated list of files that should be scanned by
gengtype.c to generate the garbage collection tables and routines for
this language. This excludes the files that are common to all front
ends. See [Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny).

**`need_gmp`**
: If defined to ``yes`', this frontend requires the GMP library.
Enables configure tests for GMP, which set `GMPLIBS` and
`GMPINC` appropriately.
