---
title: Dr. Gregory Parker, Department of Diagnostic Engineering
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html'
original_language: en
published: 2010-09-01
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b2e9d15da102f884'
translated: false
---

> 原文：[Dr. Gregory Parker, Department of Diagnostic Engineering](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: objc_msgSend_vtable](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [TargetConditionals.h](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html)

**Dr. Gregory Parker, Department of Diagnostic Engineering** ([2010-09-01 3:15 AM](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html))

Last week, [Rick Ballard](http://twitter.com/rballard) came by my office for a consult. He had caught Xcode at a crash in `objc_msgSend()`. The crash looked like an intermittent problem that had been plaguing Xcode for months. So he called the local expert on debugging `objc_msgSend()`. Dr. Gregory Parker, Department of Diagnostic Engineering.

The good news was that Rick's crash was reliably reproducible. Running tests on a live patient is better than performing an autopsy on a dead one. The bad news was that the obvious debugging tools had not helped. `NSZombieEnabled` and `guardmalloc` had turned up nothing, and `AUTO_USE_GUARDS=YES` (the GC equivalent of `guardmalloc`) just thrashed the machine for two hours before running out of address space.

[So you crashed in `objc_msgSend()`](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html). The selector was `-isAbsolutePath`, which was reasonable but meant the debugger's backtrace was missing a frame. `objc_msgSend()` had read the class from the object, read the method cache from the class, read a method from the method cache, and crashed while trying to read the `IMP` from the method. Theory: either one of those data structures had been hit by a memory smasher, or the original object was bogus but happened to have dereferenceable pointers in the right places to survive that long. The method cache's mask was invalid - it should have been of the form 2^n-1 - so the failure must have been at or before that point in the chain.

The object pointer itself looked plausible. Theory: the object was valid, but a previous object at the same location had been used after being freed. We had the great luxury of a reproducible crash, so we turned on `MallocStackLoggingNoCompact` and ran it again. That memory had only been used for one object, and it had not been deallocated. So the evidence did not support the use-after-free theory. But the history showed that the object had been allocated as an `NSPathStore2` - an internal subclass of `NSString` for file pathnames - which matched the selector `-isAbsolutePath` and matched the call site's expectations. The theory that the object pointer was valid looked good.

The object pointer was good, and the method cache was not: the failure was on the chain between them. The contents of the object looked good. The bytes looked like alternating zero and ASCII, which is a dead giveaway for the UTF-16 used inside `NSString`. The string value decoded as `@"/Xcode4/usr/bin/llvm-gcc"`, which made sense in the call site's context.

The object's `isa` pointer was not so good. Its value was `0xa0050000`. This was not class `NSPathStore2` or any other class. `vmmap` showed it to be in Foundation's data segment, and `otool` showed it was specifically in Foundation's constant CF strings. But instead of pointing to the start of some string, it pointed to the middle of a string object. That string object was `@"tzm-Latn"`: some localization thingy, perhaps? Theory: some bug had replaced this object's isa pointer with a pointer to the middle of an unrelated localization string object. This did not sound like a good theory.

Go back to the board. Symptom: the object was allocated as an `NSPathStore2`. Symptom: the object's `isa` pointer is now `0xa0050000`, which is not `NSPathStore2`. What should the `isa` pointer's value have been? `otool` and `objc_getClass()` agreed: the correct `isa` pointer should have been `0xa005f198`. `0xa0050000` is suspiciously similar. Theory: something had cleared two bytes of this object, leaving a nonsense `isa` pointer. `@"tzm-Latn"` was a red herring.

Aha! This is 32-bit i386. Little endian. The pointer `0xa005f198` is stored backwards in memory: `0x98 0xf1 0x05 0xa0`. Clearing the least-significant bytes of the `isa` pointer meant clearing bytes 0 and 1 of the object, not bytes 2 and 3. Damage to bytes 0 and 1 is exactly what you'd expect from a two-byte overrun of the object preceding this one in memory. Theory: the bug was in that preceding object, and this `NSPathStore2` object was an innocent victim.

`malloc_history` works with a pointer to the middle of an allocation, too. We plugged in `object-1` and got back an instance of `DVTSourceModelItem`, not deallocated. Rick recognized this as part of Xcode's indexer, which was always running in another thread at the time of the crash. A buffer overrun from the `DVTSourceModelItem` object fit the symptoms.

But where was the buffer? I had expected an overrun in some heap-allocated C array, not an ordinary object. Nor did `DVTSourceModelItem` have any C arrays in its instance variables.

Theory: the compiler or runtime had allocated too little memory for the instance of class `DVTSourceModelItem`, and ordinary ivar access had overrun that allocation. It was a long shot, but easy to test. `malloc_size()` and `class_getInstanceSize()` and an eyeball count of ivars all agreed that the object was 32 bytes. Theory disproved.

We tested the overrun theory again. Add an unused ivar to the end of `DVTSourceModelItem`, recompile, and run it. No crash. Remove the ivar. Crash. The extra ivar "fixed" the bug. The buffer overrun theory still fit the evidence, but we couldn't find it.

No more ideas. We needed data. Debugger watchpoints were out: there were thousands of instances of `DVTSourceModelItem`, and we couldn't watch two bytes after each of them. We were not yet desperate enough to try brute force code inspection. `AUTO_USE_GUARDS=YES` could catch it, if it didn't fall over first. Since we had a suspect in mind, we could play the `guardmalloc` trick ourselves with a narrower target. Override `+[DVTSourceModelItem alloc]`, `mprotect()` the page after the allocation, and cross our fingers really hard hoping that it still reproduced after changing the timing so much.

Bang! It crashed (good) somewhere new (also good). `DVTSourceModelItem` `-init` was writing to one of its own instance variables. The ivar was a bit in a bitfield, and that bitfield was at the end of the ivar list.

Disassemble. The generated code read 4 bytes around the bit into a register, change the bit in that register, and wrote the 4 bytes back to memory. That's typical for a bitfield. The unexpected part was that the 4 bytes spanned the last two bytes of the object and the first two bytes after the object. That's a bug. Most of the time the out of bounds access is invalid - it reads two bytes it shouldn't, and writes back the same value. But if there's another thread it can crash:

| Thread 1 | Thread 2 |
|---|---|
| reads four bytes, including two bytes outside the object |  |
|  | allocates a new object |
|  | writes an isa pointer |
| writes four bytes, clobbering the new value written by Thread 2 |  |
|  | crashes |

Theory: a compiler bug generated bad code for `DVTSourceModelItem`'s bitfield ivar, causing a read-modify-write out of bounds by two bytes, which corrupted memory in other threads. Test: try a different compiler. `DVTSourceModelItem.m` was built with `clang`, so we recompiled with `llvm-gcc`. No crash, and the disassembly looked correct. Compile with `clang` again, crash again.

Diagnosis: `clang` compiler bug in bitfield ivars. The patient's symptoms were treated with an extra ivar in `DVTSourceModelItem` until a compiler transplant could be performed.

Elapsed time: about three hours. Too long for an episode of a TV procedural drama, unfortunately.

[Sealie Software](http://sealiesoftware.com/index.html)
