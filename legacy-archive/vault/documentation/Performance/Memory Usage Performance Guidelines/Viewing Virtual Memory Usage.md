---
title: Memory Usage Performance Guidelines
apple_id: 10000160i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Performance
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/VMPages.html
archived_at: '2026-07-18T01:48:55.291020Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Usage Performance Guidelines](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Enabling%20the%20Malloc%20Debugging%20Features.md)

# Viewing Virtual Memory Usage

If you need more detailed information about virtual memory usage, you can use the `top`, `vm_stat`, `pagestuff`, and `vmmap` command-line tools for analyzing your Mac apps. The information returned by these tools ranges from summary information about all the system processes to detailed information about a specific process.

The following sections provide information on using the `vm_stat`, `pagestuff`, and `vmmap` tools to gather detailed memory information. For more information on using Instruments to analyze memory, see _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_ and the other articles in this document. For information on how to use the `top` tool, see _[Performance Overview](../Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq)_.

The `vm_stat` tool displays high-level statistics about the current virtual memory usage of the system. By default, `vm_stat` displays these statistics once, but you can specify an interval value (in seconds) to update these statistics continuously. For information on the usage of this tool, see the `vm_stat` man page.

Listing 1 shows an example of the output from `vm_stat`.

__Listing 1__  Output of vm_stat tool

```
Mach Virtual Memory Statistics: (page size of 4096 bytes)
Pages free:                     3194.
Pages active:                  34594.
Pages inactive:                17870.
Pages wired down:               9878.
"Translation faults":        6333197.
Pages copy-on-write:           81385.
Pages zero filled:           3180051.
Pages reactivated:            343961.
Pageins:                       33043.
Pageouts:                      78496.
Object cache: 66227 hits of 96952 lookups (68% hit rate)
```


The `pagestuff`tool displays information about the specified logical pages of a file conforming to the Mach-O executable format. For each specified page of code, symbols (function and static data structure names) are displayed. All pages in the `__TEXT, __text` section are displayed if no page numbers are given.

Listing 2 shows part of the output from `pagestuff` for the TextEdit application. This output is the result of running the tool with the `-a` option, which prints information about all of the executable’s code pages. It includes the virtual address locations of each page and the type of information on that page.

__Listing 2__  Partial output of pagestuff tool

```
File Page 0 contains Mach-O headers
File Page 1 contains Mach-O headers
File Page 2 contains contents of section (__TEXT,__text)
Symbols on file page 2 virtual address 0x3a08 to 0x4000
File Page 3 contains contents of section (__TEXT,__text)
Symbols on file page 3 virtual address 0x4000 to 0x5000
File Page 4 contains contents of section (__TEXT,__text)
Symbols on file page 4 virtual address 0x5000 to 0x6000

...

File Page 22 contains contents of section (__TEXT,__cstring)
File Page 22 contains contents of section (__TEXT,__literal4)
File Page 22 contains contents of section (__TEXT,__literal8)
File Page 22 contains contents of section (__TEXT,__const)
Symbols on file page 22 virtual address 0x17000 to 0x17ffc
File Page 23 contains contents of section (__DATA,__data)
File Page 23 contains contents of section (__DATA,__la_symbol_ptr)
File Page 23 contains contents of section (__DATA,__nl_symbol_ptr)
File Page 23 contains contents of section (__DATA,__dyld)
File Page 23 contains contents of section (__DATA,__cfstring)
File Page 23 contains contents of section (__DATA,__bss)
File Page 23 contains contents of section (__DATA,__common)
Symbols on file page 23 virtual address 0x18000 to 0x18d48
 0x00018000 _NXArgc
 0x00018004 _NXArgv
 0x00018008 _environ
 0x0001800c ___progname
...
```

In the preceding listing, if a page exports any symbols, those symbols are also displayed by the `-a` option. If you want to view the symbols for a single page, pass in the desired page number instead of the `-a` option. For more information about the `pagestuff` tool and its supported options, see the `pagestuff` man page.

The `vmmap` and `vmmap64` tools display the virtual memory regions allocated for a specified process. These tools provide access to the virtual memory of 32-bit and 64-bit applications, respectively. You can use them to understand the purpose of memory at a given address and how that memory is being used. For each virtual-memory region, these tools display the type of page, the starting address, region size (in kilobytes), read/write permissions, sharing mode, and the purpose of the pages in that region.

The following sections show you how to interpret the output from the `vmmap` tool. For more information about the `vmmap` and `vmmap64` tools, see the `vmmap` or `vmmap64` man pages.

Listing 3 shows some sample output from the `vmmap` tool. This example is not a full listing of the tool’s output but is an abbreviated version showing the primary sections.

__Listing 3__  Typical output of vmmap

```
==== Non-writable regions for process 313
__PAGEZERO              0 [   4K] ---/--- SM=NUL ...ts/MacOS/Clock
__TEXT               1000 [  40K] r-x/rwx SM=COW ...ts/MacOS/Clock
__LINKEDIT           e000 [   4K] r--/rwx SM=COW ...ts/w/Clock
                    90000 [   4K] r--/r-- SM=SHM
                   340000 [3228K] r--/rwx SM=COW 00000100 00320...
                   789000 [3228K] r--/rwx SM=COW 00000100 00320...
Submap           90000000-9fffffff r--/r-- machine-wide submap
__TEXT           90000000  [ 932K] r-x/r-x SM=COW /usr/lib/libSystem.B.dylib
__LINKEDIT       900e9000   [ 260K] r--/r-- SM=COW /usr/lib/libSystem.B.dylib
__TEXT           90130000 [ 740K] r-x/r-x SM=COW .../Versions/A/CoreFoundation
__LINKEDIT       901e9000 [ 188K] r--/r-- SM=COW .../Versions/A/CoreFoundation
__TEXT           90220000 [2144K] r-x/r-x SM=COW .../Versions/A/CarbonCore
__LINKEDIT       90438000 [ 296K] r--/r-- SM=COW .../Versions/A/CarbonCore

[...data omitted...]

==== Writable regions for process 606
__DATA             18000 [   4K] rw-/rwx SM=PRV /Contents/MacOS/TextEdit
__OBJC             19000 [   8K] rw-/rwx SM=COW /Contents/MacOS/TextEdit
MALLOC_OTHER       1d000 [ 256K] rw-/rwx SM=PRV
MALLOC_USED(DefaultMallocZone_0x5d2c0)     5d000 [ 256K] rw-/rwx SM=PRV
                   9d000 [ 372K] rw-/rwx SM=COW 33320000 00000020 00000000 00001b84...
VALLOC_USED(DefaultMallocZone_0x5d2c0)     ff000 [  36K] rw-/rwx SM=PRV
MALLOC_USED(CoreGraphicsDefaultZone_0x10  108000 [ 256K] rw-/rwx SM=PRV
MALLOC_USED(CoreGraphicsRegionZone_0x148  148000 [ 256K] rw-/rwx SM=PRV

[...data omitted...]

Submap           a000b000-a012ffff r--/r-- process-only submap
__DATA           a0130000 [  28K] rw-/rw- SM=COW .../Versions/A/CoreFoundation
Submap           a0137000-a021ffff r--/r-- process-only submap
__DATA           a0220000 [  20K] rw-/rw- SM=COW .../Versions/A/CarbonCore
Submap           a0225000-a048ffff r--/r-- process-only submap
__DATA           a0490000 [  12K] rw-/rw- SM=COW .../IOKit.framework/Versions/A/IOKit
Submap           a0493000-a050ffff r--/r-- process-only submap
__DATA           a0510000 [  36K] rw-/rw- SM=COW .../Versions/A/OSServices
                 b959e000 [   4K] rw-/rw- SM=SHM
                 b95a0000 [   4K] rw-/rw- SM=SHM
                 b9630000 [ 164K] rw-/rw- SM=SHM
                 b965a000 [ 896K] rw-/rw- SM=SHM
                 bff80000 [ 504K] rw-/rwx SM=ZER
STACK[0]         bfffe000 [   4K] rw-/rwx SM=PRV
                 bffff000 [   4K] rw-/rwx SM=PRV
__DATA           c000c000 [   4K] rw-/rwx SM=PRV .../Versions/A/ApplicationEnhancer
STACK[1]         f0001000 [ 512K] rw-/rwx SM=PRV
                 ff002000 [12272K] rw-/rw- SM=SHM

==== Legend
SM=sharing mode:
    COW=copy_on_write PRV=private NUL=empty ALI=aliased
    SHM=shared ZER=zero_filled S/A=shared_alias

==== Summary for process 313
ReadOnly portion of Libraries: Total=27420KB resident=12416KB(45%) swapped_out_or_unallocated=15004KB(55%)
Writable regions: Total=21632KB written=536KB(2%) resident=1916KB(9%) swapped_out=0KB(0%) unallocated=19716KB(91%)
```

If you specify the `-d` parameter (plus an interval in seconds), `vmmap` takes two snapshots of virtual-memory usage—one at the beginning of a specified interval and the other at the end—and displays the differences. It shows three sets of differences:

- individual differences
- regions in the first snapshot that are not in the second
- regions in the second snapshot that are not in the first

The columns of `vmmap` output have no headings. Instead you can interpret the type of data in each column by its format. Table 1 describes these columns.

__Table 1__  Column descriptions for vmmap

| Column Number | Example | Description |
| 1 | `__TEXT`, `__LINKEDIT`, `MALLOC_USED`, `STACK`, and so on | The purpose of the memory. This column can contain the name of a Mach-O segment or the memory allocation technique. |
| 2 | `(DefaultMallocZone_0x5d2c0)` | If present, the zone used for allocation. |
| 3 | `4eee000` | The virtual memory address of the region. |
| 4 | `[ 124K]` | The size of the region, measured in kilobytes |
| 5 | `rw-/rwx` | Read, write and execution permissions for the region. The first set of flags specifies the current protection for the region. The second set of values specifies the maximum protection for the region. If an entry contains a dash (`-`), the process does not have the target permission. |
| 6 | `SM=PRV` | Sharing mode for the region, either `COW` (copy-on-write), `PRV` (private), `NUL` (empty), `ALI` (aliased), or `SHM` (shared). |
| 7 | `...ts/MacOS/Clock` | The end of the pathname identifying the executable mapped into this region of virtual memory. If the region is stack or heap memory, nothing is displayed in this column. |

Column 1 identifies the purpose of the memory. A `__TEXT` segment contains read-only code and data. A `__DATA` segment contains data that may be both readable and writable. For allocated data, this column shows how the memory was allocated, such as on the stack, using `malloc`, and so on. For regions loaded from a library, the far right column shows the name of the library loaded into memory.

The size of the virtual memory region (column 4) represents the total size reserved for that region. This number may not reflect the actual number of memory pages allocated for the region. For example, calling `vm_allocate` reserves a set of memory pages but does not allocate any physical memory until the pages are actually touched. Similarly, a memory-mapped file may reserve a set of pages, but the system does not load pages until a read or write event occurs on the file.

The protection mode (column 5) describes the access restrictions for the memory region. A memory region contains separate flags for read, write, and execution permissions. Each virtual memory region has a current permission, and a maximum permission. In the output from `vmmap`, the current permission appears first followed by the maximum permission. Thus, if the permissions are “`r--/rwx`“ the page is currently read-only but allows read, write, and execution access as its maximum allowed permissions. Typically, the current permissions do not permit writing to a region. However, these permissions may change under certain circumstances. For example, a debugger may request write access to a page in order to set a breakpoint.

The sharing mode (`SM=` field) tells you whether pages are shared between processes and what happens when pages are modified. Private pages (`PRV`) are visible only to the process and are allocated as they are used. Private pages can also be paged out to disk. Copy-on-write (`COW`) pages are shared by multiple processes (or shared by a single process in multiple locations). When the page is modified, the writing process then receives its own copy of the page. Empty (`NUL`) sharing implies that the page does not really exist in physical memory. Aliased (`ALI`) and shared (`SHM`) memory are shared between processes.

The sharing mode typically describes the general mode controlling the region. For example, as copy-on-write pages are modified, they become private to the application. However, the region containing those private pages is still copy-on-write until all pages become private. Once all pages are private, the sharing mode changes to private.

Some lines in the output of `vmmap` describe submaps. A submap is a shared set of virtual memory page descriptions that the operating system can reuse between multiple processes. For example, the memory between `0x90000000` and `0xAFFFFFFF` is a submap containing the most common dynamic libraries. Submaps minimize the operating system’s memory usage by representing the virtual memory regions only once. Submaps can either be shared by all processes (machine-wide) or be local to the process (process-only). If the contents of a machine-wide submap are changed—for example, the debugger makes a section of memory for a dynamic library writable so it can insert debugging traps—then the submap becomes local, and the kernel allocates memory to store the extra copy.

[Next](Document%20Revision%20History.md)[Previous](Enabling%20the%20Malloc%20Debugging%20Features.md)

