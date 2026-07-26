---
title: 'the last Friday Q&A'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-11-6-creating-classes-at-runtime-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:15e1088a338c44d5'
translated: false
---

> 原文：[the last Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2010-11-6-creating-classes-at-runtime-in-objective-c.html)　·　mikeash.com Friday Q&A

Posted at 2010-11-05 17:08 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Summary of the Current State of my Publications](https://www.mikeash.com/pyblog/summary-of-the-current-state-of-my-publications.html)  
Previous article: [Friday Q&A Will Return](https://www.mikeash.com/pyblog/friday-qa-will-return.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-11-6: Creating Classes at Runtime in Objective-C

by [Mike Ash](https://www.mikeash.com/)

**`MAObjCRuntime`**  
 One of the things I did during my off time was build [`MAObjCRuntime`](http://github.com/mikeash/MAObjCRuntime), a nice OO wrapper around a lot of common runtime functionality, including everything that I'm going to talk about today. For my discussion today I will _not_ involve `MAObjCRuntime`, so that you can see how to use the runtime directly.

If you decide to use these techniques on your own, I'd recommend using `MAObjCRuntime` instead, as it makes life considerably easier.

**What and Why**  
 What exactly does it mean to create a class at runtime? If you've done any Objective-C at all, you know what it means to create a class. You create an `@interface` block, an `@implementation` block, add instance variables and methods, and you have a class that you can use.

Creating a class at runtime gives you the same result. The difference is that you write code which calls into the runtime to create class structures in memory directly, rather than writing classes to be interpreted by the compiler. You can add methods and instance variables just as you would normally.

Why would you do such a thing? It's often handy to create new classes at runtime to override functionality in arbitrary classes. For example, [`MAZeroingWeakRef`](http://github.com/mikeash/MAZeroingWeakRef") does this in order to catch memory management events in order to implement zeroing weak references.

**Creating a Class**  
 The act of creating a class is accomplished using the `objc_allocateClassPair` function in `objc/runtime.h`. You pass it a superclass, a name, and a size for per-class storage (generally best left at `0`), and it returns a class to you:

```
    Class mySubclass = objc_allocateClassPair([NSObject class], "MySubclass", 0);
```

And that's it! Of course this is pretty boring, since the new class doesn't do anything yet. I'll cover how to actually put things into it shortly.

An aside: why is it called "allocate class _pair_"? As you probably already know, all Objective-C classes are also Objective-C objects. You can put them in variables, send them messages, add them to arrays, etc. just like you would with any other object. All objects have a class, and the class of a class is called the _metaclass_. Each class has a unique metaclass, and thus the _pair_: `objc_allocateClassPair` allocates both the class and the metaclass together.

A full discussion of what the metaclass is and how it works is beyond the scope of this post, but Greg Parker has [a good discussion of metaclasses](http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html) if you're interested in reading more.

**Adding Methods**  
 You know how to create a class, but it won't do anything interesting unless you actually put things in it.

Methods are the most obvious things to add to a newly created class. You add methods to a class using the `class_addMethod` function in `objc/runtime.h`. This function takes four parameters.

The first two parameters are the class you want to manipulate, and the selector of the method that you want to add. Both of these should be pretty obvious.

The next parameter is an `IMP`. This type is a special Objective-C `typedef` for a function pointer. It's defined as:

```
    typedef id (*IMP)(id, SEL, ...);
```

Objective-C methods take two implicit parameters, `self` and `_cmd`, which are the first two parameters listed here. The other parameters are not listed, and are up to you.

To create the `IMP` that you pass to this function, implement a function that takes `id self` and `SEL _cmd` as its first two parameters. The rest of the parameters are the parameters that the method will take, and the return type is the method return type.

For example, let's say you wanted to write an `IMP` with this signature:

```
    - (NSUInteger)countOfObject: (id)obj;
```

You'd write the function like this:

```
    static NSUInteger CountOfObject(id self, SEL _cmd, id obj)
```

Unfortunately, the type of this function doesn't match the `IMP` typedef, so you have to cast it when passing it to `class_addMethod`.

The last parameter is a type encoding string which describes the type signature of the method. This is the string that the runtime uses to generate the `NSMethodSignature` that's returned from `methodSignatureForSelector:`, among other uses.

The best way to generate this type encoding string is to retrieve it from an existing class which has a method with the same signature. This way you can just trust the compiler to get it right and don't have to worry about the details of how these strings are put together. For example, the method above has the same signature as `-[NSArray indexOfObject:]`, so you can retrieve that type encoding string:

```
    Method indexOfObject = class_getInstanceMethod([NSArray class],
                                                   @selector(indexOfObject:));
    const char *types = method_getTypeEncoding(indexOfObject);
```

If no existing class has a matching method, consider writing a small dummy class that does, and then querying it.

If you absolutely must build your own type encoding string (not recommended), then you can do it using the `@encode` directive to generate strings for the individual components, then combine them. Compiler-generated strings also have numeric stack offset information embedded in them, which means that your string won't completely match its output, but it's often good enough.

The components of a method's type encoding string are simply the `@encode` representation of the return type, followed by the argument types, including the two implicit parameters at the beginning:

```
    NSString *typesNS = [NSString stringWithFormat: @"%s%s%s%s",
                         @encode(NSUInteger),
                         @encode(id), @encode(SEL),
                         @encode(id)];
    const char *types C = [typesNS UTF8String];
```

But again, avoid this if it's at all possible.

Here's a full example of adding a `description` method to a newly created class:

```
    static NSString *Description(id self, SEL _cmd)
    {
        return [NSString stringWithFormat: @"<%@ %p: foo=%@>", [self class], self, [self foo]];
    }
    
    // add Description to mySubclass
    
    // grab NSObject's description signature so we can borrow it
    Method description = class_getInstanceMethod([NSObject class],
                                                 @selector(description));
    const char *types = method_getTypeEncoding(description);
    
    // now add
    class_addMethod(mySubclass, @selector(description), (IMP)Description, types);
```

A bit verbose, but not too difficult at all.

**Adding Instance Variables**  
 You can add instance variables to a class using the `class_addIvar` method.

The first two parameters to this function are the class to manipulate and the name of the instance variable you want to add. Both are straightforward.

The next parameter is the size of the instance variable. If you're using a plain C type as the instance variable, then you can simply use `sizeof` to get the size.

Next is the alignment of the instance variable. This indicates how the instance variable's storage needs to be aligned in memory, potentially with padding in between it and the end of the previous instance variable. A trick to this parameter is that it's the log~2 of the alignment rather than the alignment itself. Passing `1` means aligning it to a 2-byte boundary, passing `4` means 16-byte alignment, etc. Since most types want to be aligned to their size, you can simply use `rint(log2(sizeof(type)))` to generate the value of this parameter.

The last parameter is a type encoding string for the parameter. This can be generated using the `@encode` directive and giving it the type of the variable that you're adding.

Here's a full example of adding an `id` instance variable:

```
    class_addIvar(mySubclass, "foo", sizeof(id), rint(log2(sizeof(id))), @encode(id));
```

**Accessing Added Instance Variables**  
 Accessing this newly-added variable is not as easy as it normally would be. You can't just write `foo` in your code, because the compiler has no idea that this thing even exists.

The runtime provides two functions for accessing instance variables: `object_setInstanceVariable` and `object_getInstanceVariable`. They take an object and a name, and either a value to set, or a place to put the current value. Here's an example of getting and setting the `foo` variable constructed above:

```
    id currentValue;
    object_getInstanceVariable(obj, "foo", &currentValue);
    // it will be replaced, so autorelease
    [currentValue autorelease];
    
    id newValue = ...;
    [newValue retain]; // runtime won't retain for us
    object_setInstanceVariable(obj, "foo", newValue);
```

Another way is to simply use key-value coding to read and write the instance variable. As long as you don't have a method with the same name, it will directly access the variable's contents. It will also do proper memory management on object-type variables. As a potential downside, it will box primitive values in `NSValue` or `NSNumber` objects, which could add complication.

With either technique, don't forget to add a `dealloc` method to release your object instance variables.

If you need per-instance storage, consider using the associated object API (`objc_setAssociatedObject` and `objc_getAssociatedObject`) instead of instance variables. It takes care of memory management for you.

**Adding Protocols**  
 You can add a protocol to a class using `class_addProtocol`. This is not usually very useful, so I won't go into how to use it. Keep in mind that this function only declares the class as conforming to the protocol in question, but it doesn't actually add any code. If you want the class to _actually_ implement the methods in a protocol, you have to implement and add those methods yourself.

**Adding Properties**  
 Although there are plenty of functions for _querying_ the properties of a class, Apple apparently forgot to provide any way to _add_ a property to a class. Fortunately, like protocols, it's not usually very useful to add a property to a class at runtime, so this is not a big loss.

**Registering the Class**  
 After you're done setting up the class, you have to register it before you can use it. You do this with the `objc_registerClassPair` function:

```
    objc_registerClassPair(mySubclass);
```

It's now ready to use.

Note that you must register a class before you use it, and you can't add any instance variables to a class after you register it. You _can_ add methods to a class after registration, however.

**Using the Class**  
 Once you've registered the class, you can message it just like you would any other class:

```
    id myInstance = [[mySubclass alloc] init];
    NSLog(@"%@", myInstance);
```

You can access the class using `NSClassFromString` as well, and in general it behaves just like any other class at this point.

**Conclusion**  
 Now you know how to create a new class at runtime, how to add methods and instance variables to it, and then use it from code. In two weeks, I'll cover how to actually do useful and interesting things with the above, instead of just using four times the code to imitate what the compiler does. Until then, keep [sending in your suggestions for topics](mailto:mike@mikeash.com); the next article is already booked, but I'm open for ideas after that.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-11-6-creating-classes-at-runtime-in-objective-c.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
