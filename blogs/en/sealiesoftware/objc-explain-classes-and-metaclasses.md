---
title: '[objc explain]: Classes and metaclasses'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html'
original_language: en
published: 2009-04-14
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ea97b01aefaeb850'
translated: false
---

> 原文：[[objc explain]: Classes and metaclasses](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: Monomorphic dispatch](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Non-fragile ivars](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)

**[objc explain]: Classes and metaclasses** ([2009-04-14 08:35 PM](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html))

Objective-C is a class-based object system. Each object is an instance of some class; the object's `isa` pointer points to its class. That class describes the object's data: allocation size and ivar types and layout. The class also describes the object's behavior: the selectors it responds to and instance methods it implements.

The class's method list is the set of instance methods, the selectors that the object responds to. When you send a message to an instance, `objc_msgSend()` looks through the method list of that object's class (and superclasses, if any) to decide what method to call.

Each Objective-C class is also an object. It has an `isa` pointer and other data, and can respond to selectors. When you call a "class method" like `[NSObject
	alloc]`, you are actually sending a message to that class object.

[![](http://sealiesoftware.com/blog/class diagram.pdf)](http://sealiesoftware.com/blog/class diagram.pdf) Since a class is an object, it must be an instance of some other class: a metaclass. The metaclass is the description of the class object, just like the class is the description of ordinary instances. In particular, the metaclass's method list is the class methods: the selectors that the class object responds to. When you send a message to a class - an instance of a metaclass - `objc_msgSend()` looks through the method list of the metaclass (and its superclasses, if any) to decide what method to call. Class methods are described by the metaclass on behalf of the class object, just like instance methods are described by the class on behalf of the instance objects.

What about the metaclass? Is it metaclasses all the way down? No. A metaclass is an instance of the root class's metaclass; the root metaclass is itself an instance of the root metaclass. The `isa` chain ends in a cycle here: instance to class to metaclass to root metaclass to itself. The behavior of metaclass `isa` pointers rarely matters, since in the real world nobody sends messages to metaclass objects.

More important is the superclass of a metaclass. The metaclass's superclass chain parallels the class's superclass chain, so class methods are inherited in parallel with instance methods. And the root metaclass's superclass is the root class, so each class object responds to the root class's instance methods. In the end, a class object is an instance of (a subclass of) the root class, just like any other object.

Confused? The diagram may help. Remember, when a message is sent to any object, the method lookup starts with that object's `isa` pointer, then continues up the superclass chain. "Instance methods" are defined by the class, and "class methods" are defined by the metaclass plus the root (non-meta) class.

In proper computer science language theory, a class and metaclass hierarchy can be more free-form, with deeper metaclass chains and multiple classes instantiated from any single metaclass. Objective-C uses metaclasses for practical goals like class methods, but otherwise tends to hide metaclasses. For example, `[NSObject class]` is identical to `[NSObject self]`, even though in formal terms it ought to return the metaclass that `NSObject->isa` points to. The Objective-C language is a set of practical compromises; here it limits the class schema before it gets too, well, _meta_.

[Sealie Software](http://sealiesoftware.com/index.html)
