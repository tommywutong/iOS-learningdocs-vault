---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_32.html
archived_at: '2026-07-15T07:31:03.464619Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Installing%20GDB.md), [next](GDB%20Remote%20Serial%20Protocol.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Maintenance Commands](Debugging%20with%20GDB.md#apple-krhugmzqge)

In addition to commands intended for GDB users, GDB
includes a number of commands intended for GDB developers,
that are not documented elsewhere in this manual. These commands are
provided here for reference. (For commands that turn on debugging
messages, see section [Optional messages about internal happenings](Controlling%20GDB.md#apple-kncugmrsgi).)

**`maint agent expression`**
: 
Translate the given expression into remote agent bytecodes.
This command is useful for debugging the Agent Expression mechanism
(see section [The GDB Agent Expression Mechanism](The%20GDB%20Agent%20Expression%20Mechanism.md#apple-kncugmzugm)).

**`@anchor{maint info breakpoints`maint info breakpoints}**
: Using the same format as `` `info breakpoints' ``, display both the
breakpoints you've set explicitly, and those GDB is using for
internal purposes. Internal breakpoints are shown with negative
breakpoint numbers. The type column identifies what kind of breakpoint
is shown:

**`breakpoint`**
: Normal, explicitly set breakpoint.

**`watchpoint`**
: Normal, explicitly set watchpoint.

**`longjmp`**
: Internal breakpoint, used to handle correctly stepping through
`longjmp` calls.

**`longjmp resume`**
: Internal breakpoint at the target of a `longjmp`.

**`until`**
: Temporary internal breakpoint used by the GDB `until` command.

**`finish`**
: Temporary internal breakpoint used by the GDB `finish` command.

**`shlib events`**
: Shared library events.

**`maint check-symtabs`**
: Check the consistency of psymtabs and symtabs.

**`maint cplus first_component name`**
: Print the first C++ class/namespace component of name.

**`maint cplus namespace`**
: Print the list of possible C++ namespaces.

**`maint demangle name`**
: Demangle a C++ or Objective-C manled name.

**`maint deprecate command [replacement]`**
:

**`maint undeprecate command`**
: Deprecate or undeprecate the named command. Deprecated commands
cause GDB to issue a warning when you use them. The optional
argument replacement says which newer command should be used in
favor of the deprecated one; if it is given, GDB will mention
the replacement as part of the warning.

**`maint dump-me`**
: 
Cause a fatal signal in the debugger and force it to dump its core.
This is supported only on systems which support aborting a program
with the `SIGQUIT` signal.

**`maint internal-error [message-text]`**
:

**`maint internal-warning [message-text]`**
: Cause GDB to call the internal function `internal_error`
or `internal_warning` and hence behave as though an internal error
or internal warning has been detected. In addition to reporting the
internal problem, these functions give the user the opportunity to
either quit GDB or create a core file of the current
GDB session.
These commands take an optional parameter message-text that is
used as the text of the error or warning message.
Here's an example of using `indernal-error`:

```
(gdb) maint internal-error testing, 1, 2
.../maint.c:121: internal-error: testing, 1, 2
A problem internal to GDB has been detected.  Further
debugging may prove unreliable.
Quit this debugging session? (y or n) n
Create a core file? (y or n) n
(gdb)
```


**`maint packet text`**
: If GDB is talking to an inferior via the serial protocol,
then this command sends the string text to the inferior, and
displays the response packet. GDB supplies the initial
`` `$' `` character, the terminating `` `#' `` character, and the
checksum.

**`maint print architecture [file]`**
: Print the entire architecture configuration. The optional argument
file names the file where the output goes.

**`maint print dummy-frames`**
: Prints the contents of GDB's internal dummy-frame stack.

```
(gdb) b add
...
(gdb) print add(2,3)
Breakpoint 2, add (a=2, b=3) at ...
58	  return (a + b);
The program being debugged stopped while in a function called from GDB.
...
(gdb) maint print dummy-frames
0x1a57c80: pc=0x01014068 fp=0x0200bddc sp=0x0200bdd6
 top=0x0200bdd4 id={stack=0x200bddc,code=0x101405c}
 call_lo=0x01014000 call_hi=0x01014001
(gdb)
```

Takes an optional file parameter.

**`maint print registers [file]`**
:

**`maint print raw-registers [file]`**
:

**`maint print cooked-registers [file]`**
:

**`maint print register-groups [file]`**
: Print GDB's internal register data structures.
The command `maint print raw-registers` includes the contents of
the raw register cache; the command `maint print cooked-registers`
includes the (cooked) value of all registers; and the command
`maint print register-groups` includes the groups that each
register is a member of. See section `Registers' in GDB Internals.
These commands take an optional parameter, a file name to which to
write the information.

**`maint print reggroups [file]`**
: Print GDB's internal register group data structures. The
optional argument file tells to what file to write the
information.
The register groups info looks like this:

```
(gdb) maint print reggroups
 Group      Type
 general    user
 float      user
 all        user
 vector     user
 system     user
 save       internal
 restore    internal
```


**`flushregs`**
: This command forces GDB to flush its internal register cache.

**`maint print objfiles`**
: Print a dump of all known object files. For each object file, this
command prints its name, address in memory, and all of its psymtabs
and symtabs.

**`maint print statistics`**
: This command prints, for each object file in the program, various data
about that object file followed by the byte cache (__bcache__)
statistics for the object file. The objfile data includes the number
of minimal, partical, full, and stabs symbols, the number of types
defined by the objfile, the number of as yet unexpanded psym tables,
the number of line tables and string tables, and the amount of memory
used by the various tables. The bcache statistics include the counts,
sizes, and counts of duplicates of all and unique objects, max,
average, and median entry size, total memory used and its overhead and
savings, and various measures of the hash table size and chain
lengths.

**`maint print type expr`**
: Print the type chain for a type specified by expr. The argument
can be either a type name or a symbol. If it is a symbol, the type of
that symbol is described. The type chain produced by this command is
a recursive definition of the data type as stored in GDB's
data structures, including its flags and contained types.

**`maint set dwarf2 max-cache-age`**
:

**`maint show dwarf2 max-cache-age`**
: Control the DWARF 2 compilation unit cache.

In object files with inter-compilation-unit references, such as those
produced by the GCC option `` `-feliminate-dwarf2-dups' ``, the DWARF 2
reader needs to frequently refer to previously read compilation units.
This setting controls how long a compilation unit will remain in the
cache if it is not referenced. A higher limit means that cached
compilation units will be stored in memory longer, and more total
memory will be used. Setting it to zero disables caching, which will
slow down GDB startup, but reduce memory consumption.

**`maint set profile`**
:

**`maint show profile`**
: Control profiling of GDB.
Profiling will be disabled until you use the `` `maint set profile' ``
command to enable it. When you enable profiling, the system will begin
collecting timing and execution count data; when you disable profiling or
exit GDB, the results will be written to a log file. Remember that
if you use profiling, GDB will overwrite the profiling log file
(often called `gmon.out'). If you have a record of important profiling
data in a `gmon.out' file, be sure to move it to a safe location.
Configuring with `` `--enable-profiling' `` arranges for GDB to be
compiled with the `` `-pg' `` compiler option.

**`maint show-debug-regs`**
: Control whether to show variables that mirror the x86 hardware debug
registers. Use `ON` to enable, `OFF` to disable. If
enabled, the debug registers values are shown when GDB inserts or
removes a hardware breakpoint or watchpoint, and when the inferior
triggers a hardware-assisted breakpoint or watchpoint.

**`maint space`**
: Control whether to display memory usage for each command. If set to a
nonzero value, GDB will display how much memory each command
took, following the command's own output. This can also be requested
by invoking GDB with the @option{--statistics} command-line
switch (see section [Choosing modes](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugoi)).

**`maint time`**
: Control whether to display the execution time for each command. If
set to a nonzero value, GDB will display how much time it
took to execute each command, following the command's own output.
This can also be requested by invoking GDB with the
@option{--statistics} command-line switch (see section [Choosing modes](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugoi)).

**`maint translate-address [section] addr`**
: Find the symbol stored at the location specified by the address
addr and an optional section name section. If found,
GDB prints the name of the closest symbol and an offset from
the symbol's location to the specified address. This is similar to
the `info address` command (see section [Examining the Symbol Table](Examining%20the%20Symbol%20Table.md#apple-kncugmjtha)), except that this
command also allows to find symbols in other sections.

The following command is useful for non-interactive invocations of
GDB, such as in the test suite.

**`set watchdog nsec`**
: 

Set the maximum number of seconds GDB will wait for the
target operation to finish. If this time expires, GDB
reports and error and the command is aborted.

**`show watchdog`**
: Show the current setting of the target wait timeout.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Installing%20GDB.md), [next](GDB%20Remote%20Serial%20Protocol.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
