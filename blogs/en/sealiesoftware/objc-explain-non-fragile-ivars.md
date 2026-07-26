---
title: '[objc explain]: Non-fragile ivars'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html'
original_language: en
published: 2009-01-27
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:bff9071576a2553c'
translated: false
---

> 原文：[[objc explain]: Non-fragile ivars](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: Classes and metaclasses](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Infinity isn't as long as you think](http://sealiesoftware.com/blog/archive/2008/11/30/Infinity_isnt_as_long_as_you_think.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html)

**[objc explain]: Non-fragile ivars** ([2009-01-27 09:30 PM](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html))

Non-fragile instance variables are a headline feature of the modern Objective-C runtime available on iPhone and 64-bit Mac. They provide framework developers more flexibility without losing binary compatibility, and pave the way for automatically-synthesized property ivars and ivars declared outside a class's interface.

#### The fragile base class problem

Fragile ivars are a subset of the classic _fragile base class_ problem. In some languages, a superclass cannot be changed without also recompiling all subclasses of that class. For example, adding data members or virtual member functions to a C++ superclass will break binary compatibility with any subclass of that class, even if the added members are private and invisible to the subclass.

In classic Objective-C, methods are mostly non-fragile, thanks to dynamic message dispatch. You can freely add methods to a superclass, as long as you don't have name conflicts. But Objective-C ivars are fragile on 32-bit Mac.

#### 32-bit Mac: fragile Objective-C ivars

Say you're writing the world's next great pet shop application for Mac OS X Leopard. You might have this `PetShopView` subclass of `NSView`, with arrays for the puppies and kittens in the pet shop.

| _`NSView (Leopard)`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |

| _`PetShopView`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSArray *kittens` |
| `32` | `NSArray *puppies` |

Then Mac OS X Def Leopard comes out, with its new multi-paw interface technology. The AppKit developers add some paw-tracking code to `NSView`.

| _`NSView (Def Leopard)`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSSet *touchedPaws` |

| _`PetShopView`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSArray *kittens` |
| `32` | `NSArray *puppies` |

Unfortunately, your kittens are doomed by fragile ivars. Alternatively, the AppKit developers are trapped with whatever ivars they chose in Mac OS X 10.0.

#### iPhone and 64-bit Mac: non-fragile Objective-C ivars

What you and the AppKit developers really want is something like this.

| _`NSView (Def Leopard)`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSSet *touchedPaws` |

| _`PetShopView`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSSet *touchedPaws` |
| `32` | `NSArray *kittens` |
| `36` | `NSArray *puppies` |

Here, the runtime has recognized that `NSView` is now larger than it was when `PetShopView` was compiled. The subclass ivars slide in response, without recompiling any code, and the kittens are saved by a dynamic runtime.

#### How it works

The generated code for classic Objective-C ivar access works like a C `struct` field. The offset to the ivar is a constant determined at compile time. The new ivar code instead creates a variable for each ivar which contains the offset to that ivar, and all code that accesses the ivar uses that variable. At launch time, the runtime can change any ivar offset variable if it detects an oversize superclass.

In the pet shop example, `_OBJC_IVAR_PetShopView_kittens` is 28 at compile time, but the runtime changes it to 32 when it sees the Def Leopard version of `NSView`. No code needs to be recompiled, and the performance overhead of the extra ivar offset variable is small. AppKit is happy, you're happy, and the kittens are happy.

Sealie Software
