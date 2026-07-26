---
title: 'Friday Q&A 2009-03-13: Intro to the Objective-C Runtime'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7d52dcef2146418c'
translated: false
---

> 原文：[Friday Q&A 2009-03-13: Intro to the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)　·　mikeash.com Friday Q&A

Posted at 2009-03-13 14:13 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-03-20: Objective-C Messaging](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)  
Previous article: [Friday Q&A 2009-03-06: Using the Clang Static Analyzer](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-03-13: Intro to the Objective-C Runtime

by [Mike Ash](https://www.mikeash.com/)

Many Cocoa programmers are only vaguely aware of the Objective-C runtime. They know it's there (and some don't even know this!), that it's important, and you can't run Objective-C without it, but that's about where it stops.

Today I want to run through exactly how Objective-C works at the runtime level and what kinds of things you can do with it.

(Note: I'll be talking only about Apple's runtime on 10.5 and later. The runtime on 10.4 and earlier is missing many APIs, instead forcing direct structure access, and the runtimes for GNU and Cocotron are different beasts entirely.)

**Objects**  
 In Objective-C we work with objects all the time, but what _is_ an object? Well, let's take a look and construct something that will tell us about them.

First, we know that objects are referred to using pointers, like `NSObject *`. And we know that we create them using the `+alloc` method. The documentation for that just says that it calls `+allocWithZone:`. Following the chain of documentation a bit further, we discover `NSDefaultMallocZone` and see that they're just allocated using `malloc`. Easy!

But what do they look like when they're allocated? Let's find out:

```
    #import <Foundation/Foundation.h>
    
    @interface A : NSObject { @public int a; } @end
    @implementation A @end
    @interface B : A { @public int b; } @end
    @implementation B @end
    @interface C : B { @public int c; } @end
    @implementation C @end
    
    int main(int argc, char **argv)
    {
        [NSAutoreleasePool new];
        
        C *obj = [[C alloc] init];
        obj->a = 0xaaaaaaaa;
        obj->b = 0xbbbbbbbb;
        obj->c = 0xcccccccc;
        
        NSData *objData = [NSData dataWithBytes:obj length:malloc_size(obj)];
        NSLog(@"Object contains %@", objData);
        
        return 0;
    }
```

We construct a class hierarchy that just has some instance variables, then we put obvious values into each ivar. Then we extract the data in nice printable form using

to get the right length, and use

to print a nice hex representation. Here's what we get:

```
    2009-01-27 15:58:04.904 a.out[22090:10b] Object contains <20300000 aaaaaaaa bbbbbbbb cccccccc>
```

We can see here that the class just gets laid out sequentially in memory. First you have A's ivar, then B's, then C's. Easy!

But what's this `20300000` thing at the beginning? Well, it comes before A's ivar, so it must be NSObject's. Let's look at NSObject's definition:

```
    /***********	Base class		***********/
    
    @interface NSObject  {
        Class	isa;
    }
```

Sure enough, there's another ivar. But what's this

business? If we tell Xcode to take us to the definition we find ourselves in

which contains:

```
    typedef struct objc_class *Class;
```

And following it further we get to

which contains:

```
    struct objc_class {
        Class isa;
    
    #if !__OBJC2__
        Class super_class                                        OBJC2_UNAVAILABLE;
        const char *name                                         OBJC2_UNAVAILABLE;
        long version                                             OBJC2_UNAVAILABLE;
        long info                                                OBJC2_UNAVAILABLE;
        long instance_size                                       OBJC2_UNAVAILABLE;
        struct objc_ivar_list *ivars                             OBJC2_UNAVAILABLE;
        struct objc_method_list **methodLists                    OBJC2_UNAVAILABLE;
        struct objc_cache *cache                                 OBJC2_UNAVAILABLE;
        struct objc_protocol_list *protocols                     OBJC2_UNAVAILABLE;
    #endif
    
    } OBJC2_UNAVAILABLE;
```

So a

is a pointer to a structure which... starts with another

.

Let's look at another root class, `NSProxy`:

```
    @interface NSProxy  {
        Class	isa;
    }
```

It's there too. Let's look in one more place, the definition of

, the Objective-C type for "any object":

```
    typedef struct objc_object {
        Class isa;
    } *id;
```

There it is again. Clearly every single Objective-C object must start with

, even class objects. But what is it?

As the name and type imply, the `isa` ivar indicates what class a particular object is. Every Objective-C object must begin with an isa pointer, otherwise the runtime won't know how to work with it. Everything about a particular object's type is wrapped up in that one little pointer. The remainder of an object is basically just a big blob and as far as the runtime is concerned, it is irrelevant. It's up to the individual classes to give that blob meaning.

**Classes**  
 What exactly do classes contain, then? The "unavailable" structure members give a good clue. (They're there for compatibility with the pre-Leopard runtime, and you shouldn't use them if you're targeting Leopard, but it still tells us what kind of information is there.) First comes the `isa`, which allows a class to act like an object as well. There's a pointer to the superclass, giving the proper class hierarchy. Some other basic information about the class follows. At the end is the really interesting stuff. There's a list of instance variables, a list of methods, and a list of protocols. All of this stuff is accessible at runtime, and can be modified at runtime too.

I skipped right over the `cache` member because it's not really useful for runtime manipulation, but it's an interesting exposure of an implementation detail. Every time you send a message (`[foo bar]`) the runtime has to look up the actual code to invoke by rummaging through the list of methods in the target object's class. However, methods are stored in big linear lists by default, so this is really slow. The cache is just a hash table mapping selectors to code. The first time you send a message you'll get a slow, time-consuming lookup, but the result is put in the hash table. Subsequent calls will find the entry in the hash table, making the process go much faster.

Looking at the rest of `runtime.h` you'll see a lot of functions for accessing and manipulating these properties. Each function is prefixed with what it operates on. General runtime functions start with `objc_`, functions that operate on a class start with `class_`, and so forth. For example, you can call `class_getInstanceMethod` to get information about a particular method, like the argument/return types. Or you can call `class_addMethod` to add a _new_ method to an existing class at runtime. You can even create a whole new class at runtime by using `objc_allocateClassPair`.

**Practical Applications**  
 There are tons of useful things that can be done with this kind of runtime meta-information, but here are some ideas.

1. Apple's Key-Value Coding does this kind of thing already: you give it a name, and it looks up a method or ivar based on that name and does some stuff with it. You can do that kind of thing yourself, in case you need to look up an ivar based on a name or something of the sort.
2. Using

  you can get a list of all classes currently known to the runtime, and by tracing out the class hierarchy, you can identify which ones subclass a given class. This can let you write subclasses to handle specialized data formats or other such situations and let the superclass look them up without having to tediously register every subclass manually.
3. This can be useful for custom unit testing frameworks and the like. Similar to #2, but look for a method being implemented rather than a particular class hierarchy.
4. The runtime provides a complete set of tools for re-pointing methods to custom implementations so that you can change what classes do without touching their source code.
5. The

  keyword is handy for making the compiler generate setters/getters but it still forces you to write cleanup code in

  . By reading meta-information about the class's properties, you can write code that will go through and clean up all synthesized properties automatically instead of having to write code for each case.
6. By dynamically generating classes at runtime, and by looking up the necessary properties on demand, you can create a bridge between Objective-C and another (sufficiently dynamic) language.
7. Don't feel limited to the above, come up with your own ideas!

**Wrapping Up**  
 Objective-C is a powerful language and the comprehensive runtime API is an extremely useful part of it. While it may be a bit ugly groveling around in all that C code, it's really not that difficult to work with, and it's well worth the power it provides.

That's it for this week's Friday Q&A. Please send in your suggestions, either by posting them below or [by e-mail](mailto:mike@mikeash.com) (tell me if you don't want me to use your name). Friday Q&A runs on your suggestions so please write in!

Have a favorite use of the ObjC runtime? Something you dislike about it? Have a tip to share? Post it all below.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
