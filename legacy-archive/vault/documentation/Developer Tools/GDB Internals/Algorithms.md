---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_3.html
archived_at: '2026-07-15T07:31:03.803330Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Overall%20Structure.md), [next](User%20Interface.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Algorithms](GDB%20Internals.md#apple-krhugnq)

GDB uses a number of debugging-specific algorithms. They are
often not very complicated, but get lost in the thicket of special
cases and real-world issues. This chapter describes the basic
algorithms and mentions some of the specific target definitions that
they use.

## [Frames](GDB%20Internals.md#apple-krhugny)

A frame is a construct that GDB uses to keep track of calling
and called functions.

`FRAME_FP` in the machine description has no meaning to the
machine-independent part of GDB, except that it is used when
setting up a new frame from scratch, as follows:

```
create_new_frame (read_register (DEPRECATED_FP_REGNUM), read_pc ()));
```


Other than that, all the meaning imparted to `DEPRECATED_FP_REGNUM`
is imparted by the machine-dependent code. So,
`DEPRECATED_FP_REGNUM` can have any value that is convenient for
the code that creates new frames. (`create_new_frame` calls
`DEPRECATED_INIT_EXTRA_FRAME_INFO` if it is defined; that is where
you should use the `DEPRECATED_FP_REGNUM` value, if your frames are
nonstandard.)

Given a GDB frame, define `DEPRECATED_FRAME_CHAIN` to
determine the address of the calling function's frame. This will be
used to create a new GDB frame struct, and then
`DEPRECATED_INIT_EXTRA_FRAME_INFO` and
`DEPRECATED_INIT_FRAME_PC` will be called for the new frame.

## [Breakpoint Handling](GDB%20Internals.md#apple-krhugoa)

In general, a breakpoint is a user-designated location in the program
where the user wants to regain control if program execution ever reaches
that location.

There are two main ways to implement breakpoints; either as "hardware"
breakpoints or as "software" breakpoints.

Hardware breakpoints are sometimes available as a builtin debugging
features with some chips. Typically these work by having dedicated
register into which the breakpoint address may be stored. If the PC
(shorthand for __program counter__)
ever matches a value in a breakpoint registers, the CPU raises an
exception and reports it to GDB.

Another possibility is when an emulator is in use; many emulators
include circuitry that watches the address lines coming out from the
processor, and force it to stop if the address matches a breakpoint's
address.

A third possibility is that the target already has the ability to do
breakpoints somehow; for instance, a ROM monitor may do its own
software breakpoints. So although these are not literally "hardware
breakpoints", from GDB's point of view they work the same;
GDB need not do anything more than set the breakpoint and wait
for something to happen.

Since they depend on hardware resources, hardware breakpoints may be
limited in number; when the user asks for more, GDB will
start trying to set software breakpoints. (On some architectures,
notably the 32-bit x86 platforms, GDB cannot always know
whether there's enough hardware resources to insert all the hardware
breakpoints and watchpoints. On those platforms, GDB prints
an error message only when the program being debugged is continued.)

Software breakpoints require GDB to do somewhat more work.
The basic theory is that GDB will replace a program
instruction with a trap, illegal divide, or some other instruction
that will cause an exception, and then when it's encountered,
GDB will take the exception and stop the program. When the
user says to continue, GDB will restore the original
instruction, single-step, re-insert the trap, and continue on.

Since it literally overwrites the program being tested, the program area
must be writable, so this technique won't work on programs in ROM. It
can also distort the behavior of programs that examine themselves,
although such a situation would be highly unusual.

Also, the software breakpoint instruction should be the smallest size of
instruction, so it doesn't overwrite an instruction that might be a jump
target, and cause disaster when the program jumps into the middle of the
breakpoint instruction. (Strictly speaking, the breakpoint must be no
larger than the smallest interval between instructions that may be jump
targets; perhaps there is an architecture where only even-numbered
instructions may jumped to.) Note that it's possible for an instruction
set not to have any instructions usable for a software breakpoint,
although in practice only the ARC has failed to define such an
instruction.

The basic definition of the software breakpoint is the macro
`BREAKPOINT`.

Basic breakpoint object handling is in `breakpoint.c'. However,
much of the interesting breakpoint action is in `infrun.c'.

## [Single Stepping](GDB%20Internals.md#apple-krhugoi)

## [Signal Handling](GDB%20Internals.md#apple-krhugmjq)

## [Thread Handling](GDB%20Internals.md#apple-krhugmjr)

## [Inferior Function Calls](GDB%20Internals.md#apple-krhugmjs)

## [Longjmp Support](GDB%20Internals.md#apple-krhugmjt)

GDB has support for figuring out that the target is doing a
`longjmp` and for stopping at the target of the jump, if we are
stepping. This is done with a few specialized internal breakpoints,
which are visible in the output of the `` `maint info breakpoint' ``
command.

To make this work, you need to define a macro called
`GET_LONGJMP_TARGET`, which will examine the `jmp_buf`
structure and extract the longjmp target address. Since `jmp_buf`
is target specific, you will need to define it in the appropriate
`tm-target.h' file. Look in `tm-sun4os4.h' and
`sparc-tdep.c' for examples of how to do this.

## [Watchpoints](GDB%20Internals.md#apple-krhugmju)

Watchpoints are a special kind of breakpoints (see section [Algorithms](#apple-kncugnq)) which break when data is accessed rather than when some
instruction is executed. When you have data which changes without
your knowing what code does that, watchpoints are the silver bullet to
hunt down and kill such bugs.

Watchpoints can be either hardware-assisted or not; the latter type is
known as "software watchpoints." GDB always uses
hardware-assisted watchpoints if they are available, and falls back on
software watchpoints otherwise. Typical situations where GDB
will use software watchpoints are:

- The watched memory region is too large for the underlying hardware
  watchpoint support. For example, each x86 debug register can watch up
  to 4 bytes of memory, so trying to watch data structures whose size is
  more than 16 bytes will cause GDB to use software
  watchpoints.
- The value of the expression to be watched depends on data held in
  registers (as opposed to memory).
- Too many different watchpoints requested. (On some architectures,
  this situation is impossible to detect until the debugged program is
  resumed.) Note that x86 debug registers are used both for hardware
  breakpoints and for watchpoints, so setting too many hardware
  breakpoints might cause watchpoint insertion to fail.
- No hardware-assisted watchpoints provided by the target
  implementation.

Software watchpoints are very slow, since GDB needs to
single-step the program being debugged and test the value of the
watched expression(s) after each instruction. The rest of this
section is mostly irrelevant for software watchpoints.

When the inferior stops, GDB tries to establish, among other
possible reasons, whether it stopped due to a watchpoint being hit.
For a data-write watchpoint, it does so by evaluating, for each
watchpoint, the expression whose value is being watched, and testing
whether the watched value has changed. For data-read and data-access
watchpoints, GDB needs the target to supply a primitive that
returns the address of the data that was accessed or read (see the
description of `target_stopped_data_address` below): if this
primitive returns a valid address, GDB infers that a
watchpoint triggered if it watches an expression whose evaluation uses
that address.

GDB uses several macros and primitives to support hardware
watchpoints:

**`TARGET_HAS_HARDWARE_WATCHPOINTS`**
: 
If defined, the target supports hardware watchpoints.

**`TARGET_CAN_USE_HARDWARE_WATCHPOINT (type, count, other)`**
: Return the number of hardware watchpoints of type type that are
possible to be set. The value is positive if count watchpoints
of this type can be set, zero if setting watchpoints of this type is
not supported, and negative if count is more than the maximum
number of watchpoints of type type that can be set. other
is non-zero if other types of watchpoints are currently enabled (there
are architectures which cannot set watchpoints of different types at
the same time).

**`TARGET_REGION_OK_FOR_HW_WATCHPOINT (addr, len)`**
: Return non-zero if hardware watchpoints can be used to watch a region
whose address is addr and whose length in bytes is len.

**`TARGET_REGION_SIZE_OK_FOR_HW_WATCHPOINT (size)`**
: Return non-zero if hardware watchpoints can be used to watch a region
whose size is size. GDB only uses this macro as a
fall-back, in case `TARGET_REGION_OK_FOR_HW_WATCHPOINT` is not
defined.

**`target_insert_watchpoint (addr, len, type)`**
:

**`target_remove_watchpoint (addr, len, type)`**
: Insert or remove a hardware watchpoint starting at addr, for
len bytes. type is the watchpoint type, one of the
possible values of the enumerated data type `target_hw_bp_type`,
defined by `breakpoint.h' as follows:

```
 enum target_hw_bp_type
   {
     hw_write   = 0, /* Common (write) HW watchpoint */
     hw_read    = 1, /* Read    HW watchpoint */
     hw_access  = 2, /* Access (read or write) HW watchpoint */
     hw_execute = 3  /* Execute HW breakpoint */
   };
```

These two macros should return 0 for success, non-zero for failure.

**`target_remove_hw_breakpoint (addr, shadow)`**
:

**`target_insert_hw_breakpoint (addr, shadow)`**
: Insert or remove a hardware-assisted breakpoint at address addr.
Returns zero for success, non-zero for failure. shadow is the
real contents of the byte where the breakpoint has been inserted; it
is generally not valid when hardware breakpoints are used, but since
no other code touches these values, the implementations of the above
two macros can use them for their internal purposes.

**`target_stopped_data_address (addr_p)`**
: If the inferior has some watchpoint that triggered, place the address
associated with the watchpoint at the location pointed to by
addr_p and return non-zero. Otherwise, return zero. Note that
this primitive is used by GDB only on targets that support
data-read or data-access type watchpoints, so targets that have
support only for data-write watchpoints need not implement these
primitives.

**`HAVE_STEPPABLE_WATCHPOINT`**
: If defined to a non-zero value, it is not necessary to disable a
watchpoint to step over it.

**`HAVE_NONSTEPPABLE_WATCHPOINT`**
: If defined to a non-zero value, GDB should disable a
watchpoint to step the inferior over it.

**`HAVE_CONTINUABLE_WATCHPOINT`**
: If defined to a non-zero value, it is possible to continue the
inferior after a watchpoint has been hit.

**`CANNOT_STEP_HW_WATCHPOINTS`**
: If this is defined to a non-zero value, GDB will remove all
watchpoints before stepping the inferior.

**`STOPPED_BY_WATCHPOINT (wait_status)`**
: Return non-zero if stopped by a watchpoint. wait_status is of
the type `struct target_waitstatus`, defined by `target.h'.
Normally, this macro is defined to invoke the function pointed to by
the `to_stopped_by_watchpoint` member of the structure (of the
type `target_ops`, defined on `target.h') that describes the
target-specific operations; `to_stopped_by_watchpoint` ignores
the wait_status argument.
GDB does not require the non-zero value returned by
`STOPPED_BY_WATCHPOINT` to be 100% correct, so if a target cannot
determine for sure whether the inferior stopped due to a watchpoint,
it could return non-zero "just in case".

### [x86 Watchpoints](GDB%20Internals.md#apple-krhugmjv)

The 32-bit Intel x86 (a.k.a. ia32) processors feature special debug
registers designed to facilitate debugging. GDB provides a
generic library of functions that x86-based ports can use to implement
support for watchpoints and hardware-assisted breakpoints. This
subsection documents the x86 watchpoint facilities in GDB.

To use the generic x86 watchpoint support, a port should do the
following:

- 
  Define the macro `I386_USE_GENERIC_WATCHPOINTS` somewhere in the
  target-dependent headers.
- Include the `config/i386/nm-i386.h' header file _after_
  defining `I386_USE_GENERIC_WATCHPOINTS`.
- Add `i386-nat.o' to the value of the Make variable
  `NATDEPFILES` (see section [Native Debugging](Native%20Debugging.md#apple-kncugojr)) or
  `TDEPFILES` (see section [Target Architecture Definition](Target%20Architecture%20Definition.md#apple-kncugnrt)).
- Provide implementations for the `I386_DR_LOW_*` macros described
  below. Typically, each macro should call a target-specific function
  which does the real work.

The x86 watchpoint support works by maintaining mirror images of the
debug registers. Values are copied between the mirror images and the
real debug registers via a set of macros which each target needs to
provide:

**`I386_DR_LOW_SET_CONTROL (val)`**
: 
Set the Debug Control (DR7) register to the value val.

**`I386_DR_LOW_SET_ADDR (idx, addr)`**
: Put the address addr into the debug register number idx.

**`I386_DR_LOW_RESET_ADDR (idx)`**
: Reset (i.e. zero out) the address stored in the debug register
number idx.

**`I386_DR_LOW_GET_STATUS`**
: Return the value of the Debug Status (DR6) register. This value is
used immediately after it is returned by
`I386_DR_LOW_GET_STATUS`, so as to support per-thread status
register values.

For each one of the 4 debug registers (whose indices are from 0 to 3)
that store addresses, a reference count is maintained by GDB,
to allow sharing of debug registers by several watchpoints. This
allows users to define several watchpoints that watch the same
expression, but with different conditions and/or commands, without
wasting debug registers which are in short supply. GDB
maintains the reference counts internally, targets don't have to do
anything to use this feature.

The x86 debug registers can each watch a region that is 1, 2, or 4
bytes long. The ia32 architecture requires that each watched region
be appropriately aligned: 2-byte region on 2-byte boundary, 4-byte
region on 4-byte boundary. However, the x86 watchpoint support in
GDB can watch unaligned regions and regions larger than 4
bytes (up to 16 bytes) by allocating several debug registers to watch
a single region. This allocation of several registers per a watched
region is also done automatically without target code intervention.

The generic x86 watchpoint support provides the following API for the
GDB's application code:

**`i386_region_ok_for_watchpoint (addr, len)`**
: 
The macro `TARGET_REGION_OK_FOR_HW_WATCHPOINT` is set to call
this function. It counts the number of debug registers required to
watch a given region, and returns a non-zero value if that number is
less than 4, the number of debug registers available to x86
processors.

**`i386_stopped_data_address (addr_p)`**
: The target function
`target_stopped_data_address` is set to call this function.
This
function examines the breakpoint condition bits in the DR6 Debug
Status register, as returned by the `I386_DR_LOW_GET_STATUS`
macro, and returns the address associated with the first bit that is
set in DR6.

**`i386_stopped_by_watchpoint (void)`**
: The macro `STOPPED_BY_WATCHPOINT`
is set to call this function. The
argument passed to `STOPPED_BY_WATCHPOINT` is ignored. This
function examines the breakpoint condition bits in the DR6 Debug
Status register, as returned by the `I386_DR_LOW_GET_STATUS`
macro, and returns true if any bit is set. Otherwise, false is
returned.

**`i386_insert_watchpoint (addr, len, type)`**
:

**`i386_remove_watchpoint (addr, len, type)`**
: Insert or remove a watchpoint. The macros
`target_insert_watchpoint` and `target_remove_watchpoint`
are set to call these functions. `i386_insert_watchpoint` first
looks for a debug register which is already set to watch the same
region for the same access types; if found, it just increments the
reference count of that debug register, thus implementing debug
register sharing between watchpoints. If no such register is found,
the function looks for a vacant debug register, sets its mirrored
value to addr, sets the mirrored value of DR7 Debug Control
register as appropriate for the len and type parameters,
and then passes the new values of the debug register and DR7 to the
inferior by calling `I386_DR_LOW_SET_ADDR` and
`I386_DR_LOW_SET_CONTROL`. If more than one debug register is
required to cover the given region, the above process is repeated for
each debug register.
`i386_remove_watchpoint` does the opposite: it resets the address
in the mirrored value of the debug register and its read/write and
length bits in the mirrored value of DR7, then passes these new
values to the inferior via `I386_DR_LOW_RESET_ADDR` and
`I386_DR_LOW_SET_CONTROL`. If a register is shared by several
watchpoints, each time a `i386_remove_watchpoint` is called, it
decrements the reference count, and only calls
`I386_DR_LOW_RESET_ADDR` and `I386_DR_LOW_SET_CONTROL` when
the count goes to zero.

**`i386_insert_hw_breakpoint (addr, shadow`**
:

**`i386_remove_hw_breakpoint (addr, shadow)`**
: These functions insert and remove hardware-assisted breakpoints. The
macros `target_insert_hw_breakpoint` and
`target_remove_hw_breakpoint` are set to call these functions.
These functions work like `i386_insert_watchpoint` and
`i386_remove_watchpoint`, respectively, except that they set up
the debug registers to watch instruction execution, and each
hardware-assisted breakpoint always requires exactly one debug
register.

**`i386_stopped_by_hwbp (void)`**
: This function returns non-zero if the inferior has some watchpoint or
hardware breakpoint that triggered. It works like
`i386_stopped_data_address`, except that it doesn't record the
address whose watchpoint triggered.

**`i386_cleanup_dregs (void)`**
: This function clears all the reference counts, addresses, and control
bits in the mirror images of the debug registers. It doesn't affect
the actual debug registers in the inferior process.

__Notes:__

1. x86 processors support setting watchpoints on I/O reads or writes.
   However, since no target supports this (as of March 2001), and since
   `enum target_hw_bp_type` doesn't even have an enumeration for I/O
   watchpoints, this feature is not yet available to GDB running
   on x86.
2. x86 processors can enable watchpoints locally, for the current task
   only, or globally, for all the tasks. For each debug register,
   there's a bit in the DR7 Debug Control register that determines
   whether the associated address is watched locally or globally. The
   current implementation of x86 watchpoint support in GDB
   always sets watchpoints to be locally enabled, since global
   watchpoints might interfere with the underlying OS and are probably
   unavailable in many platforms.

## [Observing changes in GDB internals](GDB%20Internals.md#apple-krhugmjw)

In order to function properly, several modules need to be notified when
some changes occur in the GDB internals. Traditionally, these
modules have relied on several paradigms, the most common ones being
hooks and gdb-events. Unfortunately, none of these paradigms was
versatile enough to become the standard notification mechanism in
GDB. The fact that they only supported one "client" was also
a strong limitation.

A new paradigm, based on the Observer pattern of the Design
Patterns book, has therefore been implemented. The goal was to provide
a new interface overcoming the issues with the notification mechanisms
previously available. This new interface needed to be strongly typed,
easy to extend, and versatile enough to be used as the standard
interface when adding new notifications.

See section [GDB Currently available observers](GDB%20Currently%20available%20observers.md#apple-kncugmjvgu) for a brief description of the observers
currently implemented in GDB. The rationale for the current
implementation is also briefly discussed.

---

Go to the [first](Requirements.md), [previous](Overall%20Structure.md), [next](User%20Interface.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
