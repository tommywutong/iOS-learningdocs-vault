---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_12.html
archived_at: '2026-07-15T07:31:03.718324Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Native%20Debugging.md), [next](Coding.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Support Libraries](GDB%20Internals.md#apple-krhugojy)

## [BFD](GDB%20Internals.md#apple-krhugojz)

BFD provides support for GDB in several ways:

**_identifying executable and core files_**
: BFD will identify a variety of file types, including a.out, coff, and
several variants thereof, as well as several kinds of core files.

**_access to sections of files_**
: BFD parses the file headers to determine the names, virtual addresses,
sizes, and file locations of all the various named sections in files
(such as the text section or the data section). GDB simply
calls BFD to read or write section x at byte offset y for
length z.

**_specialized core file support_**
: BFD provides routines to determine the failing command name stored in a
core file, the signal with which the program failed, and whether a core
file matches (i.e. could be a core dump of) a particular executable
file.

**_locating the symbol information_**
: GDB uses an internal interface of BFD to determine where to find the
symbol information in an executable file or symbol-file. GDB itself
handles the reading of symbols, since BFD does not "understand" debug
symbols, but GDB uses BFD's cached information to find the symbols,
string table, etc.

## [opcodes](GDB%20Internals.md#apple-krhugmjqga)

The opcodes library provides GDB's disassembler. (It's a separate
library because it's also used in binutils, for `objdump').

## [readline](GDB%20Internals.md#apple-krhugmjqge)

## [mmalloc](GDB%20Internals.md#apple-krhugmjqgi)

## [libiberty](GDB%20Internals.md#apple-krhugmjqgm)

The `libiberty` library provides a set of functions and features
that integrate and improve on functionality found in modern operating
systems. Broadly speaking, such features can be divided into three
groups: supplemental functions (functions that may be missing in some
environments and operating systems), replacement functions (providing
a uniform and easier to use interface for commonly used standard
functions), and extensions (which provide additional functionality
beyond standard functions).

GDB uses various features provided by the `libiberty`
library, for instance the C++ demangler, the @acronym{IEEE}
floating format support functions, the input options parser
`` `getopt' ``, the `` `obstack' `` extension, and other functions.

### [`obstacks` in GDB](gdbint_toc.md#apple-krhugmjqgq)

The obstack mechanism provides a convenient way to allocate and free
chunks of memory. Each obstack is a pool of memory that is managed
like a stack. Objects (of any nature, size and alignment) are
allocated and freed in a @acronym{LIFO} fashion on an obstack (see
`libiberty`'s documenatation for a more detailed explanation of
`obstacks`).

The most noticeable use of the `obstacks` in GDB is in
object files. There is an obstack associated with each internal
representation of an object file. Lots of things get allocated on
these `obstacks`: dictionary entries, blocks, blockvectors,
symbols, minimal symbols, types, vectors of fundamental types, class
fields of types, object files section lists, object files section
offets lists, line tables, symbol tables, partial symbol tables,
string tables, symbol table private data, macros tables, debug
information sections and entries, import and export lists (som),
unwind information (hppa), dwarf2 location expressions data. Plus
various strings such as directory names strings, debug format strings,
names of types.

An essential and convenient property of all data on `obstacks` is
that memory for it gets allocated (with `obstack_alloc`) at
various times during a debugging sesssion, but it is released all at
once using the `obstack_free` function. The `obstack_free`
function takes a pointer to where in the stack it must start the
deletion from (much like the cleanup chains have a pointer to where to
start the cleanups). Because of the stack like structure of the
`obstacks`, this allows to free only a top portion of the
obstack. There are a few instances in GDB where such thing
happens. Calls to `obstack_free` are done after some local data
is allocated to the obstack. Only the local data is deleted from the
obstack. Of course this assumes that nothing between the
`obstack_alloc` and the `obstack_free` allocates anything
else on the same obstack. For this reason it is best and safest to
use temporary `obstacks`.

Releasing the whole obstack is also not safe per se. It is safe only
under the condition that we know the `obstacks` memory is no
longer needed. In GDB we get rid of the `obstacks` only
when we get rid of the whole objfile(s), for instance upon reading a
new symbol file.

## [gnu-regex](GDB%20Internals.md#apple-krhugmjqgu)

Regex conditionals.

**`C_ALLOCA`**
:

**`NFAILURES`**
:

**`RE_NREGS`**
:

**`SIGN_EXTEND_CHAR`**
:

**`SWITCH_ENUM_BUG`**
:

**`SYNTAX_TABLE`**
:

**`Sword`**
:

**`sparc`**
:

## [include](GDB%20Internals.md#apple-krhugmjqgy)

---

Go to the [first](Requirements.md), [previous](Native%20Debugging.md), [next](Coding.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
