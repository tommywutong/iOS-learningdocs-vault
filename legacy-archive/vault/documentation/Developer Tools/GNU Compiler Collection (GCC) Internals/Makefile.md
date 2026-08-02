---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Makefile.html
archived_at: '2026-07-15T07:31:00.351976Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Library Files](Library-Files.md#apple-jruwe4tboj4s2rtjnrsxg),
Previous: [Build](Build.md#apple-ij2ws3de),
Up: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)

---

#### 6.3.4 Makefile Targets

**`all`**
: This is the default target. Depending on what your build/host/target
configuration is, it coordinates all the things that need to be built.

**`doc`**
: Produce info-formatted documentation and man pages. Essentially it
calls ``make man`' and ``make info`'.

**`dvi`**
: Produce DVI-formatted documentation.

**`html`**
: Produce HTML-formatted documentation.

**`man`**
: Generate man pages.

**`info`**
: Generate info-formatted pages.

**`mostlyclean`**
: Delete the files made while building the compiler.

**`clean`**
: That, and all the other files built by ``make all`'.

**`distclean`**
: That, and all the files created by `configure`.

**`maintainer-clean`**
: Distclean plus any file that can be generated from other files. Note
that additional tools may be required beyond what is normally needed to
build gcc.

**`srcextra`**
: Generates files in the source directory that do not exist in CVS but
should go into a release tarball. One example is `gcc/java/parse.c`
which is generated from the CVS source file `gcc/java/parse.y`.

**`srcinfo`

**`srcman`****
: Copies the info-formatted and manpage documentation into the source
directory usually for the purpose of generating a release tarball.

**`install`**
: Installs gcc.

**`uninstall`**
: Deletes installed files.

**`check`**
: Run the testsuite. This creates a `testsuite` subdirectory that
has various `.sum` and `.log` files containing the results of
the testing. You can run subsets with, for example, ``make check-gcc`'.
You can specify specific tests by setting RUNTESTFLAGS to be the name
of the `.exp` file, optionally followed by (for some tests) an equals
and a file wildcard, like:

```
          make check-gcc RUNTESTFLAGS="execute.exp=19980413-*"

```

Note that running the testsuite may require additional tools be
installed, such as TCL or dejagnu.

**`bootstrap`**
: Builds GCC three times—once with the native compiler, once with the
native-built compiler it just built, and once with the compiler it built
the second time. In theory, the last two should produce the same
results, which ``make compare`' can check. Each step of this process
is called a “stage”, and the results of each stage N
(N = 1...3) are copied to a subdirectory `stageN/`.

**`bootstrap-lean`**
: Like `bootstrap`, except that the various stages are removed once
they're no longer needed. This saves disk space.

**`bubblestrap`**
: This incrementally rebuilds each of the three stages, one at a time.
It does this by “bubbling” the stages up from their subdirectories
(if they had been built previously), rebuilding them, and copying them
back to their subdirectories. This will allow you to, for example,
continue a bootstrap after fixing a bug which causes the stage2 build
to crash.

**`quickstrap`**
: Rebuilds the most recently built stage. Since each stage requires
special invocation, using this target means you don't have to keep
track of which stage you're on or what invocation that stage needs.

**`cleanstrap`**
: Removed everything (``make clean`') and rebuilds (``make bootstrap`').

**`restrap`**
: Like `cleanstrap`, except that the process starts from the first
stage build, not from scratch.

**`stage`N `(`N `= 1...4)`**
: For each stage, moves the appropriate files to the `stageN`
subdirectory.

**`unstage`N `(`N `= 1...4)`**
: Undoes the corresponding `stage`N.

**`restage`N `(`N `= 1...4)`**
: Undoes the corresponding `stage`N and rebuilds it with the
appropriate flags.

**`compare`**
: Compares the results of stages 2 and 3. This ensures that the compiler
is running properly, since it should produce the same object files
regardless of how it itself was compiled.

**`profiledbootstrap`**
: Builds a compiler with profiling feedback information. For more
information, see
[Building with profile feedback](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccinstall/Building.html#Building).
This is actually a target in the top-level directory, which then
recurses into the `gcc` subdirectory multiple times.
