---
title: Last time
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af9fac8d2731cb8f'
translated: false
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)　·　mikeash.com Friday Q&A

Posted at 2013-01-25 15:32 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-02-08: Let's Build Key-Value Coding](https://www.mikeash.com/pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html)  
Previous article: [Friday Q&A 2013-01-11: Mach Exception Handlers](https://www.mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-01-25: Let's Build NSObject

by [Mike Ash](https://www.mikeash.com/)

**Components of a Root Class**  
What exactly does a root class do? In terms of Objective-C itself, there is precisely one requirement: the root class's first instance variable must be `isa`, which is a pointer to the object's class. The `isa` is used to figure out what class an object is when dispatching messages. That's all there has to be, from a strict language standpoint.

A root class that only provides that wouldn't be very useful, of course. `NSObject` provides a lot more. The functionality it provides can be broken down into three categories:

1. **Memory management:** standard memory management methods like `retain` and `release` are implemented in `NSObject`. The `alloc` method is also implemented there.
2. **Introspection:**`NSObject` provides a bunch of methods that are essentially wrappers around Objective-C runtime functionality, such as `class`, `respondsToSelector:`, and `isKindOfClass:`.
3. **Default implementations of miscellaneous methods:** there are a bunch of methods that we count on every object implementing, such as `isEqual:` and `description`. In order to ensure that every object has an implementation, `NSObject` provides a default implementation that every subclass gets if it doesn't bring its own.

**Code**  
I'll be reimplementing `NSObject` functionality as `MAObject`. I've posted the full code for this article on GitHub:

[https://github.com/mikeash/MAObject](https://github.com/mikeash/MAObject)

Note that this code is built without ARC. Although ARC is great and should be used whenever possible, it really gets in the way when implementing a root class, because a root class needs to implement memory management and ARC prefers that you leave memory management up to the compiler.

**Instance Variables**  
`MAObject` has two instance variables. The first is the `isa` pointer. The second is the object's reference count:

```
    @implementation MAObject {
        Class isa;
        volatile int32_t retainCount;
    }
```

The reference count will be managed using functions from `OSAtomic.h` to ensure thread safety, which is why it has a somewhat unusual definition rather than just using `NSUInteger` or similar.

`NSObject` actually holds reference counts externally. There's a global table which maps an object's address to its reference count. This saves memory, because the table represents the common reference count of `1` by not having an entry in the table at all. However, this technique is complex and a bit slow, so I opted not to follow it for my own version.

**Memory Management**  
The first thing that `MAObject` needs to be able to do is to create instances. This is done by implementing the `+alloc` method. (I'm skipping the deprecated and rarely used `+allocWithZone:`, which these days does the same thing and ignores its parameter anyway.)

Subclasses rarely override `+alloc`, and rely on the root class to allocate memory for them. That means that `MAObject` needs to be able to allocate instances not only of `MAObject`, but of any subclass. This is done by taking advantage of the fact that the value of `self` in a class method is the class the message was actually sent to. If code does `[SomeSubclass alloc]`, then `self` holds a pointer to `SomeSubclass`. That class can then be used to query the runtime to figure out how much memory to allocate, and to set the `isa` pointer correctly. The retain count is also initialized to `1`, as suits a newly allocated object:

```
    + (id)alloc
    {
        MAObject *obj = calloc(1, class_getInstanceSize(self));
        obj->isa = self;
        obj->retainCount = 1;
        return obj;
    }
```

The `retain` method simply uses `OSAtomicIncrement32` to bump up the retain count, and returns `self`:

```
    - (id)retain
    {
        OSAtomicIncrement32(&retainCount);
        return self;
    }
```

The release method does a bit more. It first decrements the retain count. If the retain count was decremented to `0`, then the object needs to be destroyed, so the code calls `dealloc`:

```
    - (oneway void)release
    {
        uint32_t newCount = OSAtomicDecrement32(&retainCount);
        if(newCount == 0)
            [self dealloc];
    }
```

The implementation of `autorelease` calls `NSAutoreleasePool` to add `self` to the current autorelease pool. Autorelease pools are part of the runtime these days, so this is a somewhat indirect route, but the autorelease APIs in the runtime are private, so this is the best we can do for now:

```
    - (id)autorelease
    {
        [NSAutoreleasePool addObject: self];
        return self;
    }
```

The `retainCount` method simply returns the value held in the ivar:

```
    - (NSUInteger)retainCount
    {
        return retainCount;
    }
```

Finally, there's the `dealloc` method. In normal classes, `dealloc` needs to clean up any instance variables and then call `super`. The root class has to actually dispose of the memory occupied by the object itself. In this case, it's just a simple call to `free`:

```
    - (void)dealloc
    {
        free(self);
    }
```

There are a couple of helper methods as well. `NSObject` provides a do-nothing `init` method for consistency, so that subclasses can always call `[super init]`:

```
    - (id)init
    {
        return self;
    }
```

There's also a `new` method, which is just a wrapper around `alloc` and `init`:

```
    + (id)new
    {
        return [[self alloc] init];
    }
```

There's also an empty `finalize` method. `NSObject` implements this as part of its garbage collection support. `MAObject` doesn't support garbage collection in the first place, but I included this just because `NSObject` has it:

```
    - (void)finalize
    {
    }
```

**Introspection**  
Many of the introspection methods are just wrappers around runtime functions. Since that's not too interesting, I'll give a brief discussion of what the runtime function is doing behind the scenes as well.

The simplest introspection method is `class`, which just returns the value of `isa`:

```
    - (Class)class
    {
        return isa;
    }
```

Technically, this method will fail on tagged pointers. A proper implementation should call `object_getClass`, which behaves correctly for tagged pointers, and extracts the `isa` from a normal pointer.

The `superclass` instance method is equivalent to just invoking the `superclass` class method on the object's class, so that's exactly what the method does:

```
    - (Class)superclass
    {
        return [[self class] superclass];
    }
```

There are also class methods for these. The `+class` method just returns `self`, which is the class object. This is a little weird, but it's how `NSObject` does things. `[obj class]` returns the object's class, but `[MyClass class]` just returns a pointer to `MyClass` itself. It's not consistent, as `MyClass` also has a class, which is the `MyClass` metaclass, but it's how things are done:

```
    + (Class)class
    {
        return self;
    }
```

The `+superclass` method does what it says. This is implemented by calling `class_getSuperclass`, which just grovels around inside the class structure maintained by the runtime and pulls out the pointer to the superclass.

```
    + (Class)superclass
    {
        return class_getSuperclass(self);
    }
```

There are also methods for querying whether an object's class matches a particular class. The simple one is `isMemberOfClass:`, which does a strict check, ignoring subclasses. Its implementation is simple:

```
    - (BOOL)isMemberOfClass: (Class)aClass
    {
        return isa == aClass;
    }
```

The `isKindOfClass:` method checks subclasses too, so that `[subclassInstance isKindOfClass: [Superclass class]]` returns `YES`. The output of this method is essentially the same as that of the class method `isSubclassOfClass:`, so it just calls through:

```
    - (BOOL)isKindOfClass: (Class)aClass
    {
        return [isa isSubclassOfClass: aClass];
    }
```

That method gets a bit more interesting. Starting from `self`, it walks up the class hierarchy, comparing with the target class at each level. If it finds a match, it returns `YES`. If it runs off the top of the class hierarchy without ever finding a match, it returns `NO`:

```
    + (BOOL)isSubclassOfClass: (Class)aClass
    {
        for(Class candidate = self; candidate != nil; candidate = [candidate superclass])
            if (candidate == aClass)
                return YES;

        return NO;
    }
```

It's interesting to note that this check is not particularly efficient. If you call this method on a class that's deep in the class hierarchy, it can take a lot of loop iterations before it returns `NO`. Because of that, `isKindOfClass:` checks can be quite a lot slower than message sends, and can actually be substantial bottlenecks in certain cases. Just one more reason to avoid them when possible.

The `respondsToSelector:` method just calls through to the runtime function `class_respondsToSelector`. That, in turn, looks up the selector in the class's method table to see if it has an entry:

```
    - (BOOL)respondsToSelector: (SEL)aSelector
    {
        return class_respondsToSelector(isa, aSelector);
    }
```

There's a class method, `instancesRespondToSelector:`, which is nearly identical. The only difference is passing `self`, which is the class in this context, rather than `isa`, which would be the metaclass here:

```
    + (BOOL)instancesRespondToSelector: (SEL)aSelector
    {
        return class_respondsToSelector(self, aSelector);
    }
```

There are also two `conformsToProtocol:` methods, one for instances and one for classes. These also just wrap a runtime function, which in this case just consults a table of every protocol that the class conforms to in order to see if the given protocol is present:

```
    - (BOOL)conformsToProtocol: (Protocol *)aProtocol
    {
        return class_conformsToProtocol(isa, aProtocol);
    }

    + (BOOL)conformsToProtocol: (Protocol *)protocol
    {
        return class_conformsToProtocol(self, protocol);
    }
```

Next is `methodForSelector:`, and its classy cousin `instanceMethodForSelector:`. These both call through to `class_getMethodImplementation`, which looks up the selector in the class's method table and returns the corresponding `IMP`:

```
    - (IMP)methodForSelector: (SEL)aSelector
    {
        return class_getMethodImplementation(isa, aSelector);
    }

    + (IMP)instanceMethodForSelector: (SEL)aSelector
    {
        return class_getMethodImplementation(self, aSelector);
    }
```

An interesting aspect of these methods is that `class_getMethodImplementation` always returns an `IMP`, even for unknown selectors. When the class doesn't actually implement a method, it returns a special forwarding IMP which wraps up the message arguments starts down the path to invoking `forwardInvocation:`.

The `methodSignatureForSelector:` method just wraps the equivalent class method:

```
    - (NSMethodSignature *)methodSignatureForSelector: (SEL)aSelector
    {
        return [isa instanceMethodSignatureForSelector: aSelector];
    }
```

The class method in turn wraps some runtime calls. It first fetches the `Method` for the given selector. If it can't be found, then the class doesn't implement that method, and this code returns `nil`. Otherwise, it extracts the C string representing the method's types, and wraps the in an `NSMethodSignature` object:

```
    + (NSMethodSignature *)instanceMethodSignatureForSelector: (SEL)aSelector
    {
        Method method = class_getInstanceMethod(self, aSelector);
        if(!method)
            return nil;

        const char *types = method_getTypeEncoding(method);
        return [NSMethodSignature signatureWithObjCTypes: types];
    }
```

Finally, there's `performSelector:`, and the two `withObject:` variants that take arguments. These aren't strictly introspection, but they fall in the same general category of wrapping lower-level runtime functionality. They simply retrieve the `IMP` for the given selector, cast it to the appropriate function pointer type, and call it:

```
    - (id)performSelector: (SEL)aSelector
    {
        IMP imp = [self methodForSelector: aSelector];
        return ((id (*)(id, SEL))imp)(self, aSelector);
    }

    - (id)performSelector: (SEL)aSelector withObject: (id)object
    {
        IMP imp = [self methodForSelector: aSelector];
        return ((id (*)(id, SEL, id))imp)(self, aSelector, object);
    }

    - (id)performSelector: (SEL)aSelector withObject: (id)object1 withObject: (id)object2
    {
        IMP imp = [self methodForSelector: aSelector];
        return ((id (*)(id, SEL, id, id))imp)(self, aSelector, object1, object2);
    }
```

**Default Implementations**  
`MAObject` provides default implementations of a bunch of methods. We'll start off with default implementations of `isEqual:` and `hash`, which just use the object's pointer for identity purposes:

```
    - (BOOL)isEqual: (id)object
    {
        return self == object;
    }

    - (NSUInteger)hash
    {
        return (NSUInteger)self;
    }
```

Any subclasses with a more expansive notion of equality will have to override these methods, but any subclass where an object is only ever equal to itself can just use these implementations.

The `description` method is another handy one to have a default implementation. This implementation just generates a string of the form `<MAObject: 0xdeadbeef>`, containing the object's class and pointer value.

```
    - (NSString *)description
    {
        return [NSString stringWithFormat: @"<%@: %p>", [self class], self];
    }
```

The standard for classes is to just return the class name from their own `description`, so there's a class method as well that fetches that name from the runtime and returns it:

```
    + (NSString *)description
    {
        return [NSString stringWithUTF8String: class_getName(self)];
    }
```

`doesNotRecognizeSelector:` is a lesser-known utility method. It throws an exception to make it look like the object doesn't actually respond to the given selector. This is useful for things like creating override points where subclasses have to implement a particular method:

```
    - (void)subclassesMustOverride
    {
        // pretend we don't actually implement this here
        [self doesNotRecognizeSelector: _cmd];
    }
```

The code is fairly simple. The only really tricky bit is formatting the method name. We want to display something like `-[Class method]`, but class methods need a `+` at the front, as in `+[Class classMethod]`. To figure out which context it's in, the code checks to see whether `isa` is a metaclass. If it is, then `self` is a class, and the `+` variant should be used. Otherwise, `self` is an instance, and the `-` variant is used. The rest of the code just raises the appropriate `NSException`:

```
    - (void)doesNotRecognizeSelector: (SEL)aSelector
    {
        char *methodTypeString = class_isMetaClass(isa) ? "+" : "-";
        [NSException raise: NSInvalidArgumentException format: @"%s[%@ %@]: unrecognized selector sent to instance %p", methodTypeString, [[self class] description], NSStringFromSelector(aSelector), self];
    }
```

Finally, there are a bunch of little methods that either provide obvious answers to obvious questions (e.g. the `self` method), exist to let subclasses always safely call `super` (e.g. the empty `+initialize` method), or exist as override points (e.g. the `copy` implementation that throws an exception). None of these are particularly interesting, but I include them for completeness:

```
    - (id)self
    {
        return self;
    }

    - (BOOL)isProxy
    {
        return NO;
    }

    + (void)load
    {
    }

    + (void)initialize
    {
    }

    - (id)copy
    {
        [self doesNotRecognizeSelector: _cmd];
        return nil;
    }

    - (id)mutableCopy
    {
        [self doesNotRecognizeSelector: _cmd];
        return nil;
    }

    - (id)forwardingTargetForSelector: (SEL)aSelector
    {
        return nil;
    }

    - (void)forwardInvocation: (NSInvocation *)anInvocation
    {
        [self doesNotRecognizeSelector: [anInvocation selector]];
    }

    + (BOOL)resolveClassMethod:(SEL)sel
    {
        return NO;
    }

    + (BOOL)resolveInstanceMethod:(SEL)sel
    {
        return NO;
    }
```

**Conclusion**  
`NSObject` is a big bundle of different functionality, but nothing too strange. Its main function is to handle memory allocation and management so that you can actually create objects. It also provides a bunch of handy override points for methods that every object is expected to support, and wraps a bunch of runtime functions in a nicer API.

I've skipped over a big piece of functionality provided by `NSObject`: key-value coding. This is complex enough that it deserves its own article, so I will come back to that another time.

That's it for today. Friday Q&A is driven by reader ideas, in case you somehow didn't already know, so please [send in your topic suggestions](mailto:mike@mikeash.com). Until next time, don't code anything I wouldn't code.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
