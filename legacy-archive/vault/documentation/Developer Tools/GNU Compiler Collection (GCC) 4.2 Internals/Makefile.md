---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Makefile.html
archived_at: '2026-07-15T07:31:02.358755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Library Files](Library-Files.md#apple-jruwe4tboj4s2rtjnrsxg),
Previous: [Build](Build.md#apple-ij2ws3de),
Up: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)

---

#### 6.3.4 Makefile Targets

These targets are available from the ``gcc`' directory:

**`all`**
: This is the default target. Depending on what your build/host/target
configuration is, it coordinates all the things that need to be built.

**`doc`**
: Produce info-formatted documentation and man pages. Essentially it
calls ``make man`' and ``make info`'.

**`dvi`**
: Produce DVI-formatted documentation.

**`pdf`**
: Produce PDF-formatted documentation.

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

The toplevel tree from which you start GCC compilation is not
the GCC directory, but rather a complex Makefile that coordinates
the various steps of the build, including bootstrapping the compiler
and using the new compiler to build target libraries.

When GCC is configured for a native configuration, the default action
for `make` is to do a full three-stage bootstrap. This means
that GCC is built three times—once with the native compiler, once with
the native-built compiler it just built, and once with the compiler it
built the second time. In theory, the last two should produce the same
results, which ``make compare`' can check. Each stage is configured
separately and compiled into a separate directory, to minimize problems
due to ABI incompatibilities between the native compiler and GCC.

If you do a change, rebuilding will also start from the first stage
and “bubble” up the change through the three stages. Each stage
is taken from its build directory (if it had been built previously),
rebuilt, and copied to its subdirectory. This will allow you to, for
example, continue a bootstrap after fixing a bug which causes the
stage2 build to crash. It does not provide as good coverage of the
compiler as bootstrapping from scratch, but it ensures that the new
code is syntactically correct (e.g. that you did not use GCC extensions
by mistake), and avoids spurious bootstrap comparison
failures[1](#apple-mzxc2mi).

Other targets available from the top level include:

**`bootstrap-lean`**
: Like `bootstrap`, except that the various stages are removed once
they're no longer needed. This saves disk space.

**`bootstrap2`

**`bootstrap2-lean`****
: Performs only the first two stages of bootstrap. Unlike a three-stage
bootstrap, this does not perform a comparison to test that the compiler
is running properly. Note that the disk space required by a “lean”
bootstrap is approximately independent of the number of stages.

**`stage`N`-bubble (`N `= 1...4)`**
: Rebuild all the stages up to N, with the appropriate flags,
“bubbling” the changes as described above.

**`all-stage`N `(`N `= 1...4)`**
: Assuming that stage N has already been built, rebuild it with the
appropriate flags. This is rarely needed.

**`cleanstrap`**
: Remove everything (``make clean`') and rebuilds (``make bootstrap`').

**`compare`**
: Compares the results of stages 2 and 3. This ensures that the compiler
is running properly, since it should produce the same object files
regardless of how it itself was compiled.

**`profiledbootstrap`**
: Builds a compiler with profiling feedback information. For more
information, see
[Building with profile feedback](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccinstall/Building.html#Building).

**`restrap`**
: Restart a bootstrap, so that everything that was not built with
the system compiler is rebuilt.

**`stage`N`-start (`N `= 1...4)`**
: For each package that is bootstrapped, rename directories so that,
for example, `gcc` points to the stageN GCC, compiled
with the stageN-1 GCC[2](#apple-mzxc2mq).

You will invoke this target if you need to test or debug the
stageN GCC. If you only need to execute GCC (but you need
not run ``make`' either to rebuild it or to run test suites),
you should be able to work directly in the `stageN-gcc`
directory. This makes it easier to debug multiple stages in
parallel.

**`stage`**
: For each package that is bootstrapped, relocate its build directory
to indicate its stage. For example, if the `gcc` directory
points to the stage2 GCC, after invoking this target it will be
renamed to `stage2-gcc`.

If you wish to use non-default GCC flags when compiling the stage2 and
stage3 compilers, set `BOOT_CFLAGS` on the command line when doing
``make`'.

Usually, the first stage only builds the languages that the compiler
is written in: typically, C and maybe Ada. If you are debugging a
miscompilation of a different stage2 front-end (for example, of the
Fortran front-end), you may want to have front-ends for other languages
in the first stage as well. To do so, set `STAGE1_LANGUAGES`
on the command line when doing ``make`'.

For example, in the aforementioned scenario of debugging a Fortran
front-end miscompilation caused by the stage1 compiler, you may need a
command like

```
     make stage2-bubble STAGE1_LANGUAGES=c,fortran
```

Alternatively, you can use per-language targets to build and test
languages that are not enabled by default in stage1. For example,
`make f951` will build a Fortran compiler even in the stage1
build directory.

---

#### Footnotes

[[1](#apple-mzxgiljr)] Except if the compiler was buggy and miscompiled
some of the files that were not modified. In this case, it's best
to use `make restrap`.

[[2](#apple-mzxgiljs)] Customarily, the system compiler
is also termed the `stage0` GCC.

---
