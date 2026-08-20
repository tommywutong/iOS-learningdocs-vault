---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_31.html
archived_at: '2026-07-15T07:31:03.457167Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Formatting%20Documentation.md), [next](Maintenance%20Commands.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Installing GDB](Debugging%20with%20GDB.md#apple-krhugmrzg4)

GDB comes with a `configure` script that automates the process
of preparing GDB for installation; you can then use `make` to
build the `gdb` program.
[(8)](Debugging%20with%20GDB-2.md#apple-izhu6vby)

The GDB distribution includes all the source code you need for
GDB in a single directory, whose name is usually composed by
appending the version number to `` `gdb' ``.

For example, the GDB version 6.3.50.20050815-cvs distribution is in the
`gdb-6.3.50.20050815-cvs' directory. That directory contains:

**`gdb-6.3.50.20050815-cvs/configure (and supporting files)`**
: script for configuring GDB and all its supporting libraries

**`gdb-6.3.50.20050815-cvs/gdb`**
: the source specific to GDB itself

**`gdb-6.3.50.20050815-cvs/bfd`**
: source for the Binary File Descriptor library

**`gdb-6.3.50.20050815-cvs/include`**
: GNU include files

**`gdb-6.3.50.20050815-cvs/libiberty`**
: source for the `` `-liberty' `` free software library

**`gdb-6.3.50.20050815-cvs/opcodes`**
: source for the library of opcode tables and disassemblers

**`gdb-6.3.50.20050815-cvs/readline`**
: source for the GNU command-line interface

**`gdb-6.3.50.20050815-cvs/glob`**
: source for the GNU filename pattern-matching subroutine

**`gdb-6.3.50.20050815-cvs/mmalloc`**
: source for the GNU memory-mapped malloc package

The simplest way to configure and build GDB is to run `configure`
from the `gdb-version-number' source directory, which in
this example is the `gdb-6.3.50.20050815-cvs' directory.

First switch to the `gdb-version-number' source directory
if you are not already in it; then run `configure`. Pass the
identifier for the platform on which GDB will run as an
argument.

For example:

```
cd gdb-6.3.50.20050815-cvs
./configure host
make
```

where host is an identifier such as `` `sun4' `` or
`` `decstation' ``, that identifies the platform where GDB will run.
(You can often leave off host; `configure` tries to guess the
correct value by examining your system.)

Running `` `configure host' `` and then running `make` builds the
`bfd', `readline', `mmalloc', and `libiberty'
libraries, then `gdb` itself. The configured source files, and the
binaries, are left in the corresponding source directories.

`configure` is a Bourne-shell (`/bin/sh`) script; if your
system does not recognize this automatically when you run a different
shell, you may need to run `sh` on it explicitly:

```
sh configure host
```

If you run `configure` from a directory that contains source
directories for multiple libraries or programs, such as the
`gdb-6.3.50.20050815-cvs' source directory for version 6.3.50.20050815-cvs, `configure`
creates configuration files for every directory level underneath (unless
you tell it not to, with the `` `--norecursion' `` option).

You should run the `configure` script from the top directory in the
source tree, the `gdb-version-number' directory. If you run
`configure` from one of the subdirectories, you will configure only
that subdirectory. That is usually not what you want. In particular,
if you run the first `configure` from the `gdb' subdirectory
of the `gdb-version-number' directory, you will omit the
configuration of `bfd', `readline', and other sibling
directories of the `gdb' subdirectory. This leads to build errors
about missing include files such as `bfd/bfd.h'.

You can install `gdb` anywhere; it has no hardwired paths.
However, you should make sure that the shell on your path (named by
the `` `SHELL' `` environment variable) is publicly readable. Remember
that GDB uses the shell to start your program--some systems refuse to
let GDB debug child processes whose programs are not readable.

## [Compiling GDB in another directory](Debugging%20with%20GDB.md#apple-krhugmrzha)

If you want to run GDB versions for several host or target machines,
you need a different `gdb` compiled for each combination of
host and target. `configure` is designed to make this easy by
allowing you to generate each configuration in a separate subdirectory,
rather than in the source directory. If your `make` program
handles the `` `VPATH' `` feature (GNU `make` does), running
`make` in each of these directories builds the `gdb`
program specified there.

To build `gdb` in a separate directory, run `configure`
with the `` `--srcdir' `` option to specify where to find the source.
(You also need to specify a path to find `configure`
itself from your working directory. If the path to `configure`
would be the same as the argument to `` `--srcdir' ``, you can leave out
the `` `--srcdir' `` option; it is assumed.)

For example, with version 6.3.50.20050815-cvs, you can build GDB in a
separate directory for a Sun 4 like this:

```
cd gdb-6.3.50.20050815-cvs
mkdir ../gdb-sun4
cd ../gdb-sun4
../gdb-6.3.50.20050815-cvs/configure sun4
make
```

When `configure` builds a configuration using a remote source
directory, it creates a tree for the binaries with the same structure
(and using the same names) as the tree under the source directory. In
the example, you'd find the Sun 4 library `libiberty.a' in the
directory `gdb-sun4/libiberty', and GDB itself in
`gdb-sun4/gdb'.

Make sure that your path to the `configure' script has just one
instance of `gdb' in it. If your path to `configure' looks
like `../gdb-6.3.50.20050815-cvs/gdb/configure', you are configuring only
one subdirectory of GDB, not the whole package. This leads to
build errors about missing include files such as `bfd/bfd.h'.

One popular reason to build several GDB configurations in separate
directories is to configure GDB for cross-compiling (where
GDB runs on one machine--the __host__---while debugging
programs that run on another machine--the __target__).
You specify a cross-debugging target by
giving the `` `--target=target' `` option to `configure`.

When you run `make` to build a program or library, you must run
it in a configured directory--whatever directory you were in when you
called `configure` (or one of its subdirectories).

The `Makefile` that `configure` generates in each source
directory also runs recursively. If you type `make` in a source
directory such as `gdb-6.3.50.20050815-cvs' (or in a separate configured
directory configured with `` `--srcdir=dirname/gdb-6.3.50.20050815-cvs' ``), you
will build all the required libraries, and then build GDB.

When you have multiple hosts or targets configured in separate
directories, you can run `make` on them in parallel (for example,
if they are NFS-mounted on each of the hosts); they will not interfere
with each other.

## [Specifying names for hosts and targets](Debugging%20with%20GDB.md#apple-krhugmrzhe)

The specifications used for hosts and targets in the `configure`
script are based on a three-part naming scheme, but some short predefined
aliases are also supported. The full naming scheme encodes three pieces
of information in the following pattern:

```
architecture-vendor-os
```

For example, you can use the alias `sun4` as a host argument,
or as the value for target in a `--target=target`
option. The equivalent full name is `` `sparc-sun-sunos4' ``.

The `configure` script accompanying GDB does not provide
any query facility to list all supported host and target names or
aliases. `configure` calls the Bourne shell script
`config.sub` to map abbreviations to full names; you can read the
script, if you wish, or you can use it to test your guesses on
abbreviations--for example:

```shell
% sh config.sub i386-linux
i386-pc-linux-gnu
% sh config.sub alpha-linux
alpha-unknown-linux-gnu
% sh config.sub hp9k700
hppa1.1-hp-hpux
% sh config.sub sun4
sparc-sun-sunos4.1.1
% sh config.sub sun3
m68k-sun-sunos4.1.1
% sh config.sub i986v
Invalid configuration `i986v': machine `i986v' not recognized
```

`config.sub` is also distributed in the GDB source
directory (`gdb-6.3.50.20050815-cvs', for version 6.3.50.20050815-cvs).

## [`configure` options](gdb_toc.md#apple-krhugmzqga)

Here is a summary of the `configure` options and arguments that
are most often useful for building GDB. `configure` also has
several other options not listed here. See Info file `configure.info', node `What Configure Does', for a full explanation of `configure`.

```
configure [--help]
          [--prefix=dir]
          [--exec-prefix=dir]
          [--srcdir=dirname]
          [--norecursion] [--rm]
          [--target=target]
          host
```

You may introduce options with a single `` `-' `` rather than
`` `--' `` if you prefer; but you may abbreviate option names if you use
`` `--' ``.

**`--help`**
: Display a quick summary of how to invoke `configure`.

**`--prefix=dir`**
: Configure the source to install programs and files under directory
`dir'.

**`--exec-prefix=dir`**
: Configure the source to install programs under directory
`dir'.

**`--srcdir=dirname`**
: __Warning: using this option requires GNU `make`, or another
`make` that implements the `VPATH` feature.__
Use this option to make configurations in directories separate from the
GDB source directories. Among other things, you can use this to
build (or maintain) several configurations simultaneously, in separate
directories. `configure` writes configuration specific files in
the current directory, but arranges for them to use the source in the
directory dirname. `configure` creates directories under
the working directory in parallel to the source directories below
dirname.

**`--norecursion`**
: Configure only the directory level where `configure` is executed; do not
propagate configuration to subdirectories.

**`--target=target`**
: Configure GDB for cross-debugging programs running on the specified
target. Without this option, GDB is configured to debug
programs that run on the same machine (host) as GDB itself.
There is no convenient way to generate a list of all available targets.

**`host ...`**
: Configure GDB to run on the specified host.
There is no convenient way to generate a list of all available hosts.

There are many other options available as well, but they are generally
needed for special purposes only.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Formatting%20Documentation.md), [next](Maintenance%20Commands.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
