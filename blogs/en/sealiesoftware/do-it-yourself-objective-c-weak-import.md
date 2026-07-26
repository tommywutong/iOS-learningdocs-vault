---
title: Do-it-yourself Objective-C weak import
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html'
original_language: en
published: 2010-04-08
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:42b4d22e565427b6'
translated: false
---

> 原文：[Do-it-yourself Objective-C weak import](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [TargetConditionals.h](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Weak-import classes](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html)

**Do-it-yourself Objective-C weak import** ([2010-4-8 10:23 PM](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html))

#### WARNING DANGER HAZARD BEWARE EEK

The scheme described herein is **UNTESTED** and probably **BUGGY**. Use at your own risk.

#### Executive summary

The Objective-C runtime supports [weak-imported classes](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html) back to iPhone OS 3.1. An app could use a class added in iPhone OS 3.2 or 4.0 and still run on 3.1. The app would check if `[SomeClass
	class]` is `nil` and act accordingly.

Unfortunately, the compilers and class declarations in framework headers do not support weak import yet. But you may be able to use weak linking anyway, by adding the right incantations yourself.

To **use** a class `SomeClass` that is unavailable on some of your app's deployment targets, write this in **every** file that uses the class:

```
    asm(".weak_reference _OBJC_CLASS_$_SomeClass");
```

To

a class

that is unavailable on some of your app's deployment targets, write this in the file containing your subclass's

:

```
    asm(".weak_reference _OBJC_CLASS_$_SomeClass");
    asm(".weak_reference _OBJC_METACLASS_$_SomeClass");
```

This will not work for apps running on iPhone OS 3.0 or older. Only iPhone OS 3.1 and newer has any hope of success. Of course, since this is

it may not work there either.

#### How it works

Say you're writing a game, and want to use the hypothetical `UIDancePad` class added to iPhone OS 3.2. (Do not dance on iPad.) When you use class `UIDancePad` in your code, the compiler emits a C symbol pointing to the class:

```
    .long _OBJC_CLASS_$_UIDancePad
```

Since `UIDancePad` is in a framework instead of your code, the symbol remains undefined in your executable, as shown by ``nm -m``:

```
    (undefined) external _OBJC_CLASS_$_UIDancePad (from DanceKit)
```

When you run on iPhone OS 3.2, everything works great: the dynamic loader opens your executable and DanceKit, and binds your undefined symbol to their class definition.

Things don't go so well on iPhone OS 3.1. DanceKit exists but does not define `UIDancePad`. The dynamic loader is unable to resolve your undefined symbol, and the process halts:

```
    dyld: Symbol not found: _OBJC_CLASS_$_UIDancePad
        Referenced from: /path/to/YourApp
        Expected in: /path/to/DanceKit
```

Weak import solves this. The compiled symbol reference is now a weak one:

```
    .weak_reference _OBJC_CLASS_$_UIDancePad
    .long _OBJC_CLASS_$_UIDancePad

    (undefined) weak external _OBJC_CLASS_$_UIDancePad (from DanceKit)
```

The dynamic loader shrugs its shoulders if a weak reference cannot be resolved, and sets the pointer to `NULL`. The Objective-C runtime sees the `NULL` pointer and fixes up the rest of the metadata as if `UIDancePad` never existed.

As mentioned above, the compiler and framework header support is not yet in place. The incantations simply add the assembler directives that the compiler does not yet know how to emit:

```
    asm(".weak_reference _OBJC_CLASS_$_UIDancePad");
```

Et voilà: weak import of an Objective-C class. Well, maybe. I have only tested this on toy examples, none of which got anywhere close to any version of iPhone OS. Coder beware!

(What about the `_OBJC_METACLASS` symbol, you ask? When you subclass a class, your subclass's metaclass's superclass pointer points to the subclass's superclass's metaclass. In other words, your subclass's `@implementation` points to both its superclass and its superclass's [metaclass](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html). That requires two symbols: one for the class and one for the metaclass. When you simply use a class without subclassing it, you don't need the metaclass pointer.)

Sealie Software
