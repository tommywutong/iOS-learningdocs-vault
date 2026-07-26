---
title: 'Friday Q&A 2009-03-20: Objective-C Messaging'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f7038ddac043dc7a'
translated: false
---

> 原文：[Friday Q&A 2009-03-20: Objective-C Messaging](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)　·　mikeash.com Friday Q&A

Posted at 2009-03-21 01:59 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-03-27: Objective-C Message Forwarding](https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)  
Previous article: [Friday Q&A 2009-03-13: Intro to the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-03-20: Objective-C Messaging

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Chinese (translation by neoman)](https://github.com/0oneo/iOSArchive/wiki/%E7%BF%BB%E8%AF%91%3A-Objective-C-%E6%B6%88%E6%81%AF%E5%8F%91%E9%80%81).

**Definitions**  
 Before we get started on the mechanisms, we need to define our terms. A lot of people are kind of unclear on exactly what a "method" is versus a "message", for example, but this is critically important for understanding how the messaging system works at the low level.

- **Method:** an actual piece of code associated with a class, and which is given a particular name. Example: `- (int)meaning { return 42; }`
- **Message:** a name and a set of parameters sent to an object. Example: sending "meaning" and no parameters to object `0x12345678`.
- **Selector:** a particular way of representing the name of a message or method, represented as the type `SEL`. Selectors are essentially just opaque strings that are managed so that simple pointer equality can be used to compare them, to allow for extra speed. (The implementation may be different, but that's essentially how they look on the outside.) Example: `@selector(meaning)`.
- **Message send:** the process of taking a **message** and finding and executing the appropriate **method**.

**Methods**  
 The next thing that we need to discuss is what exactly a method is at the machine level. From the definition, it's a piece of code given a name and associated with a particular class, but what does it actually end up creating in your application binary?

Methods end up being generated as straight C functions, with a couple of extra parameters. You probably know that `self` is passed as an implicit parameter, which ends up being an explicit parameter. The lesser-known implicit parameter `_cmd` (which holds the selector of the message being sent) is a second such implicit parameter. Writing a method like this:

```
    - (int)foo:(NSString *)str { ...
```

Gets translated to a function like this:

```
    int SomeClass_method_foo_(SomeClass *self, SEL _cmd, NSString *str) { ...
```

(The name mangling is just illustrative, and the gcc doesn't actually generate a linker-visible symbol for methods at all.)

What, then, happens when we write some code like this?

```
    int result = [obj foo:@"hello"];
```

The compiler ends up generating code that does the equivalent of this:

```
    int result = ((int (*)(id, SEL, NSString *))objc_msgSend)(obj, @selector(foo:), @"hello");
```

I'm sorry, did you run off screaming there? I'll just wait a moment to give everybody some time to come to their senses and return....

What that ridiculous piece of code after the equals sign does is take the `objc_msgSend` function, defined as part of the Objective-C runtime, and cast it to a different type. Specifically, it casts it from a function that returns `id` and takes `id`, `SEL`, and variable arguments after that to a function that matches the prototype of the method being invoked.

To put it another way, the compiler generates code that calls `objc_msgSend` but with parameter and return value conventions matched to the method in question.

Those readers who are really awake and didn't have their wits scared out of them have now noticed that the compiler needs to know the **method**'s prototype even though all it has to work with is the **message** being sent. How does the compiler deal with this discrepancy? Quite simply, it cheats. It makes a guess at the method prototype based on the methods it can see from the declarations that it has parsed so far. If it can't find one, or there's a mismatch between the declarations it sees and the method that will actually be executed at runtime, Bad Things Happen. This is why Objective-C deals so poorly with multiple methods which have the same name but different argument/return types.

**Messaging**  
 A message send in code turns into a call to `objc_msgSend`, so what does that do? The high-level answer should be fairly apparent. Since that's the only function call present, it must look up the appropriate method implementation and then call it. Calling is easy: it just needs to jump to the appropriate address. But how does it look it up?

The Objective-C header `runtime.h` includes this as part of the (now opaque, legacy) `objc_class` structure members:

```
    struct objc_method_list **methodLists                    OBJC2_UNAVAILABLE;
```

That struct is in turn defined:

```
    struct objc_method_list {
        struct objc_method_list *obsolete                        OBJC2_UNAVAILABLE;
    
        int method_count                                         OBJC2_UNAVAILABLE;
    #ifdef __LP64__
        int space                                                OBJC2_UNAVAILABLE;
    #endif
        /* variable length structure */
        struct objc_method method_list[1]                        OBJC2_UNAVAILABLE;
    }                                                            OBJC2_UNAVAILABLE;
```

Which is just declaring a variable-length struct holding `objc_method` structs. That one is in turn defined as:

```
    struct objc_method {
        SEL method_name                                          OBJC2_UNAVAILABLE;
        char *method_types                                       OBJC2_UNAVAILABLE;
        IMP method_imp                                           OBJC2_UNAVAILABLE;
    }                                                            OBJC2_UNAVAILABLE;
```

So even though we're not supposed to touch these structs (don't worry, all the functionality for manipulating them is provided through functions in elsewhere in the header), we can still see what the runtime considers a method to be. It's a name (in the form of a selector), a string containing argument/return types (look up the `@encode` directive for more information about this one), and an `IMP`, which is just a function pointer:

```
    typedef id 			(*IMP)(id, SEL, ...);
```

Now we know enough to see how this stuff works. All `objc_msgSend` has to do is look up the class of the object you give it (available by just dereferencing it and obtaining the `isa` member that all objects contain), get the class's method list, and search through the method list until a method with the right selector is found. If nothing is there, search the superclass's list, and so on up the hierarchy. Once the right method is found, jump to the IMP of method in question.

One more detail needs to be considered here. The above procedure would work but it would be extremely slow. `objc_msgSend` only takes about a dozen CPU cycles to execute on the x86 architecture, which makes it clear that it's not going through this lengthy procedure every single time you call it. The clue to this is another `objc_class` member:

```
    struct objc_cache *cache                                 OBJC2_UNAVAILABLE;
```

And that's defined farther down:

```
    struct objc_cache {
        unsigned int mask /* total = mask + 1 */                 OBJC2_UNAVAILABLE;
        unsigned int occupied                                    OBJC2_UNAVAILABLE;
        Method buckets[1]                                        OBJC2_UNAVAILABLE;
    }
```

This defines a hash table that stores `Method` structs, using the selector as the key. The way `objc_msgSend`_really_ works is by first hashing the selector and looking it up in the class's method cache. If it's found, which it nearly always will be, it can jump straight to the method implementation with no further fuss. Only if it's not found does it have to do the more laborious lookup, at the end of which it inserts an entry into the cache so that future lookups can be fast.

(There is actually one _more_ detail beyond this which ends up being extremely important: what happens when _no_ method can be found for a given selector. But that one is so important that it deserves its own post, so look for it next week.)

**Conclusion**  
 That wraps up this week's edition. Come back next week for more. Have a question? Think Objective-C's messaging system should be done differently? Post below.

Remember, Friday Q&A is powered by your ideas. If you have an idea for a topic, tell me! Post your idea in the comments, or [e-mail them directly to me](mailto:mike@mikeash.com) (I'll use your name unless you ask me not to).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-03-20-objective-c-messaging.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
