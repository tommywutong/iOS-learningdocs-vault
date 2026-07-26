---
title: 'Friday Q&A 2010-01-15: Stack and Heap Objects in Objective-C'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ee74357400dd0d2c'
translated: false
---

> 原文：[Friday Q&A 2010-01-15: Stack and Heap Objects in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html)　·　mikeash.com Friday Q&A

Posted at 2010-01-15 21:58 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-01-22: Toll Free Bridging Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html)  
Previous article: [Friday Q&A 2010-01-08: NSNotificationQueue](https://www.mikeash.com/pyblog/friday-qa-2010-01-08-nsnotificationqueue.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [heap](https://www.mikeash.com/pyblog/?tag=heap) [memory](https://www.mikeash.com/pyblog/?tag=memory) [stack](https://www.mikeash.com/pyblog/?tag=stack)

Friday Q&A 2010-01-15: Stack and Heap Objects in Objective-C

by [Mike Ash](https://www.mikeash.com/)

Before we get into that, let's define our terms.

**Stack**  
 The stack is a region of memory which contains storage for local variables, as well as internal temporary values and housekeeping. On a modern system, there is one stack per thread of execution. When a function is called, a _stack frame_ is pushed onto the stack, and function-local data is stored there. When the function returns, its stack frame is destroyed. All of this happens automatically, without the programmer taking any explicit action other than calling a function.

**Heap**  
 The heap is, essentially, everything else in memory. (Yes, there are things other than the stack and heap, but let's ignore that for this discussion.) Memory can be allocated on the heap at any time, and destroyed at any time. You have to explicitly request for memory to be allocated from the heap, and if you aren't using garbage collection, explicitly free it as well. This is where you store things that need to outlive the current function call. The heap is what you access when you call `malloc` and `free`.

**Stack vs Heap Objects**  
 Given that, what's a stack object, and what's a heap object?

First, we must understand what an object is in general. In Objective-C (and many other languages), an object is simply a contiguous blob of memory with a particular layout. (If you're interested in just what it contains and how it's laid out, check out my [intro to the Objective-C runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html).)

The precise location of that memory is less important. As long as you have some memory somewhere with the right contents, it's a working Objective-C object. In Objective-C, objects are usually created on the heap:

```
    NSObject *obj = [[NSObject alloc] init];
```

The storage for the `obj` variable itself is on the stack, but the object it points to is in the heap. The `[NSObject alloc]` call allocates a chunk of heap memory, and fills it out to match the layout needed for an `NSObject`.

A stack object is just an object where the memory for that object is allocated on the stack. Objective-C doesn't have any support for this directly, but you can construct one manually without too much trouble:

```
    struct {
        Class isa;
    } fakeNSObject;
    fakeNSObject.isa = [NSObject class];
    
    NSObject *obj = (NSObject *)&fakeNSObject;
    NSLog(@"%@", [obj description]);
```

This works fine, although you shouldn't depend on it, as it depends on replicating the internal layout of the class.

**Advantages of Stack Objects**  
 It's obviously possible to have stack objects in general. Aside from the above hack, real languages like C++ have language support for stack objects. In C++, you can create objects on the stack or the heap:

```
    std::string stackString;
    std::string *heapString = new std::string;
```

Why allow both?

Stack objects have two compelling advantages:

1. **Speed:** Allocating memory on the stack is really fast. All of the bookkeeping is done by the compiler when you build your program. At runtime, the function prolog just carves out the amount of space it needs for all local variables, and the code knows what goes where because it was all computed in advance. Stack allocations are essentially free, whereas heap allocations can be quite expensive.
2. **Simplicity:** Stack objects have a defined lifetime. You can never leak one, because it always gets destroyed at the end of the scope where it was declared.

**Disadvantages of Stack Objects**  
 The strictly defined lifetime of a stack object is a disadvantage as well, and a major one. In Objective-C (and C++, and many other languages), it is impossible to move an object after it's created. The reason for this is because there may be many pointers to that object, and those pointers are not tracked. They would all need to be updated to track the move, but there's no way to accomplish this.

(Note: it's not an impossibility in general, and many languages move objects around as a matter of course, often as part of garbage collection schemes. However, this requires more runtime smarts and a stricter type system than you get in Objective-C.)

As used in Cocoa, Objective-C uses a reference counting system for memory management. The advantage of this system is that any single object can have multiple "owners", and the system won't allow the object to be destroyed until all owners have relinquished ownership.

Stack allocated objects inherently have a single owner, the function which created them. If Objective-C had stack objects, what would happen if you passed it to some other code which then tried to keep it around by `retain`ing it? There's no way to prevent the object from being destroyed when the function which created it returns, so the `retain` can't work. The code which tries to keep the object around will fail, end up with a dangling reference, and will crash.

Another problem is that stack objects are not very flexible. It's not uncommon in Objective-C to implement an initializer which destroys the original object and returns a new one instead. How could you do that with a stack object? You really couldn't. Much of the runtime flexibility of Objective-C depends on having heap objects.

**Actual Stack Objects in Objective-C**  
 It turns out that Objective-C does have stack objects, truly and officially, as of 10.6!

Don't get too excited, though. It's only supported for a single kind of object: blocks. When you write a block inside a function using the `^{}` syntax, the result of that expression is a stack object!

But what about those problems I discussed above?

The problem with runtime dynamism doesn't exist with blocks. Blocks have a layout which is fixed by the language, and which can't be changed without destroying binary compatibility. The size of the block object can be computed at compile time, and in fact the whole object is built by compiler-generated code, so the possibility of writing an initializer that does tricky things simply doesn't exist.

The problem of object lifetime _does_ exist with blocks, but is less severe. The reason for this is simply because blocks are a new kind of object that never existed in the language before, and any code that deals with a block will know that it needs to `copy` a block (which creates a copy on the heap, if it's not there already, and returns a pointer to that), rather than `retain` it, if it wants to keep a reference.

The stack nature of blocks does have some pitfalls, though. For example, this code is broken:

```
    void (^block)();
    if(x)
    {
        block = ^{ printf("x\n"); };
    }
    else
    {
        block = ^{ printf("not x\n"); };
    }
    block();
```

Block stack objects are only valid through the lifetime of their enclosing scope, and here, their enclosing scopes cease to exist before the call to `block()` at the end. Other gotchas can happen when you pass blocks to code that doesn't know that they're blocks:

```
    [dictionary setObject: ^{ printf("hey hey\n"); } forKey: key];
```

The dictionary will `retain` that block object rather than `copy` it, leading to a dangling reference.

The speed and simplicity of stack objects are a great boon for blocks, but it also creates a whole new class of bugs for unwary programmers.

**Conclusion**  
 That wraps things up for this week. Come back in seven days for another exciting post. Until then, [keep those suggestions coming](mailto:mike@mikeash.com). My material comes from user ideas, so if you have a topic you would like to see discussed here, send it in!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
