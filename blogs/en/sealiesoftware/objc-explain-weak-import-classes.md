---
title: '[objc explain]: Weak-import classes'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html'
original_language: en
published: 2009-09-09
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:636c59a750b11ccf'
translated: false
---

> 原文：[[objc explain]: Weak-import classes](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Do-it-yourself Objective-C weak import](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Colorized keyboard backlight](http://sealiesoftware.com/blog/archive/2009/09/05/Colorized_keyboard_backlight.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html)

**[objc explain]: Weak-import classes** ([2009-09-09 1:30 PM](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html))

Weak-import classes are a useful new Objective-C feature that you can't use yet.

Weak import is a solution when you want to use something from a framework, but still need to be compatible with older versions of the framework that didn't support it yet. Using weak import you can test if the feature exists at runtime before you try to use it.

Objective-C has not previously supported weak import for classes. Instead you had to use clumsy runtime introspection to check whether a class was available, store a pointer to that class in a variable, and use that variable when you wanted to send a message to the class. Even worse, there was no reasonable way to create your own subclass of a superclass that might be unavailable. Some developers put the subclass in a separate library that was not loaded until after checking that the superclass was present, but even that trick is not allowed on iPhone OS.

Weak import for C functions works by checking the weak-imported function pointer's value before calling it:

```
    if (NSNewFunction != NULL) {
        NSNewFunction(...);
    } else {
        // NSNewFunction not supported on this system
    }
```

The same mechanism is a natural fit with Objective-C classes and Objective-C's handling of messages to nil. These constructs are much nicer than `NSClassFromString()` or a separate `NSBundle`.

```
    if ([NSNewClass class] != nil) {
        [NSNewClass doSomething];
    } else {
        // NSNewClass is unavailable on this system
    }
```

```
    @interface MySubclass : NSNewClass ... @end
    MySubclass *obj = [[MySubclass alloc] init];
    if (!obj) {
        // MySubclass (or a superclass thereof) is unavailable on this system
    }
```

Weak import of Objective-C classes is now available. But you can't use it yet. First, it's only supported today on iPhone OS 3.1; it's expected to arrive in a future Mac OS.

Second, there's nothing you can do with weak import until the first OS update _after_ iPhone OS 3.1. Then you could write an app that adopted new features in that future version, and used weak import to be compatible with 3.1. (It still could not run on 3.0 or 2.x, because those systems lack the runtime machinery to process the weak import references.)

Weak import for Objective-C did not make Snow Leopard for scheduling reasons. Assuming it ships in Mac OS X 10.7 Cat Name Forthcoming, you won't be able to use it until Mac OS X 10.8 LOLcat.

Sealie Software
