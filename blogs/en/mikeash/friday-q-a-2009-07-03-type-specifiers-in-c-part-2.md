---
title: 'Friday Q&A 2009-07-03: Type Specifiers in C, Part 2'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-07-03-type-specifiers-in-c-part-2.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0d9a847020164474'
translated: false
---

> 原文：[Friday Q&A 2009-07-03: Type Specifiers in C, Part 2](https://www.mikeash.com/pyblog/friday-qa-2009-07-03-type-specifiers-in-c-part-2.html)　·　mikeash.com Friday Q&A

Posted at 2009-07-03 13:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-07-10: Type Specifiers in C, Part 3](https://www.mikeash.com/pyblog/friday-qa-2009-07-10-type-specifiers-in-c-part-3.html)  
Previous article: [Friday Q&A 2009-06-26: Type Qualifiers in C, Part 1](https://www.mikeash.com/pyblog/friday-qa-2009-06-26-type-qualifiers-in-c-part-1.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-07-03: Type Specifiers in C, Part 2

by [Mike Ash](https://www.mikeash.com/)

**Virtual Machine**  
 To properly understand `volatile`, you first have to understand the way that the C language is defined. It may seem strange, because C is (rightly) seen as basically a high-level assembly language, but the behavior of C is actually defined in terms of a virtual machine.

Don't misunderstand. C isn't actually implemented with a virtual machine. (Well, there's probably an implementation out there somewhere that is, but it _usually_ isn't.) It's purely a logical device that's used to discuss behavior.

The behavior of any given chunk of C code is written into the standard. The `+` operation results in performing arithmetic on the operands. The `=` operation causes a value to be stored into the lvalue. And so forth. However, a lot of these actions end up being unnecessary. For example, consider this code:

```
    int x = 3; y = 4;
    int z = x + y * 2;
    z = x + y;
    x = x + y;
```

There's a fair amount of redundancy here. First, the initial values of the three variables are unused. Then the expression

is used twice. It would be inefficient to compile all of this code literally.

The C standard has an answer to this problem. It states that the program must execute _as if_ all the specified actions were executed in a virtual machine. In other words, given the code above, at the end of the day `x` must contain 7, `y` must contain 4, and `z` must contain 7. But how it actually gets there is entirely up for grabs. A smart compiler will just do all of the computations at compile time and generate code that dumps those final values into the variables right away, instead of doing math every time through.

**Memory Model**  
 So what's the problem? Consider a piece of code like this:

```
    int *x = ...; int y;
    y = *x;
    *x = y;
    y = *x;
    *x = y;
    y = *x;
```

Again, this code has a bunch of redundancies in it. The compiler would be entirely within its rights to rip out most of this and simply execute a single load from

, because there's no way that the value pointed to by

or anything else could possibly be changed by executing all the intermediate statements.

This is true according to the C standard, where memory is just another component of the virtual machine, and doesn't have to have any real relationship to the actual physical RAM that's sitting in your computer.

And what's wrong with that? Well, nothing really, except for when you go outside the idealized virtual machine of the C standard.

**Device Drivers**  
 This is what `volatile` was originally created for, and is still what it's most useful for. C is a common language for kernel programming and other bare metal tasks. When you're working at that level, memory isn't just memory anymore. Sometimes a particular address in memory will actually be a register on a physical device. For example, you could imagine reading and writing data to a serial port by hitting registers on the serial port hardware:

```
    char *data = ...; int length = ...;
    char *writeAddr = SerialPortWriteAddress();
    for(int i = 0; i < length; i++)
        *writeAddr = data[i];
    
    int responseLength = ...;
    char response[responseLength];
    char *readAddr = SerialPortReadAddress();
    for(int i = 0; i < responseLength; i++)
        response[i] = *readAddr;
```

In this case, every read from readAddr would actually fetch a new character from the serial port, and every write to writeAddr would actually push a new character into it. This is called

memory-mapped IO

.

The trouble is that the C compiler (and the C standard) has no idea about this magical pointer that gives you a different value every time you read from it, and this other magical pointer that causes electrons to flow through a wire every time you write to it. As far as it knows, this is just memory like anything else, and the compiler may very well decide that your loops are pointless and redundant, and hoist all of the pointer reading/writing out of them so that you only do one load and one store instead of a whole bunch of redundant ones.

This would be great if this were standard memory. Free speedup! But it's a disaster here.

Thus the `volatile` keyword. By declaring these pointers as `volatile char *` we can tell the compiler that these pointers are special pointers and every interaction with them must be taken literally. Every time we dereference one, the compiler _must_ actually read or write that memory location, even if it looks redundant.

At this point you might think that this is interesting but wondering why we care. After all, I've never done any kernel programming and you probably haven't either. Userland programs never get to play with funky device-mapped pointers. So what's the point?

Well, there _mostly_ isn't one. `volatile` just isn't that useful in userland! However there are two things where `volatile` can make a difference in userland code.

**`setjmp`/`longjmp`**  
 Long before any C-based language had ever heard of exceptions, there was this tremendously evil pair of functions called `setjmp` and `longjmp`. In short, `setjmp` saves the register state of the machine, and `longjmp` restores it, causing program flow to jump backwards. This can be used to build an exception-handling system, and indeed Cocoa did just that for a long time.

The trouble is with those pesky registers. Variables are often stored in registers instead of memory. This means that a call to `longjmp` could actually revert values stored in registers after an assignment had taken place.

Thus one handy use for `volatile`: declare any variables that this might happen to as `volatile`, and the compiler will make sure that all assignments go to memory, and thus that their contents will survive the jump.

Again, this isn't actually all that useful. Basically nobody uses `setjmp`/`longjmp` anymore. And while Objective-C's exception handling is still based on them (in the 32-bit Mac runtime), the compiler takes care of marking everything that needs it as volatile behind the scenes so you don't have to.

This leaves us with the one place where `volatile` can actually be useful in userland. It's no coincidence that this is also the one place where it is terribly abused, and where people don't really understand what it does.

**Threading**  
 Threads are another thing that the C language standard simply does not cover. The standard assumes a single thread of control in the program. All threading APIs in C go beyond the standard's guarantees.

Threading is also a place where memory semantics matter, because the heap is shared between threads. Since the C standard doesn't make any guarantees about how memory is _actually_ used with a non-`volatile` pointer, only that it _look_ like it was used in a certain way, and because the standard is unaware of threads, that shared memory can become very screwed up if the programmer assumes that the memory will be modified in exactly the manner and order in which his program specifies.

Threading also exposes another layer of hardware to the programmer. Suddenly the programmer has to worry about having multiple CPUs in the system. Much like the C standard, modern CPUs often treat memory access on an _as if_ basis. Real memory accesses may happen in a completely different order than the program actually issued them in. The `volatile` keyword can't get around this, which diminishes its usefulness to some extent.

A full discussion of the use of `volatile` in multithreaded code is unfortunately beyond my ability to write for this week! I thought I could cram it all in but I just can't. Come back next week for Part 3, and what is hopefully our exciting conclusion.

**Conclusion**  
 Now you know the basics of what `volatile` does and what it's good for. Answer: not much. As a general guideline, if you're using `volatile` in your code then you're _probably_ doing something wrong. However, there are cases where it can be useful, and most of them fall under the heading of multithreading. There are also many cases in multithreaded code where it _looks_ useful but isn't. Next week in Part 3 I will explore the ups and downs of `volatile` in multithreaded code.

Until then, leave your comments below, and [send in your ideas](mailto:mike@mikeash.com) for future topics. Remember, Friday Q&A is driven by your contributions, so send in your idea today!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
