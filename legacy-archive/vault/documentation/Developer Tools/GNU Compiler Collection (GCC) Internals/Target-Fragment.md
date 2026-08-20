---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Target-Fragment.html
archived_at: '2026-07-15T07:31:00.875190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Host Fragment](Host-Fragment.md#apple-jbxxg5bnizzgcz3nmvxhi),
Up: [Fragments](Fragments.md#apple-izzgcz3nmvxhi4y)

---

### 15.1 Target Makefile Fragments

Target makefile fragments can set these Makefile variables.

**`LIBGCC2_CFLAGS`**
: Compiler flags to use when compiling `libgcc2.c`.

**`LIB2FUNCS_EXTRA`**
: A list of source file names to be compiled or assembled and inserted
into `libgcc.a`.

**`Floating Point Emulation`**
: To have GCC include software floating point libraries in `libgcc.a`
define `FPBIT` and `DPBIT` along with a few rules as follows:

```
          # We want fine grained libraries, so use the new code
          # to build the floating point emulation libraries.
          FPBIT = fp-bit.c
          DPBIT = dp-bit.c

          fp-bit.c: $(srcdir)/config/fp-bit.c
                  echo '#define FLOAT' > fp-bit.c
                  cat $(srcdir)/config/fp-bit.c >> fp-bit.c

          dp-bit.c: $(srcdir)/config/fp-bit.c
                  cat $(srcdir)/config/fp-bit.c > dp-bit.c

```

You may need to provide additional #defines at the beginning of `fp-bit.c`
and `dp-bit.c` to control target endianness and other options.

**`CRTSTUFF_T_CFLAGS`**
: Special flags used when compiling `crtstuff.c`.
See [Initialization](Initialization.md#apple-jfxgs5djmfwgs6tboruw63q).

**`CRTSTUFF_T_CFLAGS_S`**
: Special flags used when compiling `crtstuff.c` for shared
linking. Used if you use `crtbeginS.o` and `crtendS.o`
in `EXTRA-PARTS`.
See [Initialization](Initialization.md#apple-jfxgs5djmfwgs6tboruw63q).

**`MULTILIB_OPTIONS`**
: For some targets, invoking GCC in different ways produces objects
that can not be linked together. For example, for some targets GCC
produces both big and little endian code. For these targets, you must
arrange for multiple versions of `libgcc.a` to be compiled, one for
each set of incompatible options. When GCC invokes the linker, it
arranges to link in the right version of `libgcc.a`, based on
the command line options used.

The `MULTILIB_OPTIONS` macro lists the set of options for which
special versions of `libgcc.a` must be built. Write options that
are mutually incompatible side by side, separated by a slash. Write
options that may be used together separated by a space. The build
procedure will build all combinations of compatible options.

For example, if you set `MULTILIB_OPTIONS` to ``m68000/m68020
msoft-float`', `Makefile` will build special versions of
`libgcc.a` using the following sets of options: `-m68000`,
`-m68020`, `-msoft-float`, ``-m68000 -msoft-float`', and
``-m68020 -msoft-float`'.

**`MULTILIB_DIRNAMES`**
: If `MULTILIB_OPTIONS` is used, this variable specifies the
directory names that should be used to hold the various libraries.
Write one element in `MULTILIB_DIRNAMES` for each element in
`MULTILIB_OPTIONS`. If `MULTILIB_DIRNAMES` is not used, the
default value will be `MULTILIB_OPTIONS`, with all slashes treated
as spaces.

For example, if `MULTILIB_OPTIONS` is set to ``m68000/m68020
msoft-float`', then the default value of `MULTILIB_DIRNAMES` is
``m68000 m68020 msoft-float`'. You may specify a different value if
you desire a different set of directory names.

**`MULTILIB_MATCHES`**
: Sometimes the same option may be written in two different ways. If an
option is listed in `MULTILIB_OPTIONS`, GCC needs to know about
any synonyms. In that case, set `MULTILIB_MATCHES` to a list of
items of the form ``option=option`' to describe all relevant
synonyms. For example, ``m68000=mc68000 m68020=mc68020`'.

**`MULTILIB_EXCEPTIONS`**
: Sometimes when there are multiple sets of `MULTILIB_OPTIONS` being
specified, there are combinations that should not be built. In that
case, set `MULTILIB_EXCEPTIONS` to be all of the switch exceptions
in shell case syntax that should not be built.

For example the ARM processor cannot execute both hardware floating
point instructions and the reduced size THUMB instructions at the same
time, so there is no need to build libraries with both of these
options enabled. Therefore `MULTILIB_EXCEPTIONS` is set to:

```
          *mthumb/*mhard-float*

```


**`MULTILIB_EXTRA_OPTS`**
: Sometimes it is desirable that when building multiple versions of
`libgcc.a` certain options should always be passed on to the
compiler. In that case, set `MULTILIB_EXTRA_OPTS` to be the list
of options to be used for all builds. If you set this, you should
probably set `CRTSTUFF_T_CFLAGS` to a dash followed by it.

**`SPECS`**
: Unfortunately, setting `MULTILIB_EXTRA_OPTS` is not enough, since
it does not affect the build of target libraries, at least not the
build of the default multilib. One possible work-around is to use
`DRIVER_SELF_SPECS` to bring options from the `specs` file
as if they had been passed in the compiler driver command line.
However, you don't want to be adding these options after the toolchain
is installed, so you can instead tweak the `specs` file that will
be used during the toolchain build, while you still install the
original, built-in `specs`. The trick is to set `SPECS` to
some other filename (say `specs.install`), that will then be
created out of the built-in specs, and introduce a `Makefile`
rule to generate the `specs` file that's going to be used at
build time out of your `specs.install`.
