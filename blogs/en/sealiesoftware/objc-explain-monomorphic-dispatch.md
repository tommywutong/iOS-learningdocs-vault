---
title: '[objc explain]: Monomorphic dispatch'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html'
original_language: en
published: 2009-05-14
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cf2206dd21885e21'
translated: false
---

> 原文：[[objc explain]: Monomorphic dispatch](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Valgrind for Mac OS X goes mainline](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Classes and metaclasses](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html)

**[objc explain]: Monomorphic dispatch** ([2009-05-14 8:04 PM](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html))

Polymorphic dispatch means a single call site could branch to one of several different implementations. C function calls are not polymorphic; Objective-C methods and C++ virtual methods are polymorphic.

The monomorphic dispatch optimization is used when a call site could call different implementations in principle, but can only ever call one particular implementation in reality. Then the optimizer can eliminate the polymorphic dispatcher's overhead and jump directly to the right place or even inline the callee locally. This is a classic optimization for dynamic-compiled runtimes from Smalltalk to Java and JavaScript.

There are some complications. First is dynamically-loaded code like shared libraries or eval() operations. If your new code provides a second implementation of a call that was previously monomorphic, you need to be able to undo the previous optimization on the fly and recompile it or fall back to an interpreter. Any dynamic compiler worth the name can do this nowadays.

Second, the area to search for additional implementations depends on the type-strictness of your language. If the compile-time type of the receiver rigidly defines the allowed runtime types, then the implementation need only be unique within that part of the hierarchy for the optimization to work. `Window.title` and `Employee.title` wouldn't interfere with each other at a strictly-typed call site whose receiver is of type `Employee` (or a subclass thereof).

How does Objective-C fit in here? In general, it doesn't. The monomorphic optimization is hard to apply to Objective-C. The two problems above loom large because of the language's definition, even if it suddenly acquired a runtime recompiler tomorrow.

Objective-C's call sites are not type-strict. The code may say the receiver is of some type, but at runtime it could actually be a Distributed Objects proxy or a unit test mock or a scripting bridge shim. You'd have to look at all classes to decide if a selector has multiple implementations, instead of searching only a subtree of the class hierarchy.

Even worse, there are zero selectors that have only a single implementation. They all have at least two: the one that exists in some class, and the one from every other class that calls -forwardInvocation:. You can never jump directly to any implementation, because if your receiver object is of the wrong type then you need to call the forwarding machinery instead. And checking the receiver's type quickly eats any optimization profit; you can only make a handful of checks before your cost is the same as `objc_msgSend()`.

There are some important cases where monomorphic dispatch would still work in Objective-C. The container classes in particular have only one or two real implementations, so a receiver type check could be fast enough. And in other places you can make a single relatively expensive type check but then re-use the result many times, such as a series of `[self ...]` calls. The tricky part is identifying which selectors and call sites would optimize well, without taking too much time or memory to do so.

The monomorphic dispatch optimization will be present in some future dynamic-recompiling Objective-C runtime, but it won't work as well as it does in other less-dynamic languages.

[Sealie Software](http://sealiesoftware.com/index.html)
