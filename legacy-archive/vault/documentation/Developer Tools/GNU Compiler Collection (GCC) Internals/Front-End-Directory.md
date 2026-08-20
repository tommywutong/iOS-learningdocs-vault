---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Front-End-Directory.html
archived_at: '2026-07-15T07:30:59.921556Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Front End Config](Front-End-Config.md#apple-izzg63tufvcw4zbninxw4ztjm4),
Up: [Front End](Front-End.md#apple-izzg63tufvcw4za)

---

##### 6.3.8.1 The Front End `language` Directory

A front end `language` directory contains the source files
of that front end (but not of any runtime libraries, which should be
outside the `gcc` directory). This includes documentation, and
possibly some subsidiary programs build alongside the front end.
Certain files are special and other parts of the compiler depend on
their names:

**`config-lang.in`**
: This file is required in all language subdirectories. See [The Front End `config-lang.in` File](Front-End-Config.md#apple-izzg63tufvcw4zbninxw4ztjm4), for details of
its contents

**`Make-lang.in`**
: This file is required in all language subdirectories. It contains
targets lang`.`hook (where lang is the
setting of `language` in `config-lang.in`) for the following
values of hook, and any other Makefile rules required to
build those targets (which may if necessary use other Makefiles
specified in `outputs` in `config-lang.in`, although this is
deprecated). Some hooks are defined by using a double-colon rule for
hook, rather than by using a target of form
lang`.`hook. These hooks are called “double-colon
hooks” below. It also adds any testsuite targets that can use the
standard rule in `gcc/Makefile.in` to the variable
`lang_checks`.

**`all.build`

**`all.cross`

**`start.encap`

**`rest.encap`********
: FIXME: exactly what goes in each of these targets?

**`tags`**
: Build an `etags` `TAGS` file in the language subdirectory
in the source tree.

**`info`**
: Build info documentation for the front end, in the build directory.
This target is only called by ``make bootstrap`' if a suitable
version of `makeinfo` is available, so does not need to check
for this, and should fail if an error occurs.

**`dvi`**
: Build DVI documentation for the front end, in the build directory.
This should be done using `$(TEXI2DVI)`, with appropriate
`-I` arguments pointing to directories of included files.
This hook is a double-colon hook.

**`html`**
: Build HTML documentation for the front end, in the build directory.

**`man`**
: Build generated man pages for the front end from Texinfo manuals
(see [Man Page Generation](Man-Page-Generation.md#apple-jvqw4lkqmftwklkhmvxgk4tboruw63q)), in the build directory. This target
is only called if the necessary tools are available, but should ignore
errors so as not to stop the build if errors occur; man pages are
optional and the tools involved may be installed in a broken way.

**`install-normal`**
: FIXME: what is this target for?

**`install-common`**
: Install everything that is part of the front end, apart from the
compiler executables listed in `compilers` in
`config-lang.in`.

**`install-info`**
: Install info documentation for the front end, if it is present in the
source directory. This target should have dependencies on info files
that should be installed. This hook is a double-colon hook.

**`install-man`**
: Install man pages for the front end. This target should ignore
errors.

**`srcextra`**
: Copies its dependencies into the source directory. This generally should
be used for generated files such as Bison output files which are not
present in CVS, but should be included in any release tarballs. This
target will be executed during a bootstrap if
``--enable-generated-files-in-srcdir`' was specified as a
`configure` option.

**`srcinfo`

**`srcman`****
: Copies its dependencies into the source directory. These targets will be
executed during a bootstrap if ``--enable-generated-files-in-srcdir`'
was specified as a `configure` option.

**`uninstall`**
: Uninstall files installed by installing the compiler. This is
currently documented not to be supported, so the hook need not do
anything.

**`mostlyclean`

**`clean`

**`distclean`

**`maintainer-clean`********
: The language parts of the standard GNU
``*clean`' targets. See [Standard Targets for Users](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/standards/Standard-Targets.html#Standard-Targets), for details of the standard
targets. For GCC, `maintainer-clean` should delete
all generated files in the source directory that are not checked into
CVS, but should not delete anything checked into CVS.

**`stage1`

**`stage2`

**`stage3`

**`stage4`

**`stageprofile`

**`stagefeedback`************
: Move to the stage directory files not included in `stagestuff` in
`config-lang.in` or otherwise moved by the main `Makefile`.

**`lang.opt`**
: This file registers the set of switches that the front end accepts on
the command line, and their `--help` text. The file format is
documented in the file `c.opt`. These files are processed by the
script `opts.sh`.

**`lang-specs.h`**
: This file provides entries for `default_compilers` in
`gcc.c` which override the default of giving an error that a
compiler for that language is not installed.

**`language-tree.def`**
: This file, which need not exist, defines any language-specific tree
codes.
