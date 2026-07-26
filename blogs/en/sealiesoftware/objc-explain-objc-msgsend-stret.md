---
title: '[objc explain]: objc_msgSend_stret'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html'
original_language: en
published: 2008-10-30
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:02edf4fbe2132af4'
translated: false
---

> 原文：[[objc explain]: objc_msgSend_stret](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: objc_msgSend_fpret](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [updated: Valgrind for Mac OS X](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html)

**[objc explain]: objc_msgSend_stret** ([2008-10-30 10:28 PM](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html))

`objc_msgSend` is the Objective-C message dispatcher. It's the function-calling function, using selector and the receiver object's class to decide where to jump to. `objc_msgSend_stret` is exactly the same, but for methods that return values of struct types. Why does `objc_msgSend_stret` exist? Because of the machine-level guts of the C language require it, and Objective-C methods are C functions if you tilt your head and squint a bit.

On most processors, the first few parameters to a function are passed in CPU registers, and return values are handed back in CPU registers. Objective-C methods do the same, but with `id self` and `SEL
	_cmd` as the first two parameters. Here's a PowerPC example:

```
    -(int) method:(id)arg;
        r3 = self
        r4 = _cmd, @selector(method:)
        r5 = arg
	(on exit) r3 = returned int
```

CPU registers work fine for small return values like ints and pointers, but structure values can be too big to fit. For structs, the caller allocates stack space for the returned struct, passes the address of that storage to the function, and the function writes its return value into that space. The address of the struct is an implicit first parameter just like `self` and `_cmd`:

```
    -(struct st) method:(id)arg;
        r3 = &struct_var (in caller's stack frame)
        r4 = self
        r5 = _cmd, @selector(method:)
        r6 = arg
        (on exit) return value written into struct_var
```

Now consider `objc_msgSend`'s task. It uses `_cmd` and `self->isa` to choose the destination. But `self` and `_cmd` are in different registers if the method will return a struct, and `objc_msgSend` can't tell that in advance. Thus `objc_msgSend_stret`: just like `objc_msgSend`, but reading its values from different registers.

But there's a catch.

On most architectures, some small C structs are returned in registers after all, instead of using the struct-address first parameter that `objc_msgSend_stret` expects. If the struct type falls into this category, then `objc_msgSend` is used instead. So the "struct return" part of `objc_msgSend_stret` refers to the architecture's definition of a stack-returned struct, which may not match C struct.

The rules for which struct types return in registers are always arcane, sometimes insane. ppc32 is trivial: structs never return in registers. i386 is straightforward: structs with `sizeof` exactly equal to 1, 2, 4, or 8 return in registers. x86_64 is more complicated, including rules for returning floating-point struct fields in FPU registers, and ppc64's rules and exceptions will make your head spin. The gory details are documented in the [Mac OS X ABI Guide](http://developer.apple.com/documentation/DeveloperTools/Conceptual/LowLevelABI), though as usual if the documentation and the compiler disagree then the documentation is wrong.

If you're calling `objc_msgSend` directly and need to know whether to use `objc_msgSend_stret` for a particular struct type, I recommend the empirical approach: write a line of code that calls your method, compile it on each architecture you care about, and look at the assembly code to see which dispatch function the compiler uses.

Sealie Software
