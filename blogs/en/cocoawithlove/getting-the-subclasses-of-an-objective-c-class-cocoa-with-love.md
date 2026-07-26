---
title: 'Getting the subclasses of an Objective-C class | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/01/getting-subclasses-of-objective-c-class.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:f2f9f2f63e204aba'
translated: false
---

> 原文：[Getting the subclasses of an Objective-C class | Cocoa with Love](https://www.cocoawithlove.com/2010/01/getting-subclasses-of-objective-c-class.html)　·　Cocoa with Love (Matt Gallagher)

Getting the full list of subclasses for a class is a fairly simple task but it requires some uncommon runtime functions which can make the process more difficult. In this post, I look at how a Class is defined in Objective-C and two completely different ways of working out the subclasses.

## Introduction

Given the high level of reflection and introspection in the Objective-C runtime, you might expect that you would simply find a `class_getSubclasses(Class parentClass)` in the Objective-C Runtime API but no such function exists.

There are a few possible reasons why this function might have been omitted — dynamic class creation and loading, threading and locking concerns, historical omissions in the `class_t` structure, premature optimization considerations or even an attempt to deliberately guide programmers away from certain designs — but the result is that you must work out the subclasses for yourself.

Note: fetching the subclasses of a class is an unusual thing to do and is usually done as an after-the-fact change to an API you don't control or as a debug-only introspection or hack. Generally, designs where subclasses explicitly register themselves work better than trying to find subclasses at runtime. For example, in my [Simple, Extensible HTTP Server](https://www.cocoawithlove.com/2009/07/simple-extensible-http-server-in-cocoa.html), every `HTTPResponseHandler` must include:

```objc
+ (void)load
{
    [HTTPResponseHandler registerHandler:self];
}
```

which allows subclasses of `HTTPResponseHandler` that "opt-in" to be discovered by the parent when it is looking for a handler to handle a request.

Fetching subclasses is then used in situations where you can't include a `load` method like this or you can justify not wanting to do this (e.g. debug-only verification code which checks that all `HTTPResponseHandlers` you've written actually do register themselves).

## Filter the list of all classes

The traditional definition of a class in Objective-C looks like this:

```objc
struct objc_class {
    Class isa;
    Class super_class;
    const char *name;
    long version;
    long info;
    long instance_size;
    struct objc_ivar_list *ivars;
    struct objc_method_list **methodLists;
    struct objc_cache *cache;
    struct objc_protocol_list *protocols;
};
```

Classes contain pointers to their superclass but contain no pointer to subclasses.

Since there is no specific function to access the subclasses, the only approach using public APIs is to get the list of all classes in the runtime and test each one to see if it is a subclass of the class in question.

If this sounds like a heavy-handed approach, you're probably right. In Mac OS X 10.6.2, there are 527 classes in Foundation alone and 1966 in the Cocoa framework. This doesn't include all the classes your project will add, plus classes in other frameworks. Of course, interrogating all of these only takes a millisecond or two but it's still not something you should do in a tight loop — if you need to repeatedly use the list of subclasses for a class, you'll want to cache it somewhere.

Fetching all the classes in the runtime is pretty simple:

```objc
int numClasses = objc_getClassList(NULL, 0);
Class *classes = NULL;

classes = malloc(sizeof(Class) * numClasses);
numClasses = objc_getClassList(classes, numClasses);

// do something with classes

free(classes);
```

The question is then: how do we determine which classes are actually subclasses of some parent class?

The intuitive approach would be to use the `isSubclassOfClass:` method:

```objc
NSMutableArray *result = [NSMutableArray array];
for (NSInteger i = 0; i < numClasses; i++)
{
    if ([classes[i] isSubclassOfClass:parentClass])
    {
        [result addObject:classes[i]];
    }
}
```

Unfortunately, we can't do this because when considering all classes in the runtime, the method `isSubclassOfClass:` may not be present on all of them (since `isSubclassOfClass:` is an `NSObject` method).

The problem here is that many of the methods that are commonly considered to be implemented by all classes, are actually implemented by `NSObject` or in an implementation of the `NSObject` protocol. Some classes, like `_NSZombie_` or `NSProxy` don't derive from `NSObject` and even if they do implement the `NSObject` protocol, may do so in unpredictable ways (`_NSZombie_` throws an exception for any method and `NSProxy` forwards many of these methods to its target instead of responding for itself).

So instead of invoking any methods on arbitrary classes we must use the runtime functions. We use `class_getSuperclass()` to find out the class' superclass and compare this to the `parentClass`. This gives the complete solution:

```objc
NSArray *ClassGetSubclasses(Class parentClass)
{
    int numClasses = objc_getClassList(NULL, 0);
    Class *classes = NULL;

    classes = malloc(sizeof(Class) * numClasses);
    numClasses = objc_getClassList(classes, numClasses);
    
    NSMutableArray *result = [NSMutableArray array];
    for (NSInteger i = 0; i < numClasses; i++)
    {
        Class superClass = classes[i];
        do
        {
            superClass = class_getSuperclass(superClass);
        } while(superClass && superClass != parentClass);
        
        if (superClass == nil)
        {
            continue;
        }
        
        [result addObject:classes[i]];
    }

    free(classes);
    
    return result;
}
```

## The fast and dirty hack approach

The function I just gave is the correct approach to use in a program. But I wouldn't feel like I'd made an interesting post if I didn't also show a completely different, totally unsafe approach too.

This approach will require the Objective-C Runtime 2.0 (that's the one used in Mac OS X 64-bit and on the iPhone). In the new version of the runtime, a class actually contains a direct link to its subclasses.

From [objc-runtime-new.h in Apple's opensource repository](http://opensource.apple.com/source/objc4/objc4-437/runtime/objc-runtime-new.h), a class is declared as follows:

```objc
typedef struct class_t {
    struct class_t *isa;
    struct class_t *superclass;
    Cache cache;
    IMP *vtable;
    class_rw_t *data;
} class_t;
```

with the `class_rw_t` struct definition:

```objc
typedef struct class_rw_t {
    uint32_t flags;
    uint32_t version;

    const class_ro_t *ro;
    
    struct method_list_t **methods;
    struct chained_property_list *properties;
    struct protocol_list_t ** protocols;

    struct class_t *firstSubclass;
    struct class_t *nextSiblingClass;
} class_rw_t;
```

This means that we can traverse along the `firstSubclass` and `nextSiblingClass` members to reach all of the subclasses of a parent class without needing to read every class in the runtime.

A depth-first recursive traversal then gives the full list of subclasses for a class:

```objc
typedef void *Cache;
#import "objc-runtime-new.h"

void AddSubclassesToArray(Class parentClass, NSMutableArray *subclasses)
{
    struct class_t *internalRep = (struct class_t *)parentClass;
    
    // Traverse depth first
    Class subclass = (Class)internalRep->data->firstSubclass;
    while (subclass)
    {
        [subclasses addObject:subclass];
        AddSubclassesToArray(subclass, subclasses);
    
        // Then traverse breadth-wise
        struct class_t *subclassInternalRep = (struct class_t *)subclass;
        subclass = (Class)subclassInternalRep->data->nextSiblingClass;
    }
}
```

However, while highly efficient compared to traversing the whole list of classes, this approach cannot be safely used. According to [objc-runtime-new.m](http://opensource.apple.com/source/objc4/objc4-437/runtime/objc-runtime-new.m), all access to the `data` member of a `class_t` must be protected by the `runtimeLock` — which is inaccessible outside the runtime library itself.

Since the lock is inaccessible, it means that this approach cannot be made safe, since any thread (including threads automatically started by Cocoa) could cause you to crash.

It was a fun experiment and I hope that Apple include a function to do this safely in the future.

## Conclusion

The runtime provides no simple method to access the subclasses of a class — even in the newer version of the runtime where this data is actually stored in the class' data structure.

Filtering out classes from the list of all classes presents some interesting problems due to the classes in the runtime which don't derive from `NSObject`. Ultimately though, once you're aware of the limitations of using the full class list, getting subclasses is fairly simple.

Even though it isn't data you normally need, it would be nice if Apple had decided to offer access to the subclass data in the new version of the runtime. It is more efficient and allows the list to be generated in sorted order if required.
