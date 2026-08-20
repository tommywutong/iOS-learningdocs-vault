---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_16.html
archived_at: '2026-07-15T07:31:03.247913Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Altering%20Execution.md), [next](Specifying%20a%20Debugging%20Target.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [GDB Files](Debugging%20with%20GDB.md#apple-krhugmjugy)

GDB needs to know the file name of the program to be debugged,
both in order to read its symbol table and in order to start your
program. To debug a core dump of a previous run, you must also tell
GDB the name of the core dump file.

## [Commands to specify files](Debugging%20with%20GDB.md#apple-krhugmjug4)

You may want to specify executable and core dump file names. The usual
way to do this is at start-up time, using the arguments to
GDB's start-up commands (see section [Getting In and Out of GDB](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugnq)).

Occasionally it is necessary to change to a different file during a
GDB session. Or you may run GDB and forget to
specify a file you want to use. Or you are debugging a remote target
via `gdbserver` (see section [Using the `gdbserver` program](gdb_18.md#apple-kncugmjvha)). In these situations the
GDB commands to specify new files are useful.

**`file filename`**
: 

Use filename as the program to be debugged. It is read for its
symbols and for the contents of pure memory. It is also the program
executed when you use the `run` command. If you do not specify a
directory and the file is not found in the GDB working directory,
GDB uses the environment variable `PATH` as a list of
directories to search, just as the shell does when looking for a program
to run. You can change the value of this variable, for both GDB
and your program, using the `path` command.
On systems with memory-mapped files, an auxiliary file named
`filename.syms' may hold symbol table information for
filename. If so, GDB maps in the symbol table from
`filename.syms', starting up more quickly. See the
descriptions of the file options `` `-mapped' `` and `` `-readnow' ``
(available on the command line, see section [Choosing files](Getting%20In%20and%20Out%20of%20GDB.md#apple-kncugoa),
and with the commands `file`, `symbol-file`, or
`add-symbol-file`, described below), for more information.

You can load unlinked object `.o' files into GDB using
the `file` command. You will not be able to "run" an object
file, but you can disassemble functions and inspect variables. Also,
if the underlying BFD functionality supports it, you could use
`gdb -write` to patch object files using this technique. Note
that GDB can neither interpret nor modify relocations in this
case, so branches and some initialized variables will appear to go to
the wrong place. But this feature is still handy from time to time.

**`file`**
: `file` with no argument makes GDB discard any information it
has on both executable file and the symbol table.

**`exec-file [ filename ]`**
: Specify that the program to be run (but not the symbol table) is found
in filename. GDB searches the environment variable `PATH`
if necessary to locate your program. Omitting filename means to
discard information on the executable file.

**`symbol-file [ filename ]`**
: Read symbol table information from file filename. `PATH` is
searched when necessary. Use the `file` command to get both symbol
table and program to run from the same file.
`symbol-file` with no argument clears out GDB information on your
program's symbol table.
The `symbol-file` command causes GDB to forget the contents
of its convenience variables, the value history, and all breakpoints and
auto-display expressions. This is because they may contain pointers to
the internal data recording symbols and data types, which are part of
the old symbol table data being discarded inside GDB.
`symbol-file` does not repeat if you press `RET` again after
executing it once.
When GDB is configured for a particular environment, it
understands debugging information in whatever format is the standard
generated for that environment; you may use either a GNU compiler, or
other compilers that adhere to the local conventions.
Best results are usually obtained from GNU compilers; for example,
using `gcc` you can generate debugging information for
optimized code.
For most kinds of object files, with the exception of old SVR3 systems
using COFF, the `symbol-file` command does not normally read the
symbol table in full right away. Instead, it scans the symbol table
quickly to find which source files and which symbols are present. The
details are read later, one source file at a time, as they are needed.
The purpose of this two-stage reading strategy is to make GDB
start up faster. For the most part, it is invisible except for
occasional pauses while the symbol table details for a particular source
file are being read. (The `set verbose` command can turn these
pauses into messages if desired. See section [Optional warnings and messages](Controlling%20GDB.md#apple-kncugmrsge).)
We have not implemented the two-stage strategy for COFF yet. When the
symbol table is stored in COFF format, `symbol-file` reads the
symbol table data in full right away. Note that "stabs-in-COFF"
still does the two-stage strategy, since the debug info is actually
in stabs format.

**`symbol-file filename [ -readnow ] [ -mapped ]`**
:

**`file filename [ -readnow ] [ -mapped ]`**
: You can override the GDB two-stage strategy for reading symbol
tables by using the `` `-readnow' `` option with any of the commands that
load symbol table information, if you want to be sure GDB has the
entire symbol table available.
If memory-mapped files are available on your system through the
`mmap` system call, you can use another option, `` `-mapped' ``, to
cause GDB to write the symbols for your program into a reusable
file. Future GDB debugging sessions map in symbol information
from this auxiliary symbol file (if the program has not changed), rather
than spending time reading the symbol table from the executable
program. Using the `` `-mapped' `` option has the same effect as
starting GDB with the `` `-mapped' `` command-line option.
You can use both options together, to make sure the auxiliary symbol
file has all the symbol information for your program.
The auxiliary symbol file for a program called myprog is called
`` `myprog.syms' ``. Once this file exists (so long as it is newer
than the corresponding executable), GDB always attempts to use
it when you debug myprog; no special options or commands are
needed.
The `.syms' file is specific to the host machine where you run
GDB. It holds an exact image of the internal GDB
symbol table. It cannot be shared across multiple host platforms.

**`core-file [filename]`**
:

**`core`**
: Specify the whereabouts of a core dump file to be used as the "contents
of memory". Traditionally, core files contain only some parts of the
address space of the process that generated them; GDB can access the
executable file itself for other parts.
`core-file` with no argument specifies that no core file is
to be used.
Note that the core file is ignored when your program is actually running
under GDB. So, if you have been running your program and you
wish to debug a core file instead, you must kill the subprocess in which
the program is running. To do this, use the `kill` command
(see section [Killing the child process](Running%20Programs%20Under%20GDB.md#apple-kncugmrw)).

**`add-symbol-file filename address`**
:

**`add-symbol-file filename address [ -readnow ] [ -mapped ]`**
:

**`add-symbol-file filename -ssection address ...`**
: The `add-symbol-file` command reads additional symbol table
information from the file filename. You would use this command
when filename has been dynamically loaded (by some other means)
into the program that is running. address should be the memory
address at which the file has been loaded; GDB cannot figure
this out for itself. You can additionally specify an arbitrary number
of `` `-ssection address' `` pairs, to give an explicit
section name and base address for that section. You can specify any
address as an expression.
The symbol table of the file filename is added to the symbol table
originally read with the `symbol-file` command. You can use the
`add-symbol-file` command any number of times; the new symbol data
thus read keeps adding to the old. To discard all old symbol data
instead, use the `symbol-file` command without any arguments.

Although filename is typically a shared library file, an
executable file, or some other object file which has been fully
relocated for loading into a process, you can also load symbolic
information from relocatable `.o' files, as long as:

- the file's symbolic information refers only to linker symbols defined in
  that file, not to symbols defined by other object files,
- every section the file's symbolic information refers to has actually
  been loaded into the inferior, as it appears in the file, and
- you can determine the address at which every section was loaded, and
  provide these to the `add-symbol-file` command.

Some embedded operating systems, like Sun Chorus and VxWorks, can load
relocatable files into an already running program; such systems
typically make the requirements above easy to meet. However, it's
important to recognize that many native systems use complex link
procedures (`.linkonce` section factoring and C++ constructor table
assembly, for example) that make the requirements difficult to meet. In
general, one cannot assume that using `add-symbol-file` to read a
relocatable object file's symbolic information will have the same effect
as linking the relocatable object file into the program in the normal
way.
`add-symbol-file` does not repeat if you press `RET` after using it.
You can use the `` `-mapped' `` and `` `-readnow' `` options just as with
the `symbol-file` command, to change how GDB manages the symbol
table information for filename.

**`add-symbol-file-from-memory address`**
: Load symbols from the given address in a dynamically loaded
object file whose image is mapped directly into the inferior's memory.
For example, the Linux kernel maps a `syscall DSO` into each
process's address space; this DSO provides kernel-specific code for
some system calls. The argument can be any expression whose
evaluation yields the address of the file's shared object file header.
For this command to work, you must have used `symbol-file` or
`exec-file` commands in advance.

**`add-shared-symbol-files library-file`**
:

**`assf library-file`**
: The `add-shared-symbol-files` command can currently be used only
in the Cygwin build of GDB on MS-Windows OS, where it is an
alias for the `dll-symbols` command (see section [Features for Debugging MS Windows PE executables](Configuration-Specific%20Information.md#apple-kncugmjxge)).
GDB automatically looks for shared libraries, however if
GDB does not find yours, you can invoke
`add-shared-symbol-files`. It takes one argument: the shared
library's file name. `assf` is a shorthand alias for
`add-shared-symbol-files`.

**`section section addr`**
: The `section` command changes the base address of the named
section of the exec file to addr. This can be used if the
exec file does not contain section addresses, (such as in the
`a.out` format), or when the addresses specified in the file
itself are wrong. Each section must be changed separately. The
`info files` command, described below, lists all the sections and
their addresses.

**`info files`**
:

**`info target`**
: `info files` and `info target` are synonymous; both print the
current target (see section [Specifying a Debugging Target](Specifying%20a%20Debugging%20Target.md#apple-kncugmjvga)),
including the names of the executable and core dump files currently in
use by GDB, and the files from which symbols were loaded. The
command `help target` lists all possible targets rather than
current ones.

**`maint info sections`**
: Another command that can give you extra information about program sections
is `maint info sections`. In addition to the section information
displayed by `info files`, this command displays the flags and file
offset of each section in the executable and core dump files. In addition,
`maint info sections` provides the following command options (which
may be arbitrarily combined):

**`ALLOBJ`**
: Display sections for all loaded object files, including shared libraries.

**`sections`**
: Display info only for named sections.

**`section-flags`**
: Display info only for sections for which section-flags are true.
The section flags that GDB currently knows about are:

**`ALLOC`**
: Section will have space allocated in the process when loaded.
Set for all sections except those containing debug information.

**`LOAD`**
: Section will be loaded from the file into the child process memory.
Set for pre-initialized code and data, clear for `.bss` sections.

**`RELOC`**
: Section needs to be relocated before loading.

**`READONLY`**
: Section cannot be modified by the child process.

**`CODE`**
: Section contains executable code only.

**`DATA`**
: Section contains data only (no executable code).

**`ROM`**
: Section will reside in ROM.

**`CONSTRUCTOR`**
: Section contains data for constructor/destructor lists.

**`HAS_CONTENTS`**
: Section is not empty.

**`NEVER_LOAD`**
: An instruction to the linker to not output the section.

**`COFF_SHARED_LIBRARY`**
: A notification to the linker that the section contains
COFF shared library information.

**`IS_COMMON`**
: Section contains common symbols.

**`set trust-readonly-sections on`**
: Tell GDB that readonly sections in your object file
really are read-only (i.e. that their contents will not change).
In that case, GDB can fetch values from these sections
out of the object file, rather than from the target program.
For some targets (notably embedded ones), this can be a significant
enhancement to debugging performance.
The default is off.

**`set trust-readonly-sections off`**
: Tell GDB not to trust readonly sections. This means that
the contents of the section might change while the program is running,
and must therefore be fetched from the target when needed.

**`show trust-readonly-sections`**
: Show the current setting of trusting readonly sections.

All file-specifying commands allow both absolute and relative file names
as arguments. GDB always converts the file name to an absolute file
name and remembers it that way.

GDB supports GNU/Linux, MS-Windows, HP-UX, SunOS, SVr4, Irix,
IBM RS/6000 AIX and Darwin (OS X) shared libraries.

GDB automatically loads symbol definitions from shared libraries
when you use the `run` command, or when you examine a core file.
(Before you issue the `run` command, GDB does not understand
references to a function in a shared library, however--unless you are
debugging a core file).

On HP-UX, if the program loads a library explicitly, GDB
automatically loads the symbols at the time of the `shl_load` call.

There are times, however, when you may wish to not automatically load
symbol definitions from shared libraries, such as when they are
particularly large or there are many of them.

To control the automatic loading of shared library symbols, use the
commands:

**`set auto-solib-add mode`**
: 
If mode is `on`, symbols from all shared object libraries
will be loaded automatically when the inferior begins execution, you
attach to an independently started inferior, or when the dynamic linker
informs GDB that a new library has been loaded. If mode
is `off`, symbols must be loaded manually, using the
`sharedlibrary` command. The default value is `on`.

If your program uses lots of shared libraries with debug info that
takes large amounts of memory, you can decrease the GDB
memory footprint by preventing it from automatically loading the
symbols from shared libraries. To that end, type `set
auto-solib-add off` before running the inferior, then load each
library whose debug symbols you do need with `sharedlibrary
regexp`, where regexp is a regular expresion that matches
the libraries whose symbols you want to be loaded.

**`show auto-solib-add`**
: Display the current autoloading mode.

To explicitly load shared library symbols, use the `sharedlibrary`
command:

**`info share`**
: 

**`info sharedlibrary`**
: Print the names of the shared libraries which are currently loaded.

**`sharedlibrary regex`**
:

**`share regex`**
: Load shared object library symbols for files matching a
Unix regular expression.
As with files loaded automatically, it only loads shared libraries
required by your program for a core file or after typing `run`. If
regex is omitted all shared libraries required by your program are
loaded.

**`nosharedlibrary`**
: 

Unload all shared object library symbols. This discards all symbols
that have been loaded from all shared libraries. Symbols from shared
libraries that were loaded by explicit user requests are not
discarded.

Sometimes you may wish that GDB stops and gives you control
when any of shared library events happen. Use the `set
stop-on-solib-events` command for this:

**`set stop-on-solib-events`**
: 
This command controls whether GDB should give you control
when the dynamic linker notifies it about some shared library event.
The most common event of interest is loading or unloading of a new
shared library.

**`show stop-on-solib-events`**
: 
Show whether GDB stops and gives you control when shared
library events happen.

Shared libraries are also supported in many cross or remote debugging
configurations. A copy of the target's libraries need to be present on the
host system; they need to be the same as the target libraries, although the
copies on the target can be stripped as long as the copies on the host are
not.

For remote debugging, you need to tell GDB where the target
libraries are, so that it can load the correct copies--otherwise, it
may try to load the host's libraries. GDB has two variables
to specify the search directories for target libraries.

**`set solib-absolute-prefix path`**
: 

If this variable is set, path will be used as a prefix for any
absolute shared library paths; many runtime loaders store the absolute
paths to the shared library in the target program's memory. If you use
`` `solib-absolute-prefix' `` to find shared libraries, they need to be laid
out in the same way that they are on the target, with e.g. a
`/usr/lib' hierarchy under path.

You can set the default value of `` `solib-absolute-prefix' `` by using the
configure-time `` `--with-sysroot' `` option.

**`show solib-absolute-prefix`**
: Display the current shared library prefix.

**`set solib-search-path path`**
: If this variable is set, path is a colon-separated list of directories
to search for shared libraries. `` `solib-search-path' `` is used after
`` `solib-absolute-prefix' `` fails to locate the library, or if the path to
the library is relative instead of absolute. If you want to use
`` `solib-search-path' `` instead of `` `solib-absolute-prefix' ``, be sure to
set `` `solib-absolute-prefix' `` to a nonexistant directory to prevent
GDB from finding your host's libraries.

**`show solib-search-path`**
: Display the current shared library search path.

## [Debugging Information in Separate Files](Debugging%20with%20GDB.md#apple-krhugmjuha)

GDB allows you to put a program's debugging information in a
file separate from the executable itself, in a way that allows
GDB to find and load the debugging information automatically.
Since debugging information can be very large -- sometimes larger
than the executable code itself -- some systems distribute debugging
information for their executables in separate files, which users can
install only when they need to debug a problem.

If an executable's debugging information has been extracted to a
separate file, the executable should contain a __debug link__ giving
the name of the debugging information file (with no directory
components), and a checksum of its contents. (The exact form of a
debug link is described below.) If the full name of the directory
containing the executable is execdir, and the executable has a
debug link that specifies the name debugfile, then GDB
will automatically search for the debugging information file in three
places:

- the directory containing the executable file (that is, it will look
  for a file named `execdir/debugfile',
- a subdirectory of that directory named `.debug' (that is, the
  file `execdir/.debug/debugfile', and
- a subdirectory of the global debug file directory that includes the
  executable's full path, and the name from the link (that is, the file
  `globaldebugdir/execdir/debugfile', where
  globaldebugdir is the global debug file directory, and
  execdir has been turned into a relative path).

GDB checks under each of these names for a debugging
information file whose checksum matches that given in the link, and
reads the debugging information from the first one it finds.

So, for example, if you ask GDB to debug `/usr/bin/ls',
which has a link containing the name `ls.debug', and the global
debug directory is `/usr/lib/debug', then GDB will look
for debug information in `/usr/bin/ls.debug',
`/usr/bin/.debug/ls.debug', and
`/usr/lib/debug/usr/bin/ls.debug'.

You can set the global debugging info directory's name, and view the
name GDB is currently using.

**`set debug-file-directory directory`**
: 
Set the directory which GDB searches for separate debugging
information files to directory.

**`show debug-file-directory`**
: Show the directory GDB searches for separate debugging
information files.

A debug link is a special section of the executable file named
`.gnu_debuglink`. The section must contain:

- A filename, with any leading directory components removed, followed by
  a zero byte,
- zero to three bytes of padding, as needed to reach the next four-byte
  boundary within the section, and
- a four-byte CRC checksum, stored in the same endianness used for the
  executable file itself. The checksum is computed on the debugging
  information file's full contents by the function given below, passing
  zero as the crc argument.

Any executable file format can carry a debug link, as long as it can
contain a section named `.gnu_debuglink` with the contents
described above.

The debugging information file itself should be an ordinary
executable, containing a full set of linker symbols, sections, and
debugging information. The sections of the debugging information file
should have the same names, addresses and sizes as the original file,
but they need not contain any data -- much like a `.bss` section
in an ordinary executable.

As of December 2002, there is no standard GNU utility to produce
separated executable / debugging information file pairs. Ulrich
Drepper's `elfutils' package, starting with version 0.53,
contains a version of the `strip` command such that the command
`strip foo -f foo.debug` removes the debugging information from
the executable file `foo', places it in the file
`foo.debug', and leaves behind a debug link in `foo'.

Since there are many different ways to compute CRC's (different
polynomials, reversals, byte ordering, etc.), the simplest way to
describe the CRC used in `.gnu_debuglink` sections is to give the
complete code for a function that computes it:


```
unsigned long
gnu_debuglink_crc32 (unsigned long crc,
                     unsigned char *buf, size_t len)
{
  static const unsigned long crc32_table[256] =
    {
      0x00000000, 0x77073096, 0xee0e612c, 0x990951ba, 0x076dc419,
      0x706af48f, 0xe963a535, 0x9e6495a3, 0x0edb8832, 0x79dcb8a4,
      0xe0d5e91e, 0x97d2d988, 0x09b64c2b, 0x7eb17cbd, 0xe7b82d07,
      0x90bf1d91, 0x1db71064, 0x6ab020f2, 0xf3b97148, 0x84be41de,
      0x1adad47d, 0x6ddde4eb, 0xf4d4b551, 0x83d385c7, 0x136c9856,
      0x646ba8c0, 0xfd62f97a, 0x8a65c9ec, 0x14015c4f, 0x63066cd9,
      0xfa0f3d63, 0x8d080df5, 0x3b6e20c8, 0x4c69105e, 0xd56041e4,
      0xa2677172, 0x3c03e4d1, 0x4b04d447, 0xd20d85fd, 0xa50ab56b,
      0x35b5a8fa, 0x42b2986c, 0xdbbbc9d6, 0xacbcf940, 0x32d86ce3,
      0x45df5c75, 0xdcd60dcf, 0xabd13d59, 0x26d930ac, 0x51de003a,
      0xc8d75180, 0xbfd06116, 0x21b4f4b5, 0x56b3c423, 0xcfba9599,
      0xb8bda50f, 0x2802b89e, 0x5f058808, 0xc60cd9b2, 0xb10be924,
      0x2f6f7c87, 0x58684c11, 0xc1611dab, 0xb6662d3d, 0x76dc4190,
      0x01db7106, 0x98d220bc, 0xefd5102a, 0x71b18589, 0x06b6b51f,
      0x9fbfe4a5, 0xe8b8d433, 0x7807c9a2, 0x0f00f934, 0x9609a88e,
      0xe10e9818, 0x7f6a0dbb, 0x086d3d2d, 0x91646c97, 0xe6635c01,
      0x6b6b51f4, 0x1c6c6162, 0x856530d8, 0xf262004e, 0x6c0695ed,
      0x1b01a57b, 0x8208f4c1, 0xf50fc457, 0x65b0d9c6, 0x12b7e950,
      0x8bbeb8ea, 0xfcb9887c, 0x62dd1ddf, 0x15da2d49, 0x8cd37cf3,
      0xfbd44c65, 0x4db26158, 0x3ab551ce, 0xa3bc0074, 0xd4bb30e2,
      0x4adfa541, 0x3dd895d7, 0xa4d1c46d, 0xd3d6f4fb, 0x4369e96a,
      0x346ed9fc, 0xad678846, 0xda60b8d0, 0x44042d73, 0x33031de5,
      0xaa0a4c5f, 0xdd0d7cc9, 0x5005713c, 0x270241aa, 0xbe0b1010,
      0xc90c2086, 0x5768b525, 0x206f85b3, 0xb966d409, 0xce61e49f,
      0x5edef90e, 0x29d9c998, 0xb0d09822, 0xc7d7a8b4, 0x59b33d17,
      0x2eb40d81, 0xb7bd5c3b, 0xc0ba6cad, 0xedb88320, 0x9abfb3b6,
      0x03b6e20c, 0x74b1d29a, 0xead54739, 0x9dd277af, 0x04db2615,
      0x73dc1683, 0xe3630b12, 0x94643b84, 0x0d6d6a3e, 0x7a6a5aa8,
      0xe40ecf0b, 0x9309ff9d, 0x0a00ae27, 0x7d079eb1, 0xf00f9344,
      0x8708a3d2, 0x1e01f268, 0x6906c2fe, 0xf762575d, 0x806567cb,
      0x196c3671, 0x6e6b06e7, 0xfed41b76, 0x89d32be0, 0x10da7a5a,
      0x67dd4acc, 0xf9b9df6f, 0x8ebeeff9, 0x17b7be43, 0x60b08ed5,
      0xd6d6a3e8, 0xa1d1937e, 0x38d8c2c4, 0x4fdff252, 0xd1bb67f1,
      0xa6bc5767, 0x3fb506dd, 0x48b2364b, 0xd80d2bda, 0xaf0a1b4c,
      0x36034af6, 0x41047a60, 0xdf60efc3, 0xa867df55, 0x316e8eef,
      0x4669be79, 0xcb61b38c, 0xbc66831a, 0x256fd2a0, 0x5268e236,
      0xcc0c7795, 0xbb0b4703, 0x220216b9, 0x5505262f, 0xc5ba3bbe,
      0xb2bd0b28, 0x2bb45a92, 0x5cb36a04, 0xc2d7ffa7, 0xb5d0cf31,
      0x2cd99e8b, 0x5bdeae1d, 0x9b64c2b0, 0xec63f226, 0x756aa39c,
      0x026d930a, 0x9c0906a9, 0xeb0e363f, 0x72076785, 0x05005713,
      0x95bf4a82, 0xe2b87a14, 0x7bb12bae, 0x0cb61b38, 0x92d28e9b,
      0xe5d5be0d, 0x7cdcefb7, 0x0bdbdf21, 0x86d3d2d4, 0xf1d4e242,
      0x68ddb3f8, 0x1fda836e, 0x81be16cd, 0xf6b9265b, 0x6fb077e1,
      0x18b74777, 0x88085ae6, 0xff0f6a70, 0x66063bca, 0x11010b5c,
      0x8f659eff, 0xf862ae69, 0x616bffd3, 0x166ccf45, 0xa00ae278,
      0xd70dd2ee, 0x4e048354, 0x3903b3c2, 0xa7672661, 0xd06016f7,
      0x4969474d, 0x3e6e77db, 0xaed16a4a, 0xd9d65adc, 0x40df0b66,
      0x37d83bf0, 0xa9bcae53, 0xdebb9ec5, 0x47b2cf7f, 0x30b5ffe9,
      0xbdbdf21c, 0xcabac28a, 0x53b39330, 0x24b4a3a6, 0xbad03605,
      0xcdd70693, 0x54de5729, 0x23d967bf, 0xb3667a2e, 0xc4614ab8,
      0x5d681b02, 0x2a6f2b94, 0xb40bbe37, 0xc30c8ea1, 0x5a05df1b,
      0x2d02ef8d
    };
  unsigned char *end;

  crc = ~crc & 0xffffffff;
  for (end = buf + len; buf < end; ++buf)
    crc = crc32_table[(crc ^ *buf) & 0xff] ^ (crc >> 8);
  return ~crc & 0xffffffff;
}
```

## [Errors reading symbol files](Debugging%20with%20GDB.md#apple-krhugmjuhe)

While reading a symbol file, GDB occasionally encounters problems,
such as symbol types it does not recognize, or known bugs in compiler
output. By default, GDB does not notify you of such problems, since
they are relatively common and primarily of interest to people
debugging compilers. If you are interested in seeing information
about ill-constructed symbol tables, you can either ask GDB to print
only one message about each such type of problem, no matter how many
times the problem occurs; or you can ask GDB to print more messages,
to see how many times the problems occur, with the `set
complaints` command (see section [Optional warnings and messages](Controlling%20GDB.md#apple-kncugmrsge)).

The messages currently printed, and their meanings, include:

**`inner block not inside outer block in symbol`**
: The symbol information shows where symbol scopes begin and end
(such as at the start of a function or a block of statements). This
error indicates that an inner scope block is not fully contained
in its outer scope blocks.
GDB circumvents the problem by treating the inner block as if it had
the same scope as the outer block. In the error message, symbol
may be shown as "`(don't know)`" if the outer block is not a
function.

**`block at address out of order`**
: The symbol information for symbol scope blocks should occur in
order of increasing addresses. This error indicates that it does not
do so.
GDB does not circumvent this problem, and has trouble
locating symbols in the source file whose symbols it is reading. (You
can often determine what source file is affected by specifying
`set verbose on`. See section [Optional warnings and messages](Controlling%20GDB.md#apple-kncugmrsge).)

**`bad block start address patched`**
: The symbol information for a symbol scope block has a start address
smaller than the address of the preceding source line. This is known
to occur in the SunOS 4.1.1 (and earlier) C compiler.
GDB circumvents the problem by treating the symbol scope block as
starting on the previous source line.

**`bad string table offset in symbol n`**
: 
Symbol number n contains a pointer into the string table which is
larger than the size of the string table.
GDB circumvents the problem by considering the symbol to have the
name `foo`, which may cause other problems if many symbols end up
with this name.

**`unknown symbol type 0xnn`**
: The symbol information contains new data types that GDB does
not yet know how to read. `0xnn` is the symbol type of the
uncomprehended information, in hexadecimal.
GDB circumvents the error by ignoring this symbol information.
This usually allows you to debug your program, though certain symbols
are not accessible. If you encounter such a problem and feel like
debugging it, you can debug `gdb` with itself, breakpoint
on `complain`, then go up to the function `read_dbx_symtab`
and examine `*bufp` to see the symbol.

**`stub type has NULL name`**
: GDB could not find the full definition for a struct or class.

**`const/volatile indicator missing (ok if using g++ v1.x), got...`**
: The symbol information for a C++ member function is missing some
information that recent versions of the compiler should have output for
it.

**`info mismatch between compiler and debugger`**
: GDB could not parse a type specification output by the compiler.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Altering%20Execution.md), [next](Specifying%20a%20Debugging%20Target.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
