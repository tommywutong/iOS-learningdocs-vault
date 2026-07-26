---
title: '[objc explain]: Non-pointer isa'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html'
original_language: en
published: 2013-09-24
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c74d10bd60d32670'
translated: false
---

> 原文：[[objc explain]: Non-pointer isa](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Objective-C and fork() in macOS 10.13](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: So you crashed in objc_msgSend(): iPhone 5s Edition](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html)

**[objc explain]: Non-pointer isa** ([2013-09-24 1:27 AM](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html))

On iOS for arm64, the isa field of Objective-C objects is no longer a pointer.

#### Say what?

On iOS for arm64, the isa field of Objective-C objects is no longer a pointer.

#### If it's not a pointer anymore, what is it?

Some of the bits still encode the pointer to the object's class. But neither OS X nor iOS actually uses all 64 bits of virtual address space. The Objective-C runtime may use these extra bits to store per-object data like its retain count or whether it has been weakly referenced.

#### Why change it?

Performance. Re-purposing these otherwise unused bits increases speed and decreases memory size. On iOS 7 the focus is on optimizing retain/release and alloc/dealloc.

#### What does this mean for my code?

Don't read `obj->isa` directly. The compiler will complain if you do. Trust the Compiler. The Compiler is your friend. Use `[obj class]` or `object_getClass(obj)` instead.

Don't write `obj->isa` directly. Use `object_setClass()` instead.

If you override `+allocWithZone:`, you may initialize your object's isa field to a "raw" isa pointer. If you do, no extra data will be stored in that isa field and you may suffer the slow path through code like retain/release. To enable these optimizations, instead set the isa field to zero (if it is not already) and then call `object_setClass()`.

If you override retain/release to implement a custom inline retain count, consider removing that code in favor of the runtime's implementation.

The 64-bit iOS simulator currently does not use non-pointer isa. Test your code on a real arm64 device.

#### What does this mean for debugging?

The debugger knows how to decode the class from the isa field. You should not need to examine it directly in most cases.

You can run your code with environment variable `OBJC_DISABLE_NONPOINTER_ISA=YES` to disable non-pointer isa for all classes. If your code works with this set and fails without it, you may be incorrectly accessing an isa field directly somewhere.

If you are writing a debugger-like tool, the Objective-C runtime exports some variables to help decode isa fields. `objc_debug_isa_class_mask` describes which bits are the class pointer: `(isa & class_mask) == `class pointer. `objc_debug_isa_magic_mask` and `objc_debug_isa_magic_value` describe some bits that help distinguish valid isa fields from other invalid values: `(isa & magic_mask) == magic_value` for isa fields that are not raw class pointers. These variables may change in the future so do not use them in application code.

#### No seriously, what do each of the bits mean?

For entertainment purposes only. These values will change in future OS versions. I think they already have changed, actually.

| (LSB) |  |  |  |
|---|---|---|---|
| 1 | bit | `indexed` | `0` is raw isa, `1` is non-pointer isa. |
| 1 | bit | `has_assoc` | Object has or once had an associated reference. Object with no associated references can deallocate faster. |
| 1 | bit | `has_cxx_dtor` | Object has a C++ or ARC destructor. Objects with no destructor can deallocate faster. |
| 30 | bits | `shiftcls` | Class pointer's non-zero bits. |
| 9 | bits | `magic` | Equals `0xd2`. Used by the debugger to distinguish real objects from uninitialized junk. |
| 1 | bit | `weakly_referenced` | Object is or once was pointed to by an ARC weak variable. Objects not weakly referenced can deallocate faster. |
| 1 | bit | `deallocating` | Object is currently deallocating. |
| 1 | bit | `has_sidetable_rc` | Object's retain count is too large to store inline. |
| 19 | bits | `extra_rc` | Object's retain count above 1. (For example, if `extra_rc` is 5 then the object's real retain count is 6.) |
| (MSB) |  |  |  |

[Sealie Software](http://sealiesoftware.com/index.html)
