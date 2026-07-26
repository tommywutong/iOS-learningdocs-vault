---
title: '[objc explain]: objc_msgSend_vtable'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html'
original_language: en
published: 2011-06-17
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1cf86dd029518248'
translated: false
---

> 原文：[[objc explain]: objc_msgSend_vtable](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: return value of message to nil](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Dr. Gregory Parker, Department of Diagnostic Engineering](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html)

**[objc explain]: objc_msgSend_vtable** ([2011-06-17 4:42 PM](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html))

`objc_msgSend_vtable` is a version of `objc_msgSend` used to optimize a few of the most commonly called methods.

Most Objective-C methods are dispatched using a hash table lookup inside `objc_msgSend`. On x86_64, a few selectors can be dispatched using a C++-style virtual table: an array lookup, not a hash table.

The compiler knows which selectors are optimized by the runtime. It compiles the call site differently, calling `objc_msgSend_fixup` via a function pointer. At runtime, `objc_msgSend_fixup` replaces the function pointer with one of the `objc_msgSend_vtable` functions, if the called selector is one of the optimized selectors.

C++ vtables are notoriously fragile: the array offsets for each virtual method are hardcoded into the generated code. Objective-C's vtables are not fragile. Each vtable is built at runtime and updated when method lists change. In theory even the set of optimized methods could be changed. The non-fragile flexibility costs an extra memory load during dispatch.

Dispatch via vtable is faster than a hash table, but would consume tremendous amounts of memory if used everywhere. Objective-C's vtable implementation limits its use to a few selectors that are (1) implemented everywhere, but (2) rarely overridden. That means most classes share their superclass's vtable, which keeps memory costs low.

A crash in any `objc_msgSend_vtable` function should be debugged exactly like a crash in `objc_msgSend` itself. They both crash for all of the same reasons, like incorrect memory management or memory smashers.

Currently, the runtime uses sixteen different `objc_msgSend_vtable` functions, one for each slot in the sixteen-entry vtable.

| `objc_msgSend_vtable0` | `allocWithZone:` |
|---|---|
| `objc_msgSend_vtable1` | `alloc` |
| `objc_msgSend_vtable2` | `class` |
| `objc_msgSend_vtable3` | `self` |
| `objc_msgSend_vtable4` | `isKindOfClass:` |
| `objc_msgSend_vtable5` | `respondsToSelector:` |
| `objc_msgSend_vtable6` | `isFlipped` |
| `objc_msgSend_vtable7` | `length` |
| `objc_msgSend_vtable8` | `objectForKey:` |
| `objc_msgSend_vtable9` | `count` |
| `objc_msgSend_vtable10` | `objectAtIndex:` |
| `objc_msgSend_vtable11` | `isEqualToString:` |
| `objc_msgSend_vtable12` | `isEqual:` |
| `objc_msgSend_vtable13` | `retain` (non-GC) `hash` (GC) |
| `objc_msgSend_vtable14` | `release` (non-GC) `addObject:` (GC) |
| `objc_msgSend_vtable15` | `autorelease` (non-GC) `countByEnumeratingWithState:objects:count:` (GC) |

The vtable's contents differ for GC and non-GC, for obvious reasons. `-isFlipped` is part of NSView. `-countByEnumeratingWithState:objects:count:` is the fast enumeration implementation, including `for (x in
       y)`. Together these methods make up roughly 30-50% of calls in typical Objective-C applications.

[Sealie Software](http://sealiesoftware.com/index.html)
