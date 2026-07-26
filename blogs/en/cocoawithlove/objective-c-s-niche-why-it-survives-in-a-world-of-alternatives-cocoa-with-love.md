---
title: 'Objective-C''s niche: why it survives in a world of alternatives | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/objective-c-niche-why-it-survives-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5f0d3a6a44ac303b'
translated: false
---

> 原文：[Objective-C's niche: why it survives in a world of alternatives | Cocoa with Love](https://www.cocoawithlove.com/2009/10/objective-c-niche-why-it-survives-in.html)　·　Cocoa with Love (Matt Gallagher)

Objective-C remains an impediment for many programmers coming to the Mac or iPhone platforms — few programmers have ever experienced it before learning Cocoa, forcing two learning curves at once for new Cocoa developers. How did Apple end up with such a weird language? And for a company known to replace CPU architectures and their entire operating system, why does Apple persist with Objective-C? The answer lies in the methods.

## Virtual methods

Most compiled, object-oriented languages (like C++, Java and C♯) adhere closely to the object-oriented approaches first introduced in [Simula 67](http://en.wikipedia.org/wiki/Simula) — in particular the concept of [virtual methods](http://en.wikipedia.org/wiki/Virtual_function) and how they enable methods to be overridden.

> **Origins in Algol:** In much the same way that Objective-C is often called a "pure superset" of C, Simula 67 was a "pure superset" of [Algol 60](http://en.wikipedia.org/wiki/ALGOL). While [Fortran](http://en.wikipedia.org/wiki/Fortran) is sometimes remembered as the first high-level language to gain popularity (and disdain), Algol 60 was the first programming language to actually resemble a modern language as it contained the `for`, `if`/`else`, `while` (of sorts), and other procedural contructs that are expected now in programming languages. While Algol was rarely used past the 1970's, [Pascal](http://en.wikipedia.org/wiki/Pascal_(programming_language)) and its descendants closely resemble Algol in syntax.

In a compiled language, a [regular function](http://en.wikipedia.org/wiki/Subroutine) (non-overrideable) ends up as a basic memory address. When the function is invoked, the CPU jumps to the memory address.

Simula 67 introduced [virtual method tables](http://en.wikipedia.org/wiki/Virtual_table) to adapt this for object-orientation. Instead of basic memory addresses, methods are compiled to row numbers in a table. To get the memory address, the method table is retrieved from the class of the object and the CPU jumps to the address at the specified row.

Since different objects have different classes, they will have different addresses in their method tables, hereby allowing sublcasses to have different implementations of methods ([method overrides](http://en.wikipedia.org/wiki/Method_overriding)) to their base classes.

## Message passing

While virtual method tables do introduce a level of indirection that allows method behavior to change from object to object, the offsets into the table and hence the tables themselves all need to be created at compile-time.

> **History of message passing:** As with object-orientation itself, message passing was inspired by Simula 67 but Simula's message passing (called "Simulation") wasn't for method invocations — it was instead used for discrete event simulation (mostly queueing and list processing). [Smalltalk](http://en.wikipedia.org/wiki/Smalltalk) expanded upon this idea by using message passing for method invocation. Smalltalk subsequently inspired the [Actor Model](http://en.wikipedia.org/wiki/Actor_model) (used in distributed processing) and [remote procedure calls](http://en.wikipedia.org/wiki/Remote_procedure_call) (RPC). Originally, Smalltalk messages were conceived to have a large amount of metadata (more like the full headers on an email) but eventually, this was simplified down to an approach syntactically similar to Objective-C's current implementation (minus square brackets).

[Message passing](http://en.wikipedia.org/wiki/Message_passing) presents an alternative way of solving the [method dispatch problem](http://en.wikipedia.org/wiki/Dynamic_dispatch). Instead of the virtual method's compile-time offsets and tables which don't consult the object (except for its type), message passing sends a unique message identifier to the object itself and the object determines at runtime what action to take.

Message passing approaches may still have a virtual method table ("vtable") in the class' representation but this structure is not known at compile time — it is handled entirely at runtime — and instances of the class have the opportunity to take different actions in response to the message that are unrelated to the content of the table.

There are two important differences here:

- Runtime resolution — so the connection between message identifier and action can be changed at runtime.
- Involvement of the object itself, not just its class.

On a technical level, the difference between a virtual method table and passing a message identifier is relatively minor (since both are really table lookups and both are actually performed at runtime). The difference ends up being conceptual:

- Virtual method table languages generally make it hard or impossible to change the virtual method table contents or pointers at runtime.
- Type safety is essential in a virtual method table language since the compiler may alter table lookups based on type, particularly in cases of multiple inheritance. In message passing systems, type safety is irrelevant to method invocation.

## Why this matters

The short answer is that this dynamic message handling in Objective-C makes it much easier to work within a large framework that you didn't create because you can examine, patch and modify elements of that framework on the fly. The most common situation where this is likely to occur is when dealing with an [application framework](http://en.wikipedia.org/wiki/Application_framework).

The biggest reason for this is that you can add or change methods on existing objects, without needing to subclass them, while they are running. Approaches for this include [categories](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocCategories.html#//apple_ref/doc/uid/TP30001163-CH20-TPXREF141), [method swizzling](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html) and isa-swizzling.

This makes the following situations possible:

- You want to add a convenience method to someone else's object (a quick search of my own posts reveals that about a dozens of my own posts involve adding convenience methods to Cocoa classes, e.g. [Safely fetching an NSManagedObject by URI](https://www.cocoawithlove.com/2008/08/safely-fetching-nsmanagedobject-by-uri.html)).
- You want to change the behavior of a class you didn't (and can't) allocate because it is created by someone else (this is how [Key-Value Observing is implemented in Cocoa](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/KeyValueObserving/Concepts/KVOImplementation.html)).
- You want to treat objects generically and handle potential differences with runtime introspection.
- You want to substitute an object of a completely different class to the expected class (this is used in Cocoa by [NSProxy](http://developer.apple.com/mac/library/documentation/Cocoa/Reference/Foundation/Classes/NSProxy_Class/Reference/Reference.html) to turn a regular object into a distributed object).

These points may seem somewhat mild but they are central to maximizing code reuse when working within someone else's framework: if you need existing code to work differently, you don't need to reimplement the whole class and you don't need to change how it is allocated.

Languages using virtual method tables can adopt some of these ideas (like the [boost::any](http://www.boost.org/doc/libs/1_40_0/doc/html/boost/any.html) class or [C♯ 4.0's dynamic member lookup](http://en.wikipedia.org/wiki/C_Sharp_4.0)) but these features have additional restrictions and don't apply to all objects, meaning that they can't be used on purely arbitrary objects (such as those you don't control or didn't create) and so don't help when interacting with someone else's framework.

Simply put: dynamic message passing instead of virtual method invocations makes Objective-C a much better language for working with a large library or framework that someone has written.

## The tradeoff

The downside to dynamic message invocation is that it is only as fast as virtual method invocation when the message lookup is cached, otherwise it is invariably slower.

Also, in keeping with the philosophy of a purely dynamic messaging system, Objective-C does not use templates or template metaprogramming and does not have non-dynamic (i.e. non-virtual) methods. This means that Objective-C methods will miss out on the compiler optimizations possible when employing these techniques. Also, since modern programming in C++ is substantially focussed on these features, it can difficult to adapt programs using these ideas to Objective-C.

Theoretically, Objective-C could implement these features but they are in opposition to the underlying concepts of flexibility and dynamic behavior in Objective-C — and would shut-down all advantages from the previous section if they were used.

## Conclusion

It's not a coincidence that I write an Objective-C/Cocoa blog, I'm obviously an advocate of Objective-C and Cocoa. In my opinion, Objective-C is the best language for programming situations where you must make extensive use of a framework written by someone else (particularly an application framework). The success of Objective-C in this situation is due to the combination of:

- speed and precision (from its compiled C roots)
- dynamic flexibility (due to using message passing for method invocations)

To frame this conclusion, I'll state that I've written major projects using C/WIN32, C++/PowerPlant, C++/MFC, and Java/Swing/AWT. I've also dabbled in smaller projects using C♯/.Net. In all of these cases I have found the application frameworks to be less flexible and less reusable because they lack the dynamic modifiability of Objective-C.

As I've stated, I do view Objective-C's strength in the area of application frameworks as a niche (albeit a very large niche). If I were writing a compiler, OS kernel, or a low-level/high-performance library, then I would use C++ (I wouldn't use pure C because I'd miss my abstractions) — but these are situations where metaprogramming, greater inlining and faster method invocations would trump flexibility concerns. Of course, if you have a project that needs to satisfy all these criteria: then there's always Objective-C++.
