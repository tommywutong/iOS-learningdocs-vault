---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_9.html
archived_at: '2026-07-15T07:31:03.894007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Host%20Definition.md), [next](Target%20Vector%20Definition.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Target Architecture Definition](GDB%20Internals.md#apple-krhugnrt)

GDB's target architecture defines what sort of
machine-language programs GDB can work with, and how it works
with them.

The target architecture object is implemented as the C structure
`struct gdbarch *`. The structure, and its methods, are generated
using the Bourne shell script `gdbarch.sh'.

## [Operating System ABI Variant Handling](GDB%20Internals.md#apple-krhugnru)

GDB provides a mechanism for handling variations in OS
ABIs. An OS ABI variant may have influence over any number of
variables in the target architecture definition. There are two major
components in the OS ABI mechanism: sniffers and handlers.

A __sniffer__ examines a file matching a BFD architecture/flavour pair
(the architecture may be wildcarded) in an attempt to determine the
OS ABI of that file. Sniffers with a wildcarded architecture are considered
to be __generic__, while sniffers for a specific architecture are
considered to be __specific__. A match from a specific sniffer
overrides a match from a generic sniffer. Multiple sniffers for an
architecture/flavour may exist, in order to differentiate between two
different operating systems which use the same basic file format. The
OS ABI framework provides a generic sniffer for ELF-format files which
examines the `EI_OSABI` field of the ELF header, as well as note
sections known to be used by several operating systems.

A __handler__ is used to fine-tune the `gdbarch` structure for the
selected OS ABI. There may be only one handler for a given OS ABI
for each BFD architecture.

The following OS ABI variants are defined in `osabi.h':

**`GDB_OSABI_UNKNOWN`**
: 
The ABI of the inferior is unknown. The default `gdbarch`
settings for the architecture will be used.

**`GDB_OSABI_SVR4`**
: UNIX System V Release 4

**`GDB_OSABI_HURD`**
: GNU using the Hurd kernel

**`GDB_OSABI_SOLARIS`**
: Sun Solaris

**`GDB_OSABI_OSF1`**
: OSF/1, including Digital UNIX and Compaq Tru64 UNIX

**`GDB_OSABI_LINUX`**
: GNU using the Linux kernel

**`GDB_OSABI_FREEBSD_AOUT`**
: FreeBSD using the a.out executable format

**`GDB_OSABI_FREEBSD_ELF`**
: FreeBSD using the ELF executable format

**`GDB_OSABI_NETBSD_AOUT`**
: NetBSD using the a.out executable format

**`GDB_OSABI_NETBSD_ELF`**
: NetBSD using the ELF executable format

**`GDB_OSABI_WINCE`**
: Windows CE

**`GDB_OSABI_GO32`**
: DJGPP

**`GDB_OSABI_NETWARE`**
: Novell NetWare

**`GDB_OSABI_ARM_EABI_V1`**
: ARM Embedded ABI version 1

**`GDB_OSABI_ARM_EABI_V2`**
: ARM Embedded ABI version 2

**`GDB_OSABI_ARM_APCS`**
: Generic ARM Procedure Call Standard

Here are the functions that make up the OS ABI framework:

**Function: const __char__ _\*gdbarch_osabi_name (enum gdb_osabi osabi)_**
: 
Return the name of the OS ABI corresponding to osabi.

**Function: void __gdbarch_register_osabi__ _(enum bfd_architecture arch, unsigned long machine, enum gdb_osabi osabi, void (\*init_osabi)(struct gdbarch_info info, struct gdbarch \*gdbarch))_**
: 
Register the OS ABI handler specified by init_osabi for the
architecture, machine type and OS ABI specified by arch,
machine and osabi. In most cases, a value of zero for the
machine type, which implies the architecture's default machine type,
will suffice.

**Function: void __gdbarch_register_osabi_sniffer__ _(enum bfd_architecture arch, enum bfd_flavour flavour, enum gdb_osabi (\*sniffer)(bfd \*abfd))_**
: 
Register the OS ABI file sniffer specified by sniffer for the
BFD architecture/flavour pair specified by arch and flavour.
If arch is `bfd_arch_unknown`, the sniffer is considered to
be generic, and is allowed to examine flavour-flavoured files for
any architecture.

**Function: enum __gdb_osabi__ _gdbarch_lookup_osabi (bfd \*abfd)_**
: 
Examine the file described by abfd to determine its OS ABI.
The value `GDB_OSABI_UNKNOWN` is returned if the OS ABI cannot
be determined.

**Function: void __gdbarch_init_osabi__ _(struct gdbarch info info, struct gdbarch \*gdbarch, enum gdb_osabi osabi)_**
: 
Invoke the OS ABI handler corresponding to osabi to fine-tune the
`gdbarch` structure specified by gdbarch. If a handler
corresponding to osabi has not been registered for gdbarch's
architecture, a warning will be issued and the debugging session will continue
with the defaults already established for gdbarch.

## [Registers and Memory](GDB%20Internals.md#apple-krhugnrv)

GDB's model of the target machine is rather simple.
GDB assumes the machine includes a bank of registers and a
block of memory. Each register may have a different size.

GDB does not have a magical way to match up with the
compiler's idea of which registers are which; however, it is critical
that they do match up accurately. The only way to make this work is
to get accurate information about the order that the compiler uses,
and to reflect that in the `REGISTER_NAME` and related macros.

GDB can handle big-endian, little-endian, and bi-endian architectures.

## [Pointers Are Not Always Addresses](GDB%20Internals.md#apple-krhugnrw)

On almost all 32-bit architectures, the representation of a pointer is
indistinguishable from the representation of some fixed-length number
whose value is the byte address of the object pointed to. On such
machines, the words "pointer" and "address" can be used interchangeably.
However, architectures with smaller word sizes are often cramped for
address space, so they may choose a pointer representation that breaks this
identity, and allows a larger code address space.

For example, the Renesas D10V is a 16-bit VLIW processor whose
instructions are 32 bits long[(3)](GDB%20Internals-2.md#apple-izhu6vbt).
If the D10V used ordinary byte addresses to refer to code locations,
then the processor would only be able to address 64kb of instructions.
However, since instructions must be aligned on four-byte boundaries, the
low two bits of any valid instruction's byte address are always
zero--byte addresses waste two bits. So instead of byte addresses,
the D10V uses word addresses--byte addresses shifted right two bits--to
refer to code. Thus, the D10V can use 16-bit words to address 256kb of
code space.

However, this means that code pointers and data pointers have different
forms on the D10V. The 16-bit word `0xC020` refers to byte address
`0xC020` when used as a data address, but refers to byte address
`0x30080` when used as a code address.

(The D10V also uses separate code and data address spaces, which also
affects the correspondence between pointers and addresses, but we're
going to ignore that here; this example is already too long.)

To cope with architectures like this--the D10V is not the only
one!---GDB tries to distinguish between __addresses__, which are
byte numbers, and __pointers__, which are the target's representation
of an address of a particular type of data. In the example above,
`0xC020` is the pointer, which refers to one of the addresses
`0xC020` or `0x30080`, depending on the type imposed upon it.
GDB provides functions for turning a pointer into an address
and vice versa, in the appropriate way for the current architecture.

Unfortunately, since addresses and pointers are identical on almost all
processors, this distinction tends to bit-rot pretty quickly. Thus,
each time you port GDB to an architecture which does
distinguish between pointers and addresses, you'll probably need to
clean up some architecture-independent code.

Here are functions which convert between pointers and addresses:

**Function: CORE_ADDR __extract_typed_address__ _(void \*buf, struct type \*type)_**
: 
Treat the bytes at buf as a pointer or reference of type
type, and return the address it represents, in a manner
appropriate for the current architecture. This yields an address
GDB can use to read target memory, disassemble, etc. Note that
buf refers to a buffer in GDB's memory, not the
inferior's.

For example, if the current architecture is the Intel x86, this function
extracts a little-endian integer of the appropriate length from
buf and returns it. However, if the current architecture is the
D10V, this function will return a 16-bit integer extracted from
buf, multiplied by four if type is a pointer to a function.

If type is not a pointer or reference type, then this function
will signal an internal error.

**Function: CORE_ADDR __store_typed_address__ _(void \*buf, struct type \*type, CORE_ADDR addr)_**
: 
Store the address addr in buf, in the proper format for a
pointer of type type in the current architecture. Note that
buf refers to a buffer in GDB's memory, not the
inferior's.

For example, if the current architecture is the Intel x86, this function
stores addr unmodified as a little-endian integer of the
appropriate length in buf. However, if the current architecture
is the D10V, this function divides addr by four if type is
a pointer to a function, and then stores it in buf.

If type is not a pointer or reference type, then this function
will signal an internal error.

**Function: CORE_ADDR __value_as_address__ _(struct value \*val)_**
: 
Assuming that val is a pointer, return the address it represents,
as appropriate for the current architecture.

This function actually works on integral values, as well as pointers.
For pointers, it performs architecture-specific conversions as
described above for `extract_typed_address`.

**Function: CORE_ADDR __value_from_pointer__ _(struct type \*type, CORE_ADDR addr)_**
: 
Create and return a value representing a pointer of type type to
the address addr, as appropriate for the current architecture.
This function performs architecture-specific conversions as described
above for `store_typed_address`.

Here are some macros which architectures can define to indicate the
relationship between pointers and addresses. These have default
definitions, appropriate for architectures on which all pointers are
simple unsigned byte addresses.

**Target Macro: CORE_ADDR __POINTER_TO_ADDRESS__ _(struct type \*type, char \*buf)_**
: 
Assume that buf holds a pointer of type type, in the
appropriate format for the current architecture. Return the byte
address the pointer refers to.

This function may safely assume that type is either a pointer or a
C++ reference type.

**Target Macro: void __ADDRESS_TO_POINTER__ _(struct type \*type, char \*buf, CORE_ADDR addr)_**
: 
Store in buf a pointer of type type representing the address
addr, in the appropriate format for the current architecture.

This function may safely assume that type is either a pointer or a
C++ reference type.

## [Address Classes](GDB%20Internals.md#apple-krhugnrx)

Sometimes information about different kinds of addresses is available
via the debug information. For example, some programming environments
define addresses of several different sizes. If the debug information
distinguishes these kinds of address classes through either the size
info (e.g, `DW_AT_byte_size` in DWARF 2) or through an explicit
address class attribute (e.g, `DW_AT_address_class` in DWARF 2), the
following macros should be defined in order to disambiguate these
types within GDB as well as provide the added information to
a GDB user when printing type expressions.

**Target Macro: int __ADDRESS_CLASS_TYPE_FLAGS__ _(int byte_size, int dwarf2_addr_class)_**
: 
Returns the type flags needed to construct a pointer type whose size
is byte_size and whose address class is dwarf2_addr_class.
This function is normally called from within a symbol reader. See
`dwarf2read.c'.

**Target Macro: char __\*ADDRESS_CLASS_TYPE_FLAGS_TO_NAME__ _(int type_flags)_**
: 
Given the type flags representing an address class qualifier, return
its name.

**Target Macro: int __ADDRESS_CLASS_NAME_to_TYPE_FLAGS__ _(int name, int \*var{type_flags_ptr})_**
: 
Given an address qualifier name, set the `int` refererenced by type_flags_ptr to the type flags
for that address class qualifier.

Since the need for address classes is rather rare, none of
the address class macros defined by default. Predicate
macros are provided to detect when they are defined.

Consider a hypothetical architecture in which addresses are normally
32-bits wide, but 16-bit addresses are also supported. Furthermore,
suppose that the DWARF 2 information for this architecture simply
uses a `DW_AT_byte_size` value of 2 to indicate the use of one
of these "short" pointers. The following functions could be defined
to implement the address class macros:

```
somearch_address_class_type_flags (int byte_size,
                                   int dwarf2_addr_class)
{
  if (byte_size == 2)
    return TYPE_FLAG_ADDRESS_CLASS_1;
  else
    return 0;
}

static char *
somearch_address_class_type_flags_to_name (int type_flags)
{
  if (type_flags & TYPE_FLAG_ADDRESS_CLASS_1)
    return "short";
  else
    return NULL;
}

int
somearch_address_class_name_to_type_flags (char *name,
                                           int *type_flags_ptr)
{
  if (strcmp (name, "short") == 0)
    {
      *type_flags_ptr = TYPE_FLAG_ADDRESS_CLASS_1;
      return 1;
    }
  else
    return 0;
}
```

The qualifier `@short` is used in GDB's type expressions
to indicate the presence of one of these "short" pointers. E.g, if
the debug information indicates that `short_ptr_var` is one of these
short pointers, GDB might show the following behavior:

```
(gdb) ptype short_ptr_var
type = int * @short
```

## [Raw and Virtual Register Representations](GDB%20Internals.md#apple-krhugnry)

_Maintainer note: This section is pretty much obsolete. The
functionality described here has largely been replaced by
pseudo-registers and the mechanisms described in section [Target Architecture Definition](#apple-kncugnrt). See also @uref{http://www.gnu.org/software/gdb/bugs/,
Bug Tracking Database_ and
@uref{http://sources.redhat.com/gdb/current/ari/, ARI Index} for more
up-to-date information.}

Some architectures use one representation for a value when it lives in a
register, but use a different representation when it lives in memory.
In GDB's terminology, the __raw__ representation is the one used in
the target registers, and the __virtual__ representation is the one
used in memory, and within GDB `struct value` objects.

_Maintainer note: Notice that the same mechanism is being used to
both convert a register to a `struct value` and alternative
register forms._

For almost all data types on almost all architectures, the virtual and
raw representations are identical, and no special handling is needed.
However, they do occasionally differ. For example:

- The x86 architecture supports an 80-bit `long double` type. However, when
  we store those values in memory, they occupy twelve bytes: the
  floating-point number occupies the first ten, and the final two bytes
  are unused. This keeps the values aligned on four-byte boundaries,
  allowing more efficient access. Thus, the x86 80-bit floating-point
  type is the raw representation, and the twelve-byte loosely-packed
  arrangement is the virtual representation.
- Some 64-bit MIPS targets present 32-bit registers to GDB as 64-bit
  registers, with garbage in their upper bits. GDB ignores the top 32
  bits. Thus, the 64-bit form, with garbage in the upper 32 bits, is the
  raw representation, and the trimmed 32-bit representation is the
  virtual representation.

In general, the raw representation is determined by the architecture, or
GDB's interface to the architecture, while the virtual representation
can be chosen for GDB's convenience. GDB's register file,
`registers`, holds the register contents in raw format, and the
GDB remote protocol transmits register values in raw format.

Your architecture may define the following macros to request
conversions between the raw and virtual format:

**Target Macro: int __REGISTER_CONVERTIBLE__ _(int reg)_**
: 
Return non-zero if register number reg's value needs different raw
and virtual formats.

You should not use `REGISTER_CONVERT_TO_VIRTUAL` for a register
unless this macro returns a non-zero value for that register.

**Target Macro: int __DEPRECATED_REGISTER_RAW_SIZE__ _(int reg)_**
: 
The size of register number reg's raw value. This is the number
of bytes the register will occupy in `registers`, or in a GDB
remote protocol packet.

**Target Macro: int __DEPRECATED_REGISTER_VIRTUAL_SIZE__ _(int reg)_**
: 
The size of register number reg's value, in its virtual format.
This is the size a `struct value`'s buffer will have, holding that
register's value.

**Target Macro: struct __type__ _\*DEPRECATED_REGISTER_VIRTUAL_TYPE (int reg)_**
: 
This is the type of the virtual representation of register number
reg. Note that there is no need for a macro giving a type for the
register's raw form; once the register's value has been obtained, GDB
always uses the virtual form.

**Target Macro: void __REGISTER_CONVERT_TO_VIRTUAL__ _(int reg, struct type \*type, char \*from, char \*to)_**
: 
Convert the value of register number reg to type, which
should always be `DEPRECATED_REGISTER_VIRTUAL_TYPE (reg)`. The buffer
at from holds the register's value in raw format; the macro should
convert the value to virtual format, and place it at to.

Note that `REGISTER_CONVERT_TO_VIRTUAL` and
`REGISTER_CONVERT_TO_RAW` take their reg and type
arguments in different orders.

You should only use `REGISTER_CONVERT_TO_VIRTUAL` with registers
for which the `REGISTER_CONVERTIBLE` macro returns a non-zero
value.

**Target Macro: void __REGISTER_CONVERT_TO_RAW__ _(struct type \*type, int reg, char \*from, char \*to)_**
: 
Convert the value of register number reg to type, which
should always be `DEPRECATED_REGISTER_VIRTUAL_TYPE (reg)`. The buffer
at from holds the register's value in raw format; the macro should
convert the value to virtual format, and place it at to.

Note that REGISTER_CONVERT_TO_VIRTUAL and REGISTER_CONVERT_TO_RAW take
their reg and type arguments in different orders.

## [Using Different Register and Memory Data Representations](GDB%20Internals.md#apple-krhugnrz)

_Maintainer's note: The way GDB manipulates registers is undergoing
significant change. Many of the macros and functions refered to in this
section are likely to be subject to further revision. See
@uref{http://sources.redhat.com/gdb/current/ari/, A.R. Index_ and
@uref{http://www.gnu.org/software/gdb/bugs, Bug Tracking Database} for
further information. cagney/2002-05-06.}

Some architectures can represent a data object in a register using a
form that is different to the objects more normal memory representation.
For example:

- The Alpha architecture can represent 32 bit integer values in
  floating-point registers.
- The x86 architecture supports 80-bit floating-point registers. The
  `long double` data type occupies 96 bits in memory but only 80 bits
  when stored in a register.

In general, the register representation of a data type is determined by
the architecture, or GDB's interface to the architecture, while
the memory representation is determined by the Application Binary
Interface.

For almost all data types on almost all architectures, the two
representations are identical, and no special handling is needed.
However, they do occasionally differ. Your architecture may define the
following macros to request conversions between the register and memory
representations of a data type:

**Target Macro: int __CONVERT_REGISTER_P__ _(int reg)_**
: 
Return non-zero if the representation of a data value stored in this
register may be different to the representation of that same data value
when stored in memory.

When non-zero, the macros `REGISTER_TO_VALUE` and
`VALUE_TO_REGISTER` are used to perform any necessary conversion.

**Target Macro: void __REGISTER_TO_VALUE__ _(int reg, struct type \*type, char \*from, char \*to)_**
: 
Convert the value of register number reg to a data object of type
type. The buffer at from holds the register's value in raw
format; the converted value should be placed in the buffer at to.

Note that `REGISTER_TO_VALUE` and `VALUE_TO_REGISTER` take
their reg and type arguments in different orders.

You should only use `REGISTER_TO_VALUE` with registers for which
the `CONVERT_REGISTER_P` macro returns a non-zero value.

**Target Macro: void __VALUE_TO_REGISTER__ _(struct type \*type, int reg, char \*from, char \*to)_**
: 
Convert a data value of type type to register number reg'
raw format.

Note that `REGISTER_TO_VALUE` and `VALUE_TO_REGISTER` take
their reg and type arguments in different orders.

You should only use `VALUE_TO_REGISTER` with registers for which
the `CONVERT_REGISTER_P` macro returns a non-zero value.

**Target Macro: void __REGISTER_CONVERT_TO_TYPE__ _(int regnum, struct type \*type, char \*buf)_**
: 
See `mips-tdep.c'. It does not do what you want.

## [Frame Interpretation](GDB%20Internals.md#apple-krhugnzq)

## [Inferior Call Setup](GDB%20Internals.md#apple-krhugnzr)

## [Compiler Characteristics](GDB%20Internals.md#apple-krhugnzs)

## [Target Conditionals](GDB%20Internals.md#apple-krhugnzt)

This section describes the macros that you can use to define the target
machine.

**`ADDR_BITS_REMOVE (addr)`**
: 
If a raw machine instruction address includes any bits that are not
really part of the address, then define this macro to expand into an
expression that zeroes those bits in addr. This is only used for
addresses of instructions, and even then not in all contexts.
For example, the two low-order bits of the PC on the Hewlett-Packard PA
2.0 architecture contain the privilege level of the corresponding
instruction. Since instructions must always be aligned on four-byte
boundaries, the processor masks out these bits to generate the actual
address of the instruction. ADDR_BITS_REMOVE should filter out these
bits with an expression such as `((addr) & ~3)`.

**`ADDRESS_CLASS_NAME_TO_TYPE_FLAGS (name, type_flags_ptr)`**
: 
If name is a valid address class qualifier name, set the `int`
referenced by type_flags_ptr to the mask representing the qualifier
and return 1. If name is not a valid address class qualifier name,
return 0.
The value for type_flags_ptr should be one of
`TYPE_FLAG_ADDRESS_CLASS_1`, `TYPE_FLAG_ADDRESS_CLASS_2`, or
possibly some combination of these values or'd together.
See section [Target Architecture Definition](#apple-kncugnrt).

**`ADDRESS_CLASS_NAME_TO_TYPE_FLAGS_P ()`**
: 
Predicate which indicates whether `ADDRESS_CLASS_NAME_TO_TYPE_FLAGS`
has been defined.

**`ADDRESS_CLASS_TYPE_FLAGS (byte_size, dwarf2_addr_class)`**
: 
Given a pointers byte size (as described by the debug information) and
the possible `DW_AT_address_class` value, return the type flags
used by GDB to represent this address class. The value
returned should be one of `TYPE_FLAG_ADDRESS_CLASS_1`,
`TYPE_FLAG_ADDRESS_CLASS_2`, or possibly some combination of these
values or'd together.
See section [Target Architecture Definition](#apple-kncugnrt).

**`ADDRESS_CLASS_TYPE_FLAGS_P ()`**
: 
Predicate which indicates whether `ADDRESS_CLASS_TYPE_FLAGS` has
been defined.

**`ADDRESS_CLASS_TYPE_FLAGS_TO_NAME (type_flags)`**
: 
Return the name of the address class qualifier associated with the type
flags given by type_flags.

**`ADDRESS_CLASS_TYPE_FLAGS_TO_NAME_P ()`**
: 
Predicate which indicates whether `ADDRESS_CLASS_TYPE_FLAGS_TO_NAME` has
been defined.
See section [Target Architecture Definition](#apple-kncugnrt).

**`ADDRESS_TO_POINTER (type, buf, addr)`**
: 
Store in buf a pointer of type type representing the address
addr, in the appropriate format for the current architecture.
This macro may safely assume that type is either a pointer or a
C++ reference type.
See section [Target Architecture Definition](#apple-kncugnrt).

**`BELIEVE_PCC_PROMOTION`**
: 
Define if the compiler promotes a `short` or `char`
parameter to an `int`, but still reports the parameter as its
original type, rather than the promoted type.

**`BITS_BIG_ENDIAN`**
: 
Define this if the numbering of bits in the targets does __not__ match the
endianness of the target byte order. A value of 1 means that the bits
are numbered in a big-endian bit order, 0 means little-endian.

**`BREAKPOINT`**
: 
This is the character array initializer for the bit pattern to put into
memory where a breakpoint is set. Although it's common to use a trap
instruction for a breakpoint, it's not required; for instance, the bit
pattern could be an invalid instruction. The breakpoint must be no
longer than the shortest instruction of the architecture.
`BREAKPOINT` has been deprecated in favor of
`BREAKPOINT_FROM_PC`.

**`BIG_BREAKPOINT`**
:

**`LITTLE_BREAKPOINT`**
: 

Similar to BREAKPOINT, but used for bi-endian targets.
`BIG_BREAKPOINT` and `LITTLE_BREAKPOINT` have been deprecated in
favor of `BREAKPOINT_FROM_PC`.

**`DEPRECATED_REMOTE_BREAKPOINT`**
:

**`DEPRECATED_LITTLE_REMOTE_BREAKPOINT`**
:

**`DEPRECATED_BIG_REMOTE_BREAKPOINT`**
: 

Specify the breakpoint instruction sequence for a remote target.
`DEPRECATED_REMOTE_BREAKPOINT`,
`DEPRECATED_BIG_REMOTE_BREAKPOINT` and
`DEPRECATED_LITTLE_REMOTE_BREAKPOINT` have been deprecated in
favor of `BREAKPOINT_FROM_PC` (@xref{BREAKPOINT_FROM_PC}).

**`BREAKPOINT_FROM_PC (pcptr, lenptr)`**
: 
@anchor{BREAKPOINT_FROM_PC} Use the program counter to determine the
contents and size of a breakpoint instruction. It returns a pointer to
a string of bytes that encode a breakpoint instruction, stores the
length of the string to `*lenptr`, and adjusts the program
counter (if necessary) to point to the actual memory location where the
breakpoint should be inserted.
Although it is common to use a trap instruction for a breakpoint, it's
not required; for instance, the bit pattern could be an invalid
instruction. The breakpoint must be no longer than the shortest
instruction of the architecture.
Replaces all the other BREAKPOINT macros.

**`MEMORY_INSERT_BREAKPOINT (addr, contents_cache)`**
:

**`MEMORY_REMOVE_BREAKPOINT (addr, contents_cache)`**
: 

Insert or remove memory based breakpoints. Reasonable defaults
(`default_memory_insert_breakpoint` and
`default_memory_remove_breakpoint` respectively) have been
provided so that it is not necessary to define these for most
architectures. Architectures which may want to define
`MEMORY_INSERT_BREAKPOINT` and `MEMORY_REMOVE_BREAKPOINT` will
likely have instructions that are oddly sized or are not stored in a
conventional manner.
It may also be desirable (from an efficiency standpoint) to define
custom breakpoint insertion and removal routines if
`BREAKPOINT_FROM_PC` needs to read the target's memory for some
reason.

**`ADJUST_BREAKPOINT_ADDRESS (address)`**
: 

Given an address at which a breakpoint is desired, return a breakpoint
address adjusted to account for architectural constraints on
breakpoint placement. This method is not needed by most targets.
The FR-V target (see `frv-tdep.c') requires this method.
The FR-V is a VLIW architecture in which a number of RISC-like
instructions are grouped (packed) together into an aggregate
instruction or instruction bundle. When the processor executes
one of these bundles, the component instructions are executed
in parallel.
In the course of optimization, the compiler may group instructions
from distinct source statements into the same bundle. The line number
information associated with one of the latter statements will likely
refer to some instruction other than the first one in the bundle. So,
if the user attempts to place a breakpoint on one of these latter
statements, GDB must be careful to _not_ place the break
instruction on any instruction other than the first one in the bundle.
(Remember though that the instructions within a bundle execute
in parallel, so the _first_ instruction is the instruction
at the lowest address and has nothing to do with execution order.)
The FR-V's `ADJUST_BREAKPOINT_ADDRESS` method will adjust a
breakpoint's address by scanning backwards for the beginning of
the bundle, returning the address of the bundle.
Since the adjustment of a breakpoint may significantly alter a user's
expectation, GDB prints a warning when an adjusted breakpoint
is initially set and each time that that breakpoint is hit.

**`CALL_DUMMY_LOCATION`**
: 
See the file `inferior.h'.
This method has been replaced by `push_dummy_code`
(@xref{push_dummy_code}).

**`CANNOT_FETCH_REGISTER (regno)`**
: 
A C expression that should be nonzero if regno cannot be fetched
from an inferior process. This is only relevant if
`FETCH_INFERIOR_REGISTERS` is not defined.

**`CANNOT_STORE_REGISTER (regno)`**
: 
A C expression that should be nonzero if regno should not be
written to the target. This is often the case for program counters,
status words, and other special registers. If this is not defined,
GDB will assume that all registers may be written.

**`int CONVERT_REGISTER_P(regnum)`**
: 
Return non-zero if register regnum can represent data values in a
non-standard form.
See section [Target Architecture Definition](#apple-kncugnrt).

**`DECR_PC_AFTER_BREAK`**
: 
Define this to be the amount by which to decrement the PC after the
program encounters a breakpoint. This is often the number of bytes in
`BREAKPOINT`, though not always. For most targets this value will be 0.

**`DISABLE_UNSETTABLE_BREAK (addr)`**
: 
If defined, this should evaluate to 1 if addr is in a shared
library in which breakpoints cannot be set and so should be disabled.

**`PRINT_FLOAT_INFO()`**
: 
If defined, then the `` `info float' `` command will print information about
the processor's floating point unit.

**`print_registers_info (gdbarch, frame, regnum, all)`**
: 
If defined, pretty print the value of the register regnum for the
specified frame. If the value of regnum is -1, pretty print
either all registers (all is non zero) or a select subset of
registers (all is zero).
The default method prints one register per line, and if all is
zero omits floating-point registers.

**`PRINT_VECTOR_INFO()`**
: 
If defined, then the `` `info vector' `` command will call this function
to print information about the processor's vector unit.
By default, the `` `info vector' `` command will print all vector
registers (the register's type having the vector attribute).

**`DWARF_REG_TO_REGNUM`**
: 
Convert DWARF register number into GDB regnum. If not defined,
no conversion will be performed.

**`DWARF2_REG_TO_REGNUM`**
: 
Convert DWARF2 register number into GDB regnum. If not
defined, no conversion will be performed.

**`ECOFF_REG_TO_REGNUM`**
: 
Convert ECOFF register number into GDB regnum. If not defined,
no conversion will be performed.

**`END_OF_TEXT_DEFAULT`**
: 
This is an expression that should designate the end of the text section.

**`EXTRACT_RETURN_VALUE(type, regbuf, valbuf)`**
: 
Define this to extract a function's return value of type type from
the raw register state regbuf and copy that, in virtual format,
into valbuf.
This method has been deprecated in favour of `gdbarch_return_value`
(@xref{gdbarch_return_value}).

**`DEPRECATED_EXTRACT_STRUCT_VALUE_ADDRESS(regbuf)`**
: 
@anchor{DEPRECATED_EXTRACT_STRUCT_VALUE_ADDRESS}
When defined, extract from the array regbuf (containing the raw
register state) the `CORE_ADDR` at which a function should return
its structure value.
@xref{gdbarch_return_value}.

**`DEPRECATED_EXTRACT_STRUCT_VALUE_ADDRESS_P()`**
: 
Predicate for `DEPRECATED_EXTRACT_STRUCT_VALUE_ADDRESS`.

**`DEPRECATED_FP_REGNUM`**
: 
If the virtual frame pointer is kept in a register, then define this
macro to be the number (greater than or equal to zero) of that register.
This should only need to be defined if `DEPRECATED_TARGET_READ_FP`
is not defined.

**`DEPRECATED_FRAMELESS_FUNCTION_INVOCATION(fi)`**
: 
Define this to an expression that returns 1 if the function invocation
represented by fi does not have a stack frame associated with it.
Otherwise return 0.

**`frame_align (address)`**
: @anchor{frame_align}

Define this to adjust address so that it meets the alignment
requirements for the start of a new stack frame. A stack frame's
alignment requirements are typically stronger than a target processors
stack alignment requirements (@xref{DEPRECATED_STACK_ALIGN}).
This function is used to ensure that, when creating a dummy frame, both
the initial stack pointer and (if needed) the address of the return
value are correctly aligned.
Unlike `DEPRECATED_STACK_ALIGN`, this function always adjusts the
address in the direction of stack growth.
By default, no frame based stack alignment is performed.

**`int frame_red_zone_size`**
: The number of bytes, beyond the innermost-stack-address, reserved by the
ABI. A function is permitted to use this scratch area (instead of
allocating extra stack space).
When performing an inferior function call, to ensure that it does not
modify this area, GDB adjusts the innermost-stack-address by
frame_red_zone_size bytes before pushing parameters onto the
stack.
By default, zero bytes are allocated. The value must be aligned
(@xref{frame_align}).
The AMD64 (nee x86-64) ABI documentation refers to the
_red zone_ when describing this scratch area.

**`DEPRECATED_FRAME_CHAIN(frame)`**
: 
Given frame, return a pointer to the calling frame.

**`DEPRECATED_FRAME_CHAIN_VALID(chain, thisframe)`**
: 
Define this to be an expression that returns zero if the given frame is an
outermost frame, with no caller, and nonzero otherwise. Most normal
situations can be handled without defining this macro, including `NULL`
chain pointers, dummy frames, and frames whose PC values are inside the
startup file (e.g. `crt0.o'), inside `main`, or inside
`_start`.

**`DEPRECATED_FRAME_INIT_SAVED_REGS(frame)`**
: 
See `frame.h'. Determines the address of all registers in the
current stack frame storing each in `frame->saved_regs`. Space for
`frame->saved_regs` shall be allocated by
`DEPRECATED_FRAME_INIT_SAVED_REGS` using
`frame_saved_regs_zalloc`.
`FRAME_FIND_SAVED_REGS` is deprecated.

**`FRAME_NUM_ARGS (fi)`**
: 
For the frame described by fi return the number of arguments that
are being passed. If the number of arguments is not known, return
`-1`.

**`DEPRECATED_FRAME_SAVED_PC(frame)`**
: 
@anchor{DEPRECATED_FRAME_SAVED_PC} Given frame, return the pc
saved there. This is the return address.
This method is deprecated. @xref{unwind_pc}.

**`CORE_ADDR unwind_pc (struct frame_info *this_frame)`**
: 
@anchor{unwind_pc} Return the instruction address, in this_frame's
caller, at which execution will resume after this_frame returns.
This is commonly refered to as the return address.
The implementation, which must be frame agnostic (work with any frame),
is typically no more than:

```
ULONGEST pc;
frame_unwind_unsigned_register (this_frame, D10V_PC_REGNUM, &pc);
return d10v_make_iaddr (pc);
```

@xref{DEPRECATED_FRAME_SAVED_PC}, which this method replaces.

**`CORE_ADDR unwind_sp (struct frame_info *this_frame)`**
: 
@anchor{unwind_sp} Return the frame's inner most stack address. This is
commonly refered to as the frame's __stack pointer__.
The implementation, which must be frame agnostic (work with any frame),
is typically no more than:

```
ULONGEST sp;
frame_unwind_unsigned_register (this_frame, D10V_SP_REGNUM, &sp);
return d10v_make_daddr (sp);
```

@xref{TARGET_READ_SP}, which this method replaces.

**`FUNCTION_EPILOGUE_SIZE`**
: 
For some COFF targets, the `x_sym.x_misc.x_fsize` field of the
function end symbol is 0. For such targets, you must define
`FUNCTION_EPILOGUE_SIZE` to expand into the standard size of a
function's epilogue.

**`DEPRECATED_FUNCTION_START_OFFSET`**
: 
An integer, giving the offset in bytes from a function's address (as
used in the values of symbols, function pointers, etc.), and the
function's first genuine instruction.
This is zero on almost all machines: the function's address is usually
the address of its first instruction. However, on the VAX, for
example, each function starts with two bytes containing a bitmask
indicating which registers to save upon entry to the function. The
VAX `call` instructions check this value, and save the
appropriate registers automatically. Thus, since the offset from the
function's address to its first instruction is two bytes,
`DEPRECATED_FUNCTION_START_OFFSET` would be 2 on the VAX.

**`GCC_COMPILED_FLAG_SYMBOL`**
:

**`GCC2_COMPILED_FLAG_SYMBOL`**
: 

If defined, these are the names of the symbols that GDB will
look for to detect that GCC compiled the file. The default symbols
are `gcc_compiled.` and `gcc2_compiled.`,
respectively. (Currently only defined for the Delta 68.)

**`GDB_MULTI_ARCH`**
: 
If defined and non-zero, enables support for multiple architectures
within GDB.
This support can be enabled at two levels. At level one, only
definitions for previously undefined macros are provided; at level two,
a multi-arch definition of all architecture dependent macros will be
defined.

**`GDB_TARGET_IS_HPPA`**
: 
This determines whether horrible kludge code in `dbxread.c' and
`partial-stab.h' is used to mangle multiple-symbol-table files from
HPPA's. This should all be ripped out, and a scheme like `elfread.c'
used instead.

**`GET_LONGJMP_TARGET`**
: 
For most machines, this is a target-dependent parameter. On the
DECstation and the Iris, this is a native-dependent parameter, since
the header file `setjmp.h' is needed to define it.
This macro determines the target PC address that `longjmp` will jump to,
assuming that we have just stopped at a `longjmp` breakpoint. It takes a
`CORE_ADDR *` as argument, and stores the target PC value through this
pointer. It examines the current state of the machine as needed.

**`DEPRECATED_GET_SAVED_REGISTER`**
: 
Define this if you need to supply your own definition for the function
`DEPRECATED_GET_SAVED_REGISTER`.

**`DEPRECATED_IBM6000_TARGET`**
: 
Shows that we are configured for an IBM RS/6000 system. This
conditional should be eliminated (FIXME) and replaced by
feature-specific macros. It was introduced in a haste and we are
repenting at leisure.

**`I386_USE_GENERIC_WATCHPOINTS`**
: An x86-based target can define this to use the generic x86 watchpoint
support; see section [Algorithms](Algorithms.md#apple-kncugnq).

**`SYMBOLS_CAN_START_WITH_DOLLAR`**
: 
Some systems have routines whose names start with `` `$' ``. Giving this
macro a non-zero value tells GDB's expression parser to check for such
routines when parsing tokens that begin with `` `$' ``.
On HP-UX, certain system routines (millicode) have names beginning with
`` `$' `` or `` `$$' ``. For example, `$$dyncall` is a millicode
routine that handles inter-space procedure calls on PA-RISC.

**`DEPRECATED_INIT_EXTRA_FRAME_INFO (fromleaf, frame)`**
: 
If additional information about the frame is required this should be
stored in `frame->extra_info`. Space for `frame->extra_info`
is allocated using `frame_extra_info_zalloc`.

**`DEPRECATED_INIT_FRAME_PC (fromleaf, prev)`**
: 
This is a C statement that sets the pc of the frame pointed to by
prev. [By default...]

**`INNER_THAN (lhs, rhs)`**
: 
Returns non-zero if stack address lhs is inner than (nearer to the
stack top) stack address rhs. Define this as `lhs < rhs` if
the target's stack grows downward in memory, or `lhs > rsh` if the
stack grows upward.

**`gdbarch_in_function_epilogue_p (gdbarch, pc)`**
: 
Returns non-zero if the given pc is in the epilogue of a function.
The epilogue of a function is defined as the part of a function where
the stack frame of the function already has been destroyed up to the
final `return from function call' instruction.

**`DEPRECATED_SIGTRAMP_START (pc)`**
: 

**`DEPRECATED_SIGTRAMP_END (pc)`**
: 
Define these to be the start and end address of the `sigtramp` for the
given pc. On machines where the address is just a compile time
constant, the macro expansion will typically just ignore the supplied
pc.

**`IN_SOLIB_CALL_TRAMPOLINE (pc, name)`**
: 
Define this to evaluate to nonzero if the program is stopped in the
trampoline that connects to a shared library.

**`IN_SOLIB_RETURN_TRAMPOLINE (pc, name)`**
: 
Define this to evaluate to nonzero if the program is stopped in the
trampoline that returns from a shared library.

**`IN_SOLIB_DYNSYM_RESOLVE_CODE (pc)`**
: 
Define this to evaluate to nonzero if the program is stopped in the
dynamic linker.

**`SKIP_SOLIB_RESOLVER (pc)`**
: 
Define this to evaluate to the (nonzero) address at which execution
should continue to get past the dynamic linker's symbol resolution
function. A zero value indicates that it is not important or necessary
to set a breakpoint to get through the dynamic linker and that single
stepping will suffice.

**`INTEGER_TO_ADDRESS (type, buf)`**
: 

Define this when the architecture needs to handle non-pointer to address
conversions specially. Converts that value to an address according to
the current architectures conventions.
_Pragmatics: When the user copies a well defined expression from
their source code and passes it, as a parameter, to GDB's
`print` command, they should get the same value as would have been
computed by the target program. Any deviation from this rule can cause
major confusion and annoyance, and needs to be justified carefully. In
other words, GDB doesn't really have the freedom to do these
conversions in clever and useful ways. It has, however, been pointed
out that users aren't complaining about how GDB casts integers
to pointers; they are complaining that they can't take an address from a
disassembly listing and give it to `x/i`. Adding an architecture
method like `INTEGER_TO_ADDRESS` certainly makes it possible for
GDB to "get it right" in all circumstances._
See section [Target Architecture Definition](#apple-kncugnrt).

**`NO_HIF_SUPPORT`**
: 
(Specific to the a29k.)

**`POINTER_TO_ADDRESS (type, buf)`**
: 
Assume that buf holds a pointer of type type, in the
appropriate format for the current architecture. Return the byte
address the pointer refers to.
See section [Target Architecture Definition](#apple-kncugnrt).

**`REGISTER_CONVERTIBLE (reg)`**
: 
Return non-zero if reg uses different raw and virtual formats.
See section [Target Architecture Definition](#apple-kncugnrt).

**`REGISTER_TO_VALUE(regnum, type, from, to)`**
: 
Convert the raw contents of register regnum into a value of type
type.
See section [Target Architecture Definition](#apple-kncugnrt).

**`DEPRECATED_REGISTER_RAW_SIZE (reg)`**
: 
Return the raw size of reg; defaults to the size of the register's
virtual type.
See section [Target Architecture Definition](#apple-kncugnrt).

**`register_reggroup_p (gdbarch, regnum, reggroup)`**
: 

Return non-zero if register regnum is a member of the register
group reggroup.
By default, registers are grouped as follows:

**`float_reggroup`**
: Any register with a valid name and a floating-point type.

**`vector_reggroup`**
: Any register with a valid name and a vector type.

**`general_reggroup`**
: Any register with a valid name and a type other than vector or
floating-point. `` `float_reggroup' ``.

**`save_reggroup`**
:

**`restore_reggroup`**
:

**`all_reggroup`**
: Any register with a valid name.

**`DEPRECATED_REGISTER_VIRTUAL_SIZE (reg)`**
: 
Return the virtual size of reg; defaults to the size of the
register's virtual type.
Return the virtual size of reg.
See section [Target Architecture Definition](#apple-kncugnrt).

**`DEPRECATED_REGISTER_VIRTUAL_TYPE (reg)`**
: 
Return the virtual type of reg.
See section [Target Architecture Definition](#apple-kncugnrt).

**`struct type *register_type (gdbarch, reg)`**
: 
If defined, return the type of register reg. This function
superseeds `DEPRECATED_REGISTER_VIRTUAL_TYPE`. See section [Target Architecture Definition](#apple-kncugnrt).

**`REGISTER_CONVERT_TO_VIRTUAL(reg, type, from, to)`**
: 
Convert the value of register reg from its raw form to its virtual
form.
See section [Target Architecture Definition](#apple-kncugnrt).

**`REGISTER_CONVERT_TO_RAW(type, reg, from, to)`**
: 
Convert the value of register reg from its virtual form to its raw
form.
See section [Target Architecture Definition](#apple-kncugnrt).

**`const struct regset *regset_from_core_section (struct gdbarch * gdbarch, const char * sect_name, size_t sect_size)`**
: 
Return the appropriate register set for a core file section with name
sect_name and size sect_size.

**`SOFTWARE_SINGLE_STEP_P()`**
: 
Define this as 1 if the target does not have a hardware single-step
mechanism. The macro `SOFTWARE_SINGLE_STEP` must also be defined.

**`SOFTWARE_SINGLE_STEP(signal, insert_breapoints_p)`**
: 
A function that inserts or removes (depending on
insert_breapoints_p) breakpoints at each possible destinations of
the next instruction. See `sparc-tdep.c' and `rs6000-tdep.c'
for examples.

**`SOFUN_ADDRESS_MAYBE_MISSING`**
: 
Somebody clever observed that, the more actual addresses you have in the
debug information, the more time the linker has to spend relocating
them. So whenever there's some other way the debugger could find the
address it needs, you should omit it from the debug info, to make
linking faster.
`SOFUN_ADDRESS_MAYBE_MISSING` indicates that a particular set of
hacks of this sort are in use, affecting `N_SO` and `N_FUN`
entries in stabs-format debugging information. `N_SO` stabs mark
the beginning and ending addresses of compilation units in the text
segment. `N_FUN` stabs mark the starts and ends of functions.
`SOFUN_ADDRESS_MAYBE_MISSING` means two things:

- `N_FUN` stabs have an address of zero. Instead, you should find the
  addresses where the function starts by taking the function name from
  the stab, and then looking that up in the minsyms (the
  linker/assembler symbol table). In other words, the stab has the
  name, and the linker/assembler symbol table is the only place that carries
  the address.
- `N_SO` stabs have an address of zero, too. You just look at the
  `N_FUN` stabs that appear before and after the `N_SO` stab,
  and guess the starting and ending addresses of the compilation unit from
  them.

**`PC_LOAD_SEGMENT`**
: 
If defined, print information about the load segment for the program
counter. (Defined only for the RS/6000.)

**`PC_REGNUM`**
: 
If the program counter is kept in a register, then define this macro to
be the number (greater than or equal to zero) of that register.
This should only need to be defined if `TARGET_READ_PC` and
`TARGET_WRITE_PC` are not defined.

**`PARM_BOUNDARY`**
: 
If non-zero, round arguments to a boundary of this many bits before
pushing them on the stack.

**`stabs_argument_has_addr (gdbarch, type)`**
: 

@anchor{stabs_argument_has_addr} Define this to return nonzero if a
function argument of type type is passed by reference instead of
value.
This method replaces `DEPRECATED_REG_STRUCT_HAS_ADDR`
(@xref{DEPRECATED_REG_STRUCT_HAS_ADDR}).

**`PROCESS_LINENUMBER_HOOK`**
: 
A hook defined for XCOFF reading.

**`PROLOGUE_FIRSTLINE_OVERLAP`**
: 
(Only used in unsupported Convex configuration.)

**`PS_REGNUM`**
: 
If defined, this is the number of the processor status register. (This
definition is only used in generic code when parsing "$ps".)

**`DEPRECATED_POP_FRAME`**
: 

If defined, used by `frame_pop` to remove a stack frame. This
method has been superseeded by generic code.

**`push_dummy_call (gdbarch, function, regcache, pc_addr, nargs, args, sp, struct_return, struct_addr)`**
: 

@anchor{push_dummy_call} Define this to push the dummy frame's call to
the inferior function onto the stack. In addition to pushing
nargs, the code should push struct_addr (when
struct_return), and the return address (bp_addr).
function is a pointer to a `struct value`; on architectures that use
function descriptors, this contains the function descriptor value.
Returns the updated top-of-stack pointer.
This method replaces `DEPRECATED_PUSH_ARGUMENTS`.

**`CORE_ADDR push_dummy_code (gdbarch, sp, funaddr, using_gcc, args, nargs, value_type, real_pc, bp_addr)`**
: 
@anchor{push_dummy_code} Given a stack based call dummy, push the
instruction sequence (including space for a breakpoint) to which the
called function should return.
Set bp_addr to the address at which the breakpoint instruction
should be inserted, real_pc to the resume address when starting
the call sequence, and return the updated inner-most stack address.
By default, the stack is grown sufficient to hold a frame-aligned
(@xref{frame_align}) breakpoint, bp_addr is set to the address
reserved for that breakpoint, and real_pc set to funaddr.
This method replaces `CALL_DUMMY_LOCATION`,
`DEPRECATED_REGISTER_SIZE`.

**`REGISTER_NAME(i)`**
: 
Return the name of register i as a string. May return `NULL`
or `NUL` to indicate that register i is not valid.

**`DEPRECATED_REG_STRUCT_HAS_ADDR (gcc_p, type)`**
: 
@anchor{DEPRECATED_REG_STRUCT_HAS_ADDR}Define this to return 1 if the
given type will be passed by pointer rather than directly.
This method has been replaced by `stabs_argument_has_addr`
(@xref{stabs_argument_has_addr}).

**`SAVE_DUMMY_FRAME_TOS (sp)`**
: 
@anchor{SAVE_DUMMY_FRAME_TOS} Used in `` `call_function_by_hand' `` to
notify the target dependent code of the top-of-stack value that will be
passed to the the inferior code. This is the value of the `SP`
after both the dummy frame and space for parameters/results have been
allocated on the stack. @xref{unwind_dummy_id}.

**`SDB_REG_TO_REGNUM`**
: 
Define this to convert sdb register numbers into GDB regnums. If not
defined, no conversion will be done.

**`enum return_value_convention gdbarch_return_value (struct gdbarch *gdbarch, struct type *valtype, struct regcache *regcache, void *readbuf, const void *writebuf)`**
: 
@anchor{gdbarch_return_value} Given a function with a return-value of
type rettype, return which return-value convention that function
would use.
GDB currently recognizes two function return-value conventions:
`RETURN_VALUE_REGISTER_CONVENTION` where the return value is found
in registers; and `RETURN_VALUE_STRUCT_CONVENTION` where the return
value is found in memory and the address of that memory location is
passed in as the function's first parameter.
If the register convention is being used, and writebuf is
non-`NULL`, also copy the return-value in writebuf into
regcache.
If the register convention is being used, and readbuf is
non-`NULL`, also copy the return value from regcache into
readbuf (regcache contains a copy of the registers from the
just returned function).
@xref{DEPRECATED_EXTRACT_STRUCT_VALUE_ADDRESS}, for a description of how
return-values that use the struct convention are handled.
_Maintainer note: This method replaces separate predicate, extract,
store methods. By having only one method, the logic needed to determine
the return-value convention need only be implemented in one place. If
GDB were written in an OO language, this method would
instead return an object that knew how to perform the register
return-value extract and store._
_Maintainer note: This method does not take a gcc_p
parameter, and such a parameter should not be added. If an architecture
that requires per-compiler or per-function information be identified,
then the replacement of rettype with `struct value`
function should be persued._
_Maintainer note: The regcache parameter limits this methods
to the inner most frame. While replacing regcache with a
`struct frame_info` frame parameter would remove that
limitation there has yet to be a demonstrated need for such a change._

**`SKIP_PERMANENT_BREAKPOINT`**
: 
Advance the inferior's PC past a permanent breakpoint. GDB normally
steps over a breakpoint by removing it, stepping one instruction, and
re-inserting the breakpoint. However, permanent breakpoints are
hardwired into the inferior, and can't be removed, so this strategy
doesn't work. Calling `SKIP_PERMANENT_BREAKPOINT` adjusts the processor's
state so that execution will resume just after the breakpoint. This
macro does the right thing even when the breakpoint is in the delay slot
of a branch or jump.

**`SKIP_PROLOGUE (pc)`**
: 
A C expression that returns the address of the "real" code beyond the
function entry prologue found at pc.

**`SKIP_TRAMPOLINE_CODE (pc)`**
: 
If the target machine has trampoline code that sits between callers and
the functions being called, then define this macro to return a new PC
that is at the start of the real function.

**`SP_REGNUM`**
: 
If the stack-pointer is kept in a register, then define this macro to be
the number (greater than or equal to zero) of that register, or -1 if
there is no such register.

**`STAB_REG_TO_REGNUM`**
: 
Define this to convert stab register numbers (as gotten from `r'
declarations) into GDB regnums. If not defined, no conversion will be
done.

**`DEPRECATED_STACK_ALIGN (addr)`**
: @anchor{DEPRECATED_STACK_ALIGN}

Define this to increase addr so that it meets the alignment
requirements for the processor's stack.
Unlike @xref{frame_align}, this function always adjusts addr
upwards.
By default, no stack alignment is performed.

**`STEP_SKIPS_DELAY (addr)`**
: 
Define this to return true if the address is of an instruction with a
delay slot. If a breakpoint has been placed in the instruction's delay
slot, GDB will single-step over that instruction before resuming
normally. Currently only defined for the Mips.

**`STORE_RETURN_VALUE (type, regcache, valbuf)`**
: 
A C expression that writes the function return value, found in
valbuf, into the regcache. type is the type of the
value that is to be returned.
This method has been deprecated in favour of `gdbarch_return_value`
(@xref{gdbarch_return_value}).

**`SYMBOL_RELOADING_DEFAULT`**
: 
The default value of the "symbol-reloading" variable. (Never defined in
current sources.)

**`TARGET_CHAR_BIT`**
: 
Number of bits in a char; defaults to 8.

**`TARGET_CHAR_SIGNED`**
: 
Non-zero if `char` is normally signed on this architecture; zero if
it should be unsigned.
The ISO C standard requires the compiler to treat `char` as
equivalent to either `signed char` or `unsigned char`; any
character in the standard execution set is supposed to be positive.
Most compilers treat `char` as signed, but `char` is unsigned
on the IBM S/390, RS6000, and PowerPC targets.

**`TARGET_COMPLEX_BIT`**
: 
Number of bits in a complex number; defaults to `2 * TARGET_FLOAT_BIT`.
At present this macro is not used.

**`TARGET_DOUBLE_BIT`**
: 
Number of bits in a double float; defaults to `8 * TARGET_CHAR_BIT`.

**`TARGET_DOUBLE_COMPLEX_BIT`**
: 
Number of bits in a double complex; defaults to `2 * TARGET_DOUBLE_BIT`.
At present this macro is not used.

**`TARGET_FLOAT_BIT`**
: 
Number of bits in a float; defaults to `4 * TARGET_CHAR_BIT`.

**`TARGET_INT_BIT`**
: 
Number of bits in an integer; defaults to `4 * TARGET_CHAR_BIT`.

**`TARGET_LONG_BIT`**
: 
Number of bits in a long integer; defaults to `4 * TARGET_CHAR_BIT`.

**`TARGET_LONG_DOUBLE_BIT`**
: 
Number of bits in a long double float;
defaults to `2 * TARGET_DOUBLE_BIT`.

**`TARGET_LONG_LONG_BIT`**
: 
Number of bits in a long long integer; defaults to `2 * TARGET_LONG_BIT`.

**`TARGET_PTR_BIT`**
: 
Number of bits in a pointer; defaults to `TARGET_INT_BIT`.

**`TARGET_SHORT_BIT`**
: 
Number of bits in a short integer; defaults to `2 * TARGET_CHAR_BIT`.

**`TARGET_READ_PC`**
: 

**`TARGET_WRITE_PC (val, pid)`**
: 
@anchor{TARGET_WRITE_PC}

**`TARGET_READ_SP`**
: 

**`TARGET_READ_FP`**
: 

@anchor{TARGET_READ_SP} These change the behavior of `read_pc`,
`write_pc`, and `read_sp`. For most targets, these may be
left undefined. GDB will call the read and write register
functions with the relevant `_REGNUM` argument.
These macros are useful when a target keeps one of these registers in a
hard to get at place; for example, part in a segment register and part
in an ordinary register.
@xref{unwind_sp}, which replaces `TARGET_READ_SP`.

**`TARGET_VIRTUAL_FRAME_POINTER(pc, regp, offsetp)`**
: 
Returns a `(register, offset)` pair representing the virtual frame
pointer in use at the code address pc. If virtual frame pointers
are not used, a default definition simply returns
`DEPRECATED_FP_REGNUM`, with an offset of zero.

**`TARGET_HAS_HARDWARE_WATCHPOINTS`**
: If non-zero, the target has support for hardware-assisted
watchpoints. See section [Algorithms](Algorithms.md#apple-kncugnq), for more details and
other related macros.

**`TARGET_PRINT_INSN (addr, info)`**
: 
This is the function used by GDB to print an assembly
instruction. It prints the instruction at address addr in
debugged memory and returns the length of the instruction, in bytes. If
a target doesn't define its own printing routine, it defaults to an
accessor function for the global pointer
`deprecated_tm_print_insn`. This usually points to a function in
the `opcodes` library (see section [Support Libraries](Support%20Libraries.md#apple-kncugojy)).
info is a structure (of type `disassemble_info`) defined in
`include/dis-asm.h' used to pass information to the instruction
decoding routine.

**`struct frame_id unwind_dummy_id (struct frame_info *frame)`**
: 
@anchor{unwind_dummy_id} Given frame return a @code{struct
frame_id} that uniquely identifies an inferior function call's dummy
frame. The value returned must match the dummy frame stack value
previously saved using `SAVE_DUMMY_FRAME_TOS`.
@xref{SAVE_DUMMY_FRAME_TOS}.

**`DEPRECATED_USE_STRUCT_CONVENTION (gcc_p, type)`**
: 
If defined, this must be an expression that is nonzero if a value of the
given type being returned from a function must have space
allocated for it on the stack. gcc_p is true if the function
being considered is known to have been compiled by GCC; this is helpful
for systems where GCC is known to use different calling convention than
other compilers.
This method has been deprecated in favour of `gdbarch_return_value`
(@xref{gdbarch_return_value}).

**`VALUE_TO_REGISTER(type, regnum, from, to)`**
: 
Convert a value of type type into the raw contents of register
regnum's.
See section [Target Architecture Definition](#apple-kncugnrt).

**`VARIABLES_INSIDE_BLOCK (desc, gcc_p)`**
: 
For dbx-style debugging information, if the compiler puts variable
declarations inside LBRAC/RBRAC blocks, this should be defined to be
nonzero. desc is the value of `n_desc` from the
`N_RBRAC` symbol, and gcc_p is true if GDB has noticed the
presence of either the `GCC_COMPILED_SYMBOL` or the
`GCC2_COMPILED_SYMBOL`. By default, this is 0.

**`OS9K_VARIABLES_INSIDE_BLOCK (desc, gcc_p)`**
: 
Similarly, for OS/9000. Defaults to 1.

Motorola M68K target conditionals.

**`BPT_VECTOR`**
: 
Define this to be the 4-bit location of the breakpoint trap vector. If
not defined, it will default to `0xf`.

**`REMOTE_BPT_VECTOR`**
: 
Defaults to `1`.

**`NAME_OF_MALLOC`**
: 

A string containing the name of the function to call in order to
allocate some memory in the inferior. The default value is "malloc".

## [Adding a New Target](GDB%20Internals.md#apple-krhugnzu)

The following files add a target to GDB:

**`gdb/config/arch/ttt.mt'**
: 
Contains a Makefile fragment specific to this target. Specifies what
object files are needed for target ttt, by defining
`` `TDEPFILES=...' `` and `` `TDEPLIBS=...' ``. Also specifies
the header file which describes ttt, by defining `` `TM_FILE=
tm-ttt.h' ``.
You can also define `` `TM_CFLAGS' ``, `` `TM_CLIBS' ``, `` `TM_CDEPS' ``,
but these are now deprecated, replaced by autoconf, and may go away in
future versions of GDB.

**`gdb/ttt-tdep.c'**
: Contains any miscellaneous code required for this target machine. On
some machines it doesn't exist at all. Sometimes the macros in
`tm-ttt.h' become very complicated, so they are implemented
as functions here instead, and the macro is simply defined to call the
function. This is vastly preferable, since it is easier to understand
and debug.

**`gdb/arch-tdep.c'**
:

**`gdb/arch-tdep.h'**
: This often exists to describe the basic layout of the target machine's
processor chip (registers, stack, etc.). If used, it is included by
`ttt-tdep.h'. It can be shared among many targets that use
the same processor.

**`gdb/config/arch/tm-ttt.h'**
: (`tm.h' is a link to this file, created by `configure`). Contains
macro definitions about the target machine's registers, stack frame
format and instructions.
New targets do not need this file and should not create it.

**`gdb/config/arch/tm-arch.h'**
: This often exists to describe the basic layout of the target machine's
processor chip (registers, stack, etc.). If used, it is included by
`tm-ttt.h'. It can be shared among many targets that use the
same processor.
New targets do not need this file and should not create it.

If you are adding a new operating system for an existing CPU chip, add a
`config/tm-os.h' file that describes the operating system
facilities that are unusual (extra symbol table info; the breakpoint
instruction needed; etc.). Then write a `arch/tm-os.h'
that just `#include`s `tm-arch.h' and
`config/tm-os.h'.

## [Converting an existing Target Architecture to Multi-arch](GDB%20Internals.md#apple-krhugnzv)

This section describes the current accepted best practice for converting
an existing target architecture to the multi-arch framework.

The process consists of generating, testing, posting and committing a
sequence of patches. Each patch must contain a single change, for
instance:

- Directly convert a group of functions into macros (the conversion does
  not change the behavior of any of the functions).
- Replace a non-multi-arch with a multi-arch mechanism (e.g.,
  `FRAME_INFO`).
- Enable multi-arch level one.
- Delete one or more files.

There isn't a size limit on a patch, however, a developer is strongly
encouraged to keep the patch size down.

Since each patch is well defined, and since each change has been tested
and shows no regressions, the patches are considered _fairly_
obvious. Such patches, when submitted by developers listed in the
`MAINTAINERS' file, do not need approval. Occasional steps in the
process may be more complicated and less clear. The developer is
expected to use their judgment and is encouraged to seek advice as
needed.

### [Preparation](GDB%20Internals.md#apple-krhugnzw)

The first step is to establish control. Build (with @option{-Werror}
enabled) and test the target so that there is a baseline against which
the debugger can be compared.

At no stage can the test results regress or GDB stop compiling
with @option{-Werror}.

### [Add the multi-arch initialization code](GDB%20Internals.md#apple-krhugnzx)

The objective of this step is to establish the basic multi-arch
framework. It involves

- The addition of a `arch_gdbarch_init` function[(4)](GDB%20Internals-2.md#apple-izhu6vbu) that creates
  the architecture:

  ```
  static struct gdbarch *
  d10v_gdbarch_init (info, arches)
       struct gdbarch_info info;
       struct gdbarch_list *arches;
  {
    struct gdbarch *gdbarch;
    /* there is only one d10v architecture */
    if (arches != NULL)
      return arches->gdbarch;
    gdbarch = gdbarch_alloc (&info, NULL);
    return gdbarch;
  }
  ```
- A per-architecture dump function to print any architecture specific
  information:

  ```
  static void
  mips_dump_tdep (struct gdbarch *current_gdbarch,
                  struct ui_file *file)
  {
     ... code to print architecture specific info ...
  }
  ```
- A change to `_initialize_arch_tdep` to register this new
  architecture:

  ```
  void
  _initialize_mips_tdep (void)
  {
    gdbarch_register (bfd_arch_mips, mips_gdbarch_init,
                      mips_dump_tdep);
  ```
- Add the macro `GDB_MULTI_ARCH`, defined as 0 (zero), to the file
  `config/arch/tm-arch.h'.

### [Update multi-arch incompatible mechanisms](GDB%20Internals.md#apple-krhugnzy)

Some mechanisms do not work with multi-arch. They include:

**`FRAME_FIND_SAVED_REGS`**
: Replaced with `DEPRECATED_FRAME_INIT_SAVED_REGS`

At this stage you could also consider converting the macros into
functions.

### [Prepare for multi-arch level to one](GDB%20Internals.md#apple-krhugnzz)

Temporally set `GDB_MULTI_ARCH` to `GDB_MULTI_ARCH_PARTIAL`
and then build and start GDB (the change should not be
committed). GDB may not build, and once built, it may die with
an internal error listing the architecture methods that must be
provided.

Fix any build problems (patch(es)).

Convert all the architecture methods listed, which are only macros, into
functions (patch(es)).

Update `arch_gdbarch_init` to set all the missing
architecture methods and wrap the corresponding macros in `#if
!GDB_MULTI_ARCH` (patch(es)).

### [Set multi-arch level one](GDB%20Internals.md#apple-krhugobq)

Change the value of `GDB_MULTI_ARCH` to GDB_MULTI_ARCH_PARTIAL (a
single patch).

Any problems with throwing "the switch" should have been fixed
already.

### [Convert remaining macros](GDB%20Internals.md#apple-krhugobr)

Suggest converting macros into functions (and setting the corresponding
architecture method) in small batches.

### [Set multi-arch level to two](GDB%20Internals.md#apple-krhugobs)

This should go smoothly.

### [Delete the TM file](GDB%20Internals.md#apple-krhugobt)

The `tm-arch.h' can be deleted. `arch.mt' and
`configure.in' updated.

---

Go to the [first](Requirements.md), [previous](Host%20Definition.md), [next](Target%20Vector%20Definition.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
