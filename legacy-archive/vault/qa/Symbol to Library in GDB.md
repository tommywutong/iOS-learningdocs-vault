---
title: Symbol to Library in GDB
apple_id: DTS10003450
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-10-28'
source_url: https://developer.apple.com/library/archive/qa/qa1388/_index.html
archived_at: '2026-07-18T02:30:29.545820Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1388

# Symbol to Library in GDB

## Q:  I'm debugging with GDB. If I know the address of a symbol, how can I find the shared library that contains it?

A: You can do this by passing the address to GDB's `info sharedlibrary` command. Listing 1 shows an example of doing this for the symbol `CFRunLoopRun`.

__Listing 1__  Finding a symbol's shared library

```
$ gdb
GNU gdb 6.3.50-20050815 (Apple version gdb-1518) [...]
(gdb) attach Finder
Attaching to process 159.
Reading symbols for shared libraries [...] done
0x00007fff8041ed7a in mach_msg_trap ()
(gdb) p/a &CFRunLoopRun
$1 = 0x7fff86cf1b00 <CFRunLoopRun>
(gdb) info shared 0x7fff86cf1b00
 27 CoreFoundation               F 0x7fff86ca6000        dyld Y Y \
/System/Library/Frameworks/CoreFoundation.framework/Versions/A/\
CoreFoundation at 0x7fff86ca6000 (offset 0x7fff86ca6000)
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-10-28 | Updated to show a more modern example of this technique. |
| 2004-11-15 | New document that shows how to find the library containing a symbol in GDB. |

