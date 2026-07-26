---
title: '[objc explain]: objc_msgSend_fpret'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html'
original_language: en
published: 2008-11-16
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:79531377e20c0805'
translated: false
---

> 原文：[[objc explain]: objc_msgSend_fpret](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Infinity isn't as long as you think](http://sealiesoftware.com/blog/archive/2008/11/30/Infinity_isnt_as_long_as_you_think.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: objc_msgSend_stret](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html)

**[objc explain]: objc_msgSend_fpret** ([2008-11-16 7:00 PM](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html))

`objc_msgSend` is the Objective-C message dispatcher. `objc_msgSend_stret` is exactly the same, but for methods that return values of struct types. And `objc_msgSend_fpret` is for methods that return floating-point values on some architectures.

|  | `objc_msgSend_fpret` return types |
|---|---|
| i386 | `float`, `double`, `long double` |
| x86_64 | `long double` |
| ppc | none (identical to `objc_msgSend`) |
| ppc64 |  |
| arm |  |

`objc_msgSend_stret` exists because the parameters are passed in different places for struct-returning functions. That's not the problem that `objc_msgSend_fpret` solves. Instead, `objc_msgSend_fpret` exists to handle the return value itself correctly. Specifically, the return value of a message sent to nil on i386 and x86_64.

Messages to nil return zero if possible. On ppc, `objc_msgSend` with a nil receiver clears registers r3, r4, f1, and f2 before returning. This means any pointer or integer or floating-point return value will be zero, and structs are undefined. On ppc, `objc_msgSend_fpret` is unnecessary, because clearing f1 and f2 is harmless if the caller is actually expecting a value in r3 or r4.

i386 is different. The floating-point registers there are historically derived from the 8087 FPU for the original 8086 CPU. The x87 unit is an odd beast: it has eight floating-point registers, but the registers themselves are used as if they were a stack. Values are pushed and popped from this stack even though the stack is stored in registers and has a maximum of eight entries.

For return values, the callee pushes the value on the x87 stack and the caller pops it. This is fine for C functions, but not so good when `objc_msgSend` returns zero. `objc_msgSend` does not know what return type the caller really wants, and it must not push a zero on the x87 stack unless the caller expects to pop a floating-point value.

The solution is `objc_msgSend_fpret`. During a message to nil on i386, `objc_msgSend_fpret` pushes a zero on the x87 stack which the caller will pop, and `objc_msgSend` does not. The caller knows which return type the caller expects, and uses the matching dispatcher. On ppc, ppc64, and arm, `objc_msgSend_fpret` is identical to `objc_msgSend` and is usually unused.

What about x86_64? This architecture is one step forward, two steps back. The good news is that return values of types `float` and `double` are returned in the XMM registers. `objc_msgSend` can handle that itself just like ppc. The bad news is that `long double` still uses the x87 stack. So `objc_msgSend_fpret` still exists, but is only used for `long double` on x86_64. The worse news is that C99's `complex long double` returns two values on the x87 stack. So now there's `objc_msgSend_fp2ret` for that case only. Currently no compiler actually uses `objc_msgSend_fp2ret`, so hopefully nobody is writing code that sends a message to nil on x86_64 and expects a zero return value of type `complex long
	double`.

One last thing: Mac OS X 10.4 and earlier did not return zero for floating-point messages to nil on ppc. Be careful if you're writing code for those older systems. All other architectures have always returned floating-point zero, including i386 on 10.4.

[Sealie Software](http://sealiesoftware.com/index.html)
