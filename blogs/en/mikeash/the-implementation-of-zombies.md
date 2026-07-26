---
title: the implementation of zombies
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:948667e0dd9ba332'
translated: false
---

> 原文：[the implementation of zombies](https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)　·　mikeash.com Friday Q&A

Posted at 2011-05-20 16:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-06-03: Objective-C Blocks vs. C++0x Lambdas: Fight!](https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)  
Previous article: [Friday Q&A 2011-05-06: A Tour of MABlockClosure](https://www.mikeash.com/pyblog/friday-qa-2011-05-06-a-tour-of-mablockclosure.html)  
Tags: [braaaiiiinnnssss](https://www.mikeash.com/pyblog/?tag=braaaiiiinnnssss) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [zombie](https://www.mikeash.com/pyblog/?tag=zombie)

Friday Q&A 2011-05-20: The Inner Life of Zombies

by [Mike Ash](https://www.mikeash.com/)

**Zombie Overview**  
 [As you may recall](http://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html), an Objective-C object is just a block of allocated memory. The first pointer-sized chunk of that block is the `isa` pointer, which points to the object's class. The rest of the block contains the object's instance variables.

When an object is deallocated, the block of memory which contains it is freed. Normally this means that it's simply marked as being available for reuse. If you've screwed up and kept a pointer to this deallocated object, many mysterious things can happen.

In some cases, code which tries to use the deallocated object will work just fine. If the deallocated memory hasn't actually been overwritten yet, it will still behave like a normal Objective-C object.

Frequently, the deallocated memory will be reused to hold a new object. In this case, the old pointer ends up pointing to this new object. Attempts to use the old pointer will send messages to the new object instead, with confusing results. This is why one of the most common symptoms of a memory management error is a mystery object, like a random `NSString`, showing up where you expected to see something else.

Occasionally, the memory will be overwritten with something that's not an object, and your code crashes. This is the best outcome of the three, since it fails more quickly and makes it more clear what's going wrong, but it also tends to be rare.

Zombies greatly improve the diagnostics available for this common scenario. Instead of simply leaving the deallocated memory alone, zombies take it over and replace it with an object which traps all attempts to access it. Thus the term "zombie": the dead object is resurrected to a sort of unlife. When a zombie object is messaged, it logs an error and crashes, providing a convenient backtrace so you can see exactly where the problem lies.

**Using Zombies**  
 Zombies can be enabled by setting the `NSZombieEnabled` environment variable to `YES`. Run the app in `gdb`, and it will crash on any attempted access to a dead object. Be careful, though: by default, zombies are never deallocated, so your app's memory usage can become extremely high.

Another useful option is the Zombies instruments in Instruments. This enables zombies and also tracks objects' retain counts so that you can go back and see the retain/release activity for any improperly messaged object.

**Investigating Zombies**  
 Let's take a look at what these things are doing behind the scenes. To help with the investigation, I wrote a small function to dump the contents of an object:

```
    void Dump(NSString *msg, id obj, int size)
    {
        NSString *s = [NSString stringWithFormat: @"%@ malloc_size %d - %@", msg, (int)malloc_size(obj), [NSData dataWithBytes: obj length: size]];
        printf("%s\n", [s UTF8String]);
    }
```

For the size, the caller can use `malloc_size` to get the size of the allocated block of memory. This is left up to the caller because `malloc_size` won't work on a deallocated block, so the caller will need to fetch the size while the object is still live and then keep it around.

Let's create an `NSObject` and log it before and after being destroyed:

```
    id obj = [[NSObject alloc] init];
    int size = malloc_size(obj);
    Dump(@"Fresh NSObject", obj, size);
    [obj release];
    Dump(@"Destroyed NSObject", obj, size);
```

Here's a normal run without zombies:

```
    Fresh NSObject malloc_size 16 - <68046370 ff7f0000 00000000 00000000>
    Destroyed NSObject malloc_size 0 - <68046370 ff7f0000 00000000 00000000>
```

Notice how `malloc_size` went to `0` after being destroyed, indicating that the memory block is now freed. Also notice that nothing else changes. The object contains the exact same thing before and after being destroyed. This object could still be used after being destroyed.

Let's try another one with zombies enabled:

```
    Fresh NSObject malloc_size 16 - <68046370 ff7f0000 00000000 00000000>
    Destroyed NSObject malloc_size 16 - <d0011100 01000000 00000000 00000000>
```

Now we're seeing some differences. First of all, `malloc_size` is still reporting `16`, so the memory was never deallocated. Secondly, the contents of the object have changed. The `isa` pointer occupies the first eight bytes of the object (running in 64-bit mode here), or the first two groups in the above dump. The `isa` pointer is completely different afterwards.

The second eight bytes is just unused here. Let's write a quick dummy class that uses it and see how it behaves:

```
    @interface Dummy : NSObject
    {
        uintptr_t secondEight;
    }
    @end
```

```
    @implementation Dummy
    - (id)init
    {
        if((self = [super init]))
            secondEight = 0xdeadbeefcafebabeULL;
        return self;
    }
    @end
```

Let's then add some code to dump one of these as well:

```
    obj = [[Dummy alloc] init];
    size = malloc_size(obj);
    Dump(@"Fresh Dummy", obj, size);
    [obj release];
    Dump(@"Destroyed Dummy", obj, size);
```

Here's a run without zombies:

```
    Fresh Dummy malloc_size 16 - <28110000 01000000 bebafeca efbeadde>
    Destroyed Dummy malloc_size 0 - <28110000 01000000 bebafeca efbeadde>
```

As before, nothing changes when it's deallocated. Note that the contents of `secondEight` are backwards because this code is running on a little-endian architecture.

Here's a run with zombies:

```
    Fresh Dummy malloc_size 16 - <28110000 01000000 bebafeca efbeadde>
    Destroyed Dummy malloc_size 16 - <e0071100 01000000 bebafeca efbeadde>
```

The rest of the object is left alone, but once again the `isa` pointer is overwritten. Let's see just what this new `isa` pointer is:

```
    NSLog(@"%s", class_getName(object_getClass(obj)));
```

Running this tells us that the class is called `_NSZombie_Dummy`. We can see that zombies work by overwriting the `isa` pointer with a special zombie class. This special zombie class incorporates the name of the original class, making it easy to see what the original class was and making diagnostics much simpler.

Let's see just what this class contains. Here's a function which will dump out various information about a class:

```
    void DumpClass(Class c)
    {
        printf("Dumping class %s\n", class_getName(c));
        
        printf("Superclass: %s\n", class_getName(class_getSuperclass(c)));
        
        printf("Ivars:\n");
        Ivar *ivars = class_copyIvarList(c, NULL);
        for(Ivar *cursor = ivars; cursor && *cursor; cursor++)
            printf("    %s %s %d\n", ivar_getName(*cursor), ivar_getTypeEncoding(*cursor), (int)ivar_getOffset(*cursor));
        free(ivars);
        
        printf("Methods:\n");
        Method *methods = class_copyMethodList(c, NULL);
        for(Method *cursor = methods; cursor && *cursor; cursor++)
            fprintf(stderr, "    %s %s\n", sel_getName(method_getName(*cursor)), method_getTypeEncoding(*cursor));
        free(methods);
    }
```

Now to run this on the deallocated instance of `Dummy`:

```
    DumpClass(object_getClass(obj));
```

Here's what it prints:

```
    Dumping class _NSZombie_Dummy
    Superclass: nil
    Ivars:
        isa # 0
    Methods:
```

This class contains essentially nothing. Other than the `isa` ivar (which every class needs to have), there's nothing there. No superclass, no other instance variables, no methods.

What, then, happens when we try to message an instance of this empty class? I put `[obj self]` in the code after destroying the object and then ran it in `gdb`. Here's the result:

```
    2011-05-19 14:42:39.427 a.out[62888:a0f] *** -[Dummy self]: message sent to deallocated instance 0x1001106b0
    
    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x00007fff82a4d6c6 in ___forwarding___ ()
    (gdb) bt
    #0  0x00007fff82a4d6c6 in ___forwarding___ ()
    #1  0x00007fff82a49a68 in __forwarding_prep_0___ ()
    #2  0x0000000100001c49 in main (argc=1, argv=0x7fff5fbff690) at zomb.m:62
```

The `___forwarding___` stuff is the part of the runtime that takes over when the target object doesn't implement the message that was sent to it. It's called "forwarding" because [forwarding messages to other objects](http://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html) is one of its major uses.

The forwarding mechanism is throwing a `SIGTRAP` because the class doesn't implement the minimum necessary forwarding methods. What's logging "message sent to deallocated instance", though? Let's put a breakpoint on `CFLog` and find out:

```
    Breakpoint 2, 0x00007fff82a98327 in CFLog ()
    (gdb) bt
    #0  0x00007fff82a98327 in CFLog ()
    #1  0x00007fff82a4d6c5 in ___forwarding___ ()
    #2  0x00007fff82a49a68 in __forwarding_prep_0___ ()
    #3  0x0000000100001c49 in main (argc=1, argv=0x7fff5fbff690) at zomb.m:62
    (gdb) cont
    Continuing.
    2011-05-19 15:45:03.905 a.out[62938:a0f] *** -[Dummy self]: message sent to deallocated instance 0x1001106b0
```

And so we can see that the runtime forwarding mechanism itself emits this log after detecting the zombie class.

**Conclusion**  
 Zombies are a really useful tool for debugging memory problems. Under the hood, zombies work by rewriting the object's `isa` pointer to point to a special zombie class associated with the original. When a message is sent to an instance of the special zombie class, it gets trapped by the runtime's message forwarding system which then logs the event and crashes the app.

That wraps things up for today. Come back in two more weeks for the next one, just in time for WWDC. In the meantime, as always, [keep sending me your ideas for topics](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
