---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_12.html
archived_at: '2026-07-15T07:31:03.200260Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Tracepoints.md), [next](Using%20GDB%20with%20Different%20Languages.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Debugging Programs That Use Overlays](Debugging%20with%20GDB.md#apple-krhugojt)

If your program is too large to fit completely in your target system's
memory, you can sometimes use __overlays__ to work around this
problem. GDB provides some support for debugging programs that
use overlays.

## [How Overlays Work](Debugging%20with%20GDB.md#apple-krhugoju)

Suppose you have a computer whose instruction address space is only 64
kilobytes long, but which has much more memory which can be accessed by
other means: special instructions, segment registers, or memory
management hardware, for example. Suppose further that you want to
adapt a program which is larger than 64 kilobytes to run on this system.

One solution is to identify modules of your program which are relatively
independent, and need not call each other directly; call these modules
__overlays__. Separate the overlays from the main program, and place
their machine code in the larger memory. Place your main program in
instruction memory, but leave at least enough space there to hold the
largest overlay as well.

Now, to call a function located in an overlay, you must first copy that
overlay's machine code from the large memory into the space set aside
for it in the instruction memory, and then jump to its entry point
there.

```
    Data             Instruction            Larger
Address Space       Address Space        Address Space
+-----------+       +-----------+        +-----------+
|           |       |           |        |           |
+-----------+       +-----------+        +-----------+<-- overlay 1
| program   |       |   main    |   .----| overlay 1 | load address
| variables |       |  program  |   |    +-----------+
| and heap  |       |           |   |    |           |
+-----------+       |           |   |    +-----------+<-- overlay 2
|           |       +-----------+   |    |           | load address
+-----------+       |           |   |  .-| overlay 2 |
                    |           |   |  | |           |
         mapped --->+-----------+   |  | +-----------+
         address    |           |   |  | |           |
                    |  overlay  | <-'  | |           |
                    |   area    |  <---' +-----------+<-- overlay 3
                    |           | <---.  |           | load address
                    +-----------+     `--| overlay 3 |
                    |           |        |           |
                    +-----------+        |           |
                                         +-----------+
                                         |           |
                                         +-----------+

                    @anchor{A code overlay}A code overlay
```

The diagram (@xref{A code overlay}) shows a system with separate data
and instruction address spaces. To map an overlay, the program copies
its code from the larger address space to the instruction address space.
Since the overlays shown here all use the same mapped address, only one
may be mapped at a time. For a system with a single address space for
data and instructions, the diagram would be similar, except that the
program variables and heap would share an address space with the main
program and the overlay area.

An overlay loaded into instruction memory and ready for use is called a
__mapped__ overlay; its __mapped address__ is its address in the
instruction memory. An overlay not present (or only partially present)
in instruction memory is called __unmapped__; its __load address__
is its address in the larger memory. The mapped address is also called
the __virtual memory address__, or __VMA__; the load address is also
called the __load memory address__, or __LMA__.

Unfortunately, overlays are not a completely transparent way to adapt a
program to limited instruction memory. They introduce a new set of
global constraints you must keep in mind as you design your program:

- Before calling or returning to a function in an overlay, your program
  must make sure that overlay is actually mapped. Otherwise, the call or
  return will transfer control to the right address, but in the wrong
  overlay, and your program will probably crash.
- If the process of mapping an overlay is expensive on your system, you
  will need to choose your overlays carefully to minimize their effect on
  your program's performance.
- The executable file you load onto your system must contain each
  overlay's instructions, appearing at the overlay's load address, not its
  mapped address. However, each overlay's instructions must be relocated
  and its symbols defined as if the overlay were at its mapped address.
  You can use GNU linker scripts to specify different load and relocation
  addresses for pieces of your program; see section `Overlay Description' in Using ld: the GNU linker.
- The procedure for loading executable files onto your system must be able
  to load their contents into the larger address space as well as the
  instruction and data spaces.

The overlay system described above is rather simple, and could be
improved in many ways:

- If your system has suitable bank switch registers or memory management
  hardware, you could use those facilities to make an overlay's load area
  contents simply appear at their mapped address in instruction space.
  This would probably be faster than copying the overlay to its mapped
  area in the usual way.
- If your overlays are small enough, you could set aside more than one
  overlay area, and have more than one overlay mapped at a time.
- You can use overlays to manage data, as well as instructions. In
  general, data overlays are even less transparent to your design than
  code overlays: whereas code overlays only require care when you call or
  return to functions, data overlays require care every time you access
  the data. Also, if you change the contents of a data overlay, you
  must copy its contents back out to its load address before you can copy a
  different data overlay into the same mapped area.

## [Overlay Commands](Debugging%20with%20GDB.md#apple-krhugojv)

To use GDB's overlay support, each overlay in your program must
correspond to a separate section of the executable file. The section's
virtual memory address and load memory address must be the overlay's
mapped and load addresses. Identifying overlays with sections allows
GDB to determine the appropriate address of a function or
variable, depending on whether the overlay is mapped or not.

GDB's overlay commands all start with the word `overlay`;
you can abbreviate this as `ov` or `ovly`. The commands are:

**`overlay off`**
: 
Disable GDB's overlay support. When overlay support is
disabled, GDB assumes that all functions and variables are
always present at their mapped addresses. By default, GDB's
overlay support is disabled.

**`overlay manual`**
: 
Enable __manual__ overlay debugging. In this mode, GDB
relies on you to tell it which overlays are mapped, and which are not,
using the `overlay map-overlay` and `overlay unmap-overlay`
commands described below.

**`overlay map-overlay overlay`**
:

**`overlay map overlay`**
: 
Tell GDB that overlay is now mapped; overlay must
be the name of the object file section containing the overlay. When an
overlay is mapped, GDB assumes it can find the overlay's
functions and variables at their mapped addresses. GDB assumes
that any other overlays whose mapped ranges overlap that of
overlay are now unmapped.

**`overlay unmap-overlay overlay`**
:

**`overlay unmap overlay`**
: 
Tell GDB that overlay is no longer mapped; overlay
must be the name of the object file section containing the overlay.
When an overlay is unmapped, GDB assumes it can find the
overlay's functions and variables at their load addresses.

**`overlay auto`**
: Enable __automatic__ overlay debugging. In this mode, GDB
consults a data structure the overlay manager maintains in the inferior
to see which overlays are mapped. For details, see section [Automatic Overlay Debugging](#apple-kncugojw).

**`overlay load-target`**
:

**`overlay load`**
: 
Re-read the overlay table from the inferior. Normally, GDB
re-reads the table GDB automatically each time the inferior
stops, so this command should only be necessary if you have changed the
overlay mapping yourself using GDB. This command is only
useful when using automatic overlay debugging.

**`overlay list-overlays`**
:

**`overlay list`**
: 
Display a list of the overlays currently mapped, along with their mapped
addresses, load addresses, and sizes.

Normally, when GDB prints a code address, it includes the name
of the function the address falls in:

```
(gdb) print main
$3 = {int ()} 0x11a0 <main>
```

When overlay debugging is enabled, GDB recognizes code in
unmapped overlays, and prints the names of unmapped functions with
asterisks around them. For example, if `foo` is a function in an
unmapped overlay, GDB prints it this way:

```
(gdb) overlay list
No sections are mapped.
(gdb) print foo
$5 = {int (int)} 0x100000 <*foo*>
```

When `foo`'s overlay is mapped, GDB prints the function's
name normally:

```
(gdb) overlay list
Section .ov.foo.text, loaded at 0x100000 - 0x100034,
        mapped at 0x1016 - 0x104a
(gdb) print foo
$6 = {int (int)} 0x1016 <foo>
```

When overlay debugging is enabled, GDB can find the correct
address for functions and variables in an overlay, whether or not the
overlay is mapped. This allows most GDB commands, like
`break` and `disassemble`, to work normally, even on unmapped
code. However, GDB's breakpoint support has some limitations:

- 
  
  You can set breakpoints in functions in unmapped overlays, as long as
  GDB can write to the overlay at its load address.
- GDB can not set hardware or simulator-based breakpoints in
  unmapped overlays. However, if you set a breakpoint at the end of your
  overlay manager (and tell GDB which overlays are now mapped, if
  you are using manual overlay management), GDB will re-set its
  breakpoints properly.

## [Automatic Overlay Debugging](Debugging%20with%20GDB.md#apple-krhugojw)

GDB can automatically track which overlays are mapped and which
are not, given some simple co-operation from the overlay manager in the
inferior. If you enable automatic overlay debugging with the
`overlay auto` command (see section [Overlay Commands](#apple-kncugojv)), GDB
looks in the inferior's memory for certain variables describing the
current state of the overlays.

Here are the variables your overlay manager must define to support
GDB's automatic overlay debugging:

**`_ovly_table`:**
: This variable must be an array of the following structures:

```
struct
{
  /* The overlay's mapped address.  */
  unsigned long vma;

  /* The size of the overlay, in bytes.  */
  unsigned long size;

  /* The overlay's load address.  */
  unsigned long lma;

  /* Non-zero if the overlay is currently mapped;
     zero otherwise.  */
  unsigned long mapped;
}
```

**`_novlys`:**
: This variable must be a four-byte signed integer, holding the total
number of elements in `_ovly_table`.

To decide whether a particular overlay is mapped or not, GDB
looks for an entry in `_ovly_table` whose `vma` and
`lma` members equal the VMA and LMA of the overlay's section in the
executable file. When GDB finds a matching entry, it consults
the entry's `mapped` member to determine whether the overlay is
currently mapped.

In addition, your overlay manager may define a function called
`_ovly_debug_event`. If this function is defined, GDB
will silently set a breakpoint there. If the overlay manager then
calls this function whenever it has changed the overlay table, this
will enable GDB to accurately keep track of which overlays
are in program memory, and update any breakpoints that may be set
in overlays. This will allow breakpoints to work even if the
overlays are kept in ROM or other non-writable memory while they
are not being executed.

## [Overlay Sample Program](Debugging%20with%20GDB.md#apple-krhugojx)

When linking a program which uses overlays, you must place the overlays
at their load addresses, while relocating them to run at their mapped
addresses. To do this, you must write a linker script (see section `Overlay Description' in Using ld: the GNU linker). Unfortunately,
since linker scripts are specific to a particular host system, target
architecture, and target memory layout, this manual cannot provide
portable sample code demonstrating GDB's overlay support.

However, the GDB source distribution does contain an overlaid
program, with linker scripts for a few systems, as part of its test
suite. The program consists of the following files from
`gdb/testsuite/gdb.base':

**`overlays.c'**
: The main program file.

**`ovlymgr.c'**
: A simple overlay manager, used by `overlays.c'.

**`foo.c'**
:

**`bar.c'**
:

**`baz.c'**
:

**`grbx.c'**
: Overlay modules, loaded and used by `overlays.c'.

**`d10v.ld'**
:

**`m32r.ld'**
: Linker scripts for linking the test program on the `d10v-elf`
and `m32r-elf` targets.

You can build the test program using the `d10v-elf` GCC
cross-compiler like this:

```shell
$ d10v-elf-gcc -g -c overlays.c
$ d10v-elf-gcc -g -c ovlymgr.c
$ d10v-elf-gcc -g -c foo.c
$ d10v-elf-gcc -g -c bar.c
$ d10v-elf-gcc -g -c baz.c
$ d10v-elf-gcc -g -c grbx.c
$ d10v-elf-gcc -g overlays.o ovlymgr.o foo.o bar.o \
                  baz.o grbx.o -Wl,-Td10v.ld -o overlays
```

The build process is identical for any other architecture, except that
you must substitute the appropriate compiler and linker script for the
target system for `d10v-elf-gcc` and `d10v.ld`.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Tracepoints.md), [next](Using%20GDB%20with%20Different%20Languages.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
