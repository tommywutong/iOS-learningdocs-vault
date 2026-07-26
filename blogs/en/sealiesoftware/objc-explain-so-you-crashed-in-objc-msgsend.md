---
title: '[objc explain]: So you crashed in objc_msgSend()'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html'
original_language: en
published: 2008-09-22
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c6cf68bad0382d80'
translated: false
---

> 原文：[[objc explain]: So you crashed in objc_msgSend()](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

\<\< [Valgrind for Mac OS X (some assembly required)](http://sealiesoftware.com/blog/archive/2008/09/28/Valgrind_for_Mac_OS_X_some_assembly_required.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Exceptions and autorelease pools](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html)

**[objc explain]: So you crashed in objc_msgSend()** ([2008-09-22 02:02 PM](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html))

So you crashed in `objc_msgSend()`. Now what?

Most likely, you sent a message to an already-freed object. Or maybe your pointer is perfectly correct, but someone else mangled the object's contents - perhaps a buffer overrun in a nearby allocation, or use of a dangling pointer that once pointed to the memory now occupied by your object. Occasionally `objc_msgSend()` crashes because a memory error smashed the runtime's own data structures, but usually the trouble is in the receiver object itself.

Whether you're in the debugger or looking at a crash log, you can recover more information about the crash than just the backtrace.

#### Receiver and selector registers

`objc_msgSend()` stores the receiver object and the selector in CPU registers while it works. These values can help diagnose the problem.

The register names differ based on architecture and the `objc_msgSend()` variant used. This list is correct for Mac OS X Leopard and will probably remain correct for Snow Leopard.

|  | `receiver` | `SEL` | `receiver` | `SEL` |
|---|---|---|---|---|
| i386 | eax* | ecx | eax* | ecx |
| x86_64 | rdi | rsi | rsi | rdx |
| ppc | r3 | r4 | r4 | r5 |
| ppc64 | r3 | r4 | r4 | r5 |
| arm | r0 | r1 | r1 | r2 |
| arm64 | x0 | x1 | — | — |

* i386 note: The receiver is in eax for most crashes, but not all. If you manage to get far into `objc_msgSend()` before falling over, then eax will have some other value.

#### Interpreting the receiver and invalid address

You can use the receiver's address and the invalid address that caused the crash to get some hints about the underlying problem. In a crash log, the receiver's address is in the Thread State using the register name in the table above, and the invalid address is listed at the top (usually something like `KERN_PROTECTION_FAILURE at <invalid address>`). In the debugger console, the invalid address is printed when the program stops, and you can print the receiver's address using the register name in the table above.

```
    Program received signal EXC_BAD_ACCESS, Could not access memory.
    Reason: KERN_PROTECTION_FAILURE at address: 0x00000001
    0x00090ec4 in objc_msgSend ()
    (gdb) p/x $eax
    $1 = 0x1
```

My test program crashed at `[(id)1 release]`. In real crashes, these values are typically more interesting.

Usually, one of two things happens. The receiver address itself is bogus, and the invalid address is the same value (or 16 or 32 bytes away). Or the receiver address is reasonable, and the invalid address is the receiver's `isa` pointer. The latter is what usually happens if you try to use an already-deallocated object or someone else clobbered your valid object.

Look for special values like these in your crashes. Also look for nearby values; on some architectures, an invalid `isa` will cause a crash at `isa+16` or `isa+32` instead.

Not divisble by 16 - misaligned `malloc()` returns 16-byte aligned blocks. If your receiver isn't 16-byte aligned, it probably never was a valid object pointer. Top two and bottom two bits all set - malloc free list After a block is freed, the memory allocator may write free list pointers into it. If you use a freed object after this, you'll see an `isa` pointer with the top two and bottom two bits all set. All bits inverted - GC free list Like the malloc free list case above, but caused by the garbage collector instead. In this case `address` looks bad, but `~address` is more reasonable. 0xa1b1c1d3 - CF container CoreFoundation containers use this value for deleted or empty items. Perhaps a freed object has been re-allocated as a container, or someone used a freed container that has been re-allocated as your object, or you read your pointer from a container that was simultaneously changed by some other thread and you don't have the right locks in place. ASCII text Perhaps a freed object has been re-allocated as a string, or someone used a freed string that has been re-allocated as your object, or some string operation has a buffer overrun. Use [asciify](http://sealiesoftware.com/asciify.c) to print these quickly in both endians. This one looks URL-related, for example:  % asciify 0x2e777777 ###.www### ###www.###

#### Interrogating the selector

Compiler optimization means the call site pointed to by the second frame in the backtrace might not be the call that actually crashed. It's possible that call succeeded, and then that method made a _tail call_ which was the one that crashed. Because of tail call optimization, the intermediate frame would be missing from the backtrace. We can use the selector register to determine what the real crashing call was.

A selector is a pointer to a unique C string. This may change in future OS versions, but for now it's handy for debugging. If you have crashed in a debugger, open the debugger console and run this, substituting the correct `SEL` register from the table above:

```
    (gdb) x/s $ecx
    0xa1029: "release"
```

Snow Leopard's crash reporter adds selector names to crash logs for you:

```
    Application Specific Information:
    objc_msgSend() selector name: release
```

Otherwise, retrieving the selector name from just a crash log is difficult and doesn't always work. Until you have Snow Leopard, cross your fingers and try this.

1. From the crash log's Thread State, find the `SEL`'s value using the register name in the table above.

  ```
      ecx: 0x000a1029
  ```
2. From the crash log's Binary Images, find the image whose address range includes the `SEL`'s value. This will often be either the application itself or `libobjc.A.dylib`. If no image spans that address, give up.   
  `    0x8b000 -   0x106ff7  libobjc.A.dylib ??? (???) <9b5973b7fa88f9aab7885530c7b278dd> /usr/lib/libobjc.A.dylib`
3. Find a copy of the image that matches the one in the crash log. Use the UUID to verify the match.

  ```
      % dwarfdump -u /usr/lib/libobjc.A.dylib
      UUID: 26650299-C6EA-B1C8-52D6-072AC874D400 (ppc) /usr/lib/libobjc.A.dylib
      UUID: 9B5973B7-FA88-F9AA-B788-5530C7B278DD (i386) /usr/lib/libobjc.A.dylib
      UUID: D2A4E8E1-3C1C-E0D9-2249-125B6DD621F8 (x86_64) /usr/lib/libobjc.A.dylib
  ```

  This crash matches my installed `libobjc.A.dylib` for i386. If it's a system library, you may need the image from the OS version listed in the crash log. If it's your application, you did keep a copy of every version you shipped, right?

  ```

  ```
4. Calculate the `SEL`'s offset into the image.

  ```
      0xa1029 - 0x8b000 = 0x16029
  ```
5. Print the C string in the image at that offset. Remember to specify the correct architecture.

  ```
      % otool -v -arch i386 -s __TEXT __cstring /usr/lib/libobjc.A.dylib | grep 16029
      00016029  release
  ```

[Sealie Software](http://sealiesoftware.com/index.html)
