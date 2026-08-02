---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Subdirectories.html
archived_at: '2026-07-15T07:31:00.846165Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Configuration](Configuration.md#apple-inxw4ztjm52xeylunfxw4),
Up: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)

---

#### 6.3.1 Subdirectories of `gcc`

The `gcc` directory contains the following subdirectories:

**`language`**
: Subdirectories for various languages. Directories containing a file
`config-lang.in` are language subdirectories. The contents of
the subdirectories `cp` (for C++), `objc` (for Objective-C)
and `objcp` (for Objective-C++) are documented in this manual
(see [Passes and Files of the Compiler](Passes.md#apple-kbqxg43fom)); those for other
languages are not. See [Anatomy of a Language Front End](Front-End.md#apple-izzg63tufvcw4za),
for details of the files in these directories.

**`config`**
: Configuration files for supported architectures and operating
systems. See [Anatomy of a Target Back End](Back-End.md#apple-ijqwg2znivxgi), for
details of the files in this directory.

**`doc`**
: Texinfo documentation for GCC, together with automatically generated
man pages and support for converting the installation manual to
HTML. See [Documentation](Documentation.md#apple-irxwg5lnmvxhiylunfxw4).

**`fixinc`**
: The support for fixing system headers to work with GCC. See
`fixinc/README` for more information. The headers fixed by this
mechanism are installed in `libsubdir/include`. Along with
those headers, `README-fixinc` is also installed, as
`libsubdir/include/README`.

**`ginclude`**
: System headers installed by GCC, mainly those required by the C
standard of freestanding implementations. See [Headers Installed by GCC](Headers.md#apple-jbswczdfojzq), for details of when these and other headers are
installed.

**`intl`**
: GNU `libintl`, from GNU `gettext`, for systems which do not
include it in libc. Properly, this directory should be at top level,
parallel to the `gcc` directory.

**`po`**
: Message catalogs with translations of messages produced by GCC into
various languages, `language.po`. This directory also
contains `gcc.pot`, the template for these message catalogues,
`exgettext`, a wrapper around `gettext` to extract the
messages from the GCC sources and create `gcc.pot`, which is run
by ``make gcc.pot`', and `EXCLUDES`, a list of files from
which messages should not be extracted.

**`testsuite`**
: The GCC testsuites (except for those for runtime libraries).
See [Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt).
