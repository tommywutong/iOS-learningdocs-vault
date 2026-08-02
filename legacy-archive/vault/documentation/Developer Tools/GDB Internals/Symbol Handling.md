---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_6.html
archived_at: '2026-07-15T07:31:03.870421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](libgdb.md), [next](Language%20Support.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Symbol Handling](GDB%20Internals.md#apple-krhugmzu)

Symbols are a key part of GDB's operation. Symbols include variables,
functions, and types.

## [Symbol Reading](GDB%20Internals.md#apple-krhugmzv)

GDB reads symbols from __symbol files__. The usual symbol
file is the file containing the program which GDB is
debugging. GDB can be directed to use a different file for
symbols (with the `` `symbol-file' `` command), and it can also read
more symbols via the `` `add-file' `` and `` `load' `` commands, or while
reading symbols from shared libraries.

Symbol files are initially opened by code in `symfile.c' using
the BFD library (see section [Support Libraries](Support%20Libraries.md#apple-kncugojy)). BFD identifies the type
of the file by examining its header. `find_sym_fns` then uses
this identification to locate a set of symbol-reading functions.

Symbol-reading modules identify themselves to GDB by calling
`add_symtab_fns` during their module initialization. The argument
to `add_symtab_fns` is a `struct sym_fns` which contains the
name (or name prefix) of the symbol format, the length of the prefix,
and pointers to four functions. These functions are called at various
times to process symbol files whose identification matches the specified
prefix.

The functions supplied by each module are:

**`xyz_symfile_init(struct sym_fns *sf)`**
: 
Called from `symbol_file_add` when we are about to read a new
symbol file. This function should clean up any internal state (possibly
resulting from half-read previous files, for example) and prepare to
read a new symbol file. Note that the symbol file which we are reading
might be a new "main" symbol file, or might be a secondary symbol file
whose symbols are being added to the existing symbol table.
The argument to `xyz_symfile_init` is a newly allocated
`struct sym_fns` whose `bfd` field contains the BFD for the
new symbol file being read. Its `private` field has been zeroed,
and can be modified as desired. Typically, a struct of private
information will be `malloc`'d, and a pointer to it will be placed
in the `private` field.
There is no result from `xyz_symfile_init`, but it can call
`error` if it detects an unavoidable problem.

**`xyz_new_init()`**
: Called from `symbol_file_add` when discarding existing symbols.
This function needs only handle the symbol-reading module's internal
state; the symbol table data structures visible to the rest of
GDB will be discarded by `symbol_file_add`. It has no
arguments and no result. It may be called after
`xyz_symfile_init`, if a new symbol table is being read, or
may be called alone if all symbols are simply being discarded.

**`xyz_symfile_read(struct sym_fns *sf, CORE_ADDR addr, int mainline)`**
: Called from `symbol_file_add` to actually read the symbols from a
symbol-file into a set of psymtabs or symtabs.
`sf` points to the `struct sym_fns` originally passed to
`xyz_sym_init` for possible initialization. `addr` is
the offset between the file's specified start address and its true
address in memory. `mainline` is 1 if this is the main symbol
table being read, and 0 if a secondary symbol file (e.g. shared library
or dynamically loaded file) is being read.

In addition, if a symbol-reading module creates psymtabs when
xyz_symfile_read is called, these psymtabs will contain a pointer
to a function `xyz_psymtab_to_symtab`, which can be called
from any point in the GDB symbol-handling code.

**`xyz_psymtab_to_symtab (struct partial_symtab *pst)`**
: Called from `psymtab_to_symtab` (or the `PSYMTAB_TO_SYMTAB` macro) if
the psymtab has not already been read in and had its `pst->symtab`
pointer set. The argument is the psymtab to be fleshed-out into a
symtab. Upon return, `pst->readin` should have been set to 1, and
`pst->symtab` should contain a pointer to the new corresponding symtab, or
zero if there were no symbols in that part of the symbol file.

## [Partial Symbol Tables](GDB%20Internals.md#apple-krhugmzw)

GDB has three types of symbol tables:

- 
  
  Full symbol tables (__symtabs__). These contain the main
  information about symbols and addresses.
  
- Partial symbol tables (__psymtabs__). These contain enough
  information to know when to read the corresponding part of the full
  symbol table.

- Minimal symbol tables (__msymtabs__). These contain information
  gleaned from non-debugging symbols.

This section describes partial symbol tables.

A psymtab is constructed by doing a very quick pass over an executable
file's debugging information. Small amounts of information are
extracted--enough to identify which parts of the symbol table will
need to be re-read and fully digested later, when the user needs the
information. The speed of this pass causes GDB to start up very
quickly. Later, as the detailed rereading occurs, it occurs in small
pieces, at various times, and the delay therefrom is mostly invisible to
the user.

The symbols that show up in a file's psymtab should be, roughly, those
visible to the debugger's user when the program is not running code from
that file. These include external symbols and types, static symbols and
types, and `enum` values declared at file scope.

The psymtab also contains the range of instruction addresses that the
full symbol table would represent.

The idea is that there are only two ways for the user (or much of the
code in the debugger) to reference a symbol:

- 
  
  By its address (e.g. execution stops at some address which is inside a
  function in this file). The address will be noticed to be in the
  range of this psymtab, and the full symtab will be read in.
  `find_pc_function`, `find_pc_line`, and other
  `find_pc_...` functions handle this.
  
- By its name
  (e.g. the user asks to print a variable, or set a breakpoint on a
  function). Global names and file-scope names will be found in the
  psymtab, which will cause the symtab to be pulled in. Local names will
  have to be qualified by a global name, or a file-scope name, in which
  case we will have already read in the symtab as we evaluated the
  qualifier. Or, a local symbol can be referenced when we are "in" a
  local scope, in which case the first case applies. `lookup_symbol`
  does most of the work here.

The only reason that psymtabs exist is to cause a symtab to be read in
at the right moment. Any symbol that can be elided from a psymtab,
while still causing that to happen, should not appear in it. Since
psymtabs don't have the idea of scope, you can't put local symbols in
them anyway. Psymtabs don't have the idea of the type of a symbol,
either, so types need not appear, unless they will be referenced by
name.

It is a bug for GDB to behave one way when only a psymtab has
been read, and another way if the corresponding symtab has been read
in. Such bugs are typically caused by a psymtab that does not contain
all the visible symbols, or which has the wrong instruction address
ranges.

The psymtab for a particular section of a symbol file (objfile) could be
thrown away after the symtab has been read in. The symtab should always
be searched before the psymtab, so the psymtab will never be used (in a
bug-free environment). Currently, psymtabs are allocated on an obstack,
and all the psymbols themselves are allocated in a pair of large arrays
on an obstack, so there is little to be gained by trying to free them
unless you want to do a lot more work.

## [Types](GDB%20Internals.md#apple-krhugmzx)

### [Fundamental Types (e.g., `FT_VOID`, `FT_BOOLEAN`).](gdbint_toc.md#apple-krhugmzy)

These are the fundamental types that GDB uses internally. Fundamental
types from the various debugging formats (stabs, ELF, etc) are mapped
into one of these. They are basically a union of all fundamental types
that GDB knows about for all the languages that GDB
knows about.

### [Type Codes (e.g., `TYPE_CODE_PTR`, `TYPE_CODE_ARRAY`).](gdbint_toc.md#apple-krhugmzz)

Each time GDB builds an internal type, it marks it with one
of these types. The type may be a fundamental type, such as
`TYPE_CODE_INT`, or a derived type, such as `TYPE_CODE_PTR`
which is a pointer to another type. Typically, several `FT_*`
types map to one `TYPE_CODE_*` type, and are distinguished by
other members of the type struct, such as whether the type is signed
or unsigned, and how many bits it uses.

### [Builtin Types (e.g., `builtin_type_void`, `builtin_type_char`).](gdbint_toc.md#apple-krhugnbq)

These are instances of type structs that roughly correspond to
fundamental types and are created as global types for GDB to
use for various ugly historical reasons. We eventually want to
eliminate these. Note for example that `builtin_type_int`
initialized in `gdbtypes.c' is basically the same as a
`TYPE_CODE_INT` type that is initialized in `c-lang.c' for
an `FT_INTEGER` fundamental type. The difference is that the
`builtin_type` is not associated with any particular objfile, and
only one instance exists, while `c-lang.c' builds as many
`TYPE_CODE_INT` types as needed, with each one associated with
some particular objfile.

## [Object File Formats](GDB%20Internals.md#apple-krhugnbr)

### [a.out](GDB%20Internals.md#apple-krhugnbs)

The `a.out` format is the original file format for Unix. It
consists of three sections: `text`, `data`, and `bss`,
which are for program code, initialized data, and uninitialized data,
respectively.

The `a.out` format is so simple that it doesn't have any reserved
place for debugging information. (Hey, the original Unix hackers used
`` `adb' ``, which is a machine-language debugger!) The only debugging
format for `a.out` is stabs, which is encoded as a set of normal
symbols with distinctive attributes.

The basic `a.out` reader is in `dbxread.c'.

### [COFF](GDB%20Internals.md#apple-krhugnbt)

The COFF format was introduced with System V Release 3 (SVR3) Unix.
COFF files may have multiple sections, each prefixed by a header. The
number of sections is limited.

The COFF specification includes support for debugging. Although this
was a step forward, the debugging information was woefully limited. For
instance, it was not possible to represent code that came from an
included file.

The COFF reader is in `coffread.c'.

### [ECOFF](GDB%20Internals.md#apple-krhugnbu)

ECOFF is an extended COFF originally introduced for Mips and Alpha
workstations.

The basic ECOFF reader is in `mipsread.c'.

### [XCOFF](GDB%20Internals.md#apple-krhugnbv)

The IBM RS/6000 running AIX uses an object file format called XCOFF.
The COFF sections, symbols, and line numbers are used, but debugging
symbols are `dbx`-style stabs whose strings are located in the
`.debug` section (rather than the string table). For more
information, see section `Top' in The Stabs Debugging Format.

The shared library scheme has a clean interface for figuring out what
shared libraries are in use, but the catch is that everything which
refers to addresses (symbol tables and breakpoints at least) needs to be
relocated for both shared libraries and the main executable. At least
using the standard mechanism this can only be done once the program has
been run (or the core file has been read).

### [PE](GDB%20Internals.md#apple-krhugnbw)

Windows 95 and NT use the PE (__Portable Executable__) format for their
executables. PE is basically COFF with additional headers.

While BFD includes special PE support, GDB needs only the basic
COFF reader.

### [ELF](GDB%20Internals.md#apple-krhugnbx)

The ELF format came with System V Release 4 (SVR4) Unix. ELF is similar
to COFF in being organized into a number of sections, but it removes
many of COFF's limitations.

The basic ELF reader is in `elfread.c'.

### [SOM](GDB%20Internals.md#apple-krhugnby)

SOM is HP's object file and debug format (not to be confused with IBM's
SOM, which is a cross-language ABI).

The SOM reader is in `hpread.c'.

### [Other File Formats](GDB%20Internals.md#apple-krhugnbz)

Other file formats that have been supported by GDB include Netware
Loadable Modules (`nlmread.c').

## [Debugging File Formats](GDB%20Internals.md#apple-krhugnjq)

This section describes characteristics of debugging information that
are independent of the object file format.

### [stabs](GDB%20Internals.md#apple-krhugnjr)

`stabs` started out as special symbols within the `a.out`
format. Since then, it has been encapsulated into other file
formats, such as COFF and ELF.

While `dbxread.c' does some of the basic stab processing,
including for encapsulated versions, `stabsread.c' does
the real work.

### [COFF](GDB%20Internals.md#apple-krhugnjs)

The basic COFF definition includes debugging information. The level
of support is minimal and non-extensible, and is not often used.

### [Mips debug (Third Eye)](GDB%20Internals.md#apple-krhugnjt)

ECOFF includes a definition of a special debug format.

The file `mdebugread.c' implements reading for this format.

### [DWARF 1](GDB%20Internals.md#apple-krhugnju)

DWARF 1 is a debugging format that was originally designed to be
used with ELF in SVR4 systems.

The DWARF 1 reader is in `dwarfread.c'.

### [DWARF 2](GDB%20Internals.md#apple-krhugnjv)

DWARF 2 is an improved but incompatible version of DWARF 1.

The DWARF 2 reader is in `dwarf2read.c'.

### [SOM](GDB%20Internals.md#apple-krhugnjw)

Like COFF, the SOM definition includes debugging information.

## [Adding a New Symbol Reader to GDB](GDB%20Internals.md#apple-krhugnjx)

If you are using an existing object file format (`a.out`, COFF, ELF, etc),
there is probably little to be done.

If you need to add a new object file format, you must first add it to
BFD. This is beyond the scope of this document.

You must then arrange for the BFD code to provide access to the
debugging symbols. Generally GDB will have to call swapping routines
from BFD and a few other BFD internal routines to locate the debugging
information. As much as possible, GDB should not depend on the BFD
internal data structures.

For some targets (e.g., COFF), there is a special transfer vector used
to call swapping routines, since the external data structures on various
platforms have different sizes and layouts. Specialized routines that
will only ever be implemented by one object file format may be called
directly. This interface should be described in a file
`bfd/libxyz.h', which is included by GDB.

---

Go to the [first](Requirements.md), [previous](libgdb.md), [next](Language%20Support.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
