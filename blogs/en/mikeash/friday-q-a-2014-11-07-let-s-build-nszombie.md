---
title: 'Friday Q&A 2014-11-07: Let''s Build NSZombie'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-11-07-lets-build-nszombie.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7532230f3d59c519'
translated: false
---

> 原文：[Friday Q&A 2014-11-07: Let's Build NSZombie](https://www.mikeash.com/pyblog/friday-qa-2014-11-07-lets-build-nszombie.html)　·　mikeash.com Friday Q&A

Posted at 2014-11-07 16:04 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-01-23: Let's Build Swift Notifications](https://www.mikeash.com/pyblog/friday-qa-2015-01-23-lets-build-swift-notifications.html)  
Previous article: [A Brief Pause](https://www.mikeash.com/pyblog/a-brief-pause.html)  
Tags: [braaaiiiinnnssss](https://www.mikeash.com/pyblog/?tag=braaaiiiinnnssss) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [zombie](https://www.mikeash.com/pyblog/?tag=zombie)

Friday Q&A 2014-11-07: Let's Build NSZombie

by [Mike Ash](https://www.mikeash.com/)

**Review**  
Zombies detect memory management errors. Specifically, they detect the scenario where an Objective-C object is deallocated and then a message is sent using a pointer to where that object used to be. This is a specific case of the general "use after free" error.

In normal operation, this results in a message being sent to memory that may have been overwritten or returned to the kernel. This results in a crash if the memory has been returned to the kernel, and can result in a crash if the memory has been overwritten. In the case where the memory was overwritten with a new Objective-C object, then the message is sent to that new object which is probably completely unrelated to the original one, which can cause exceptions thrown due to unrecognized selectors or can even cause bizarre misbehaviors if the message is one the object actually responds to.

It's also possible that the memory hasn't been touched and still contains the original object, in a post-`dealloc` state. This can lead to other interesting and bizarre failures. For example, if the object contains a UNIX file handle, it may call `close` on a file descriptor twice, which can end up closing a file descriptor owned by some other part of the program, causing a failure far away from the bug.

ARC has greatly reduced the frequency of these errors, but it hasn't eliminated them altogether. These problems can still occur due to problems with multithreading, interactions with non-ARC code, mismatched method declarations, or type system abuse that strips or changes ARC storage modifiers.

Zombies hook into object deallocation. Instead of freeing the underlying memory as the last step in object deallocation, zombies change the object to a new zombie class which intercepts all messages sent to it. Any message sent to a zombie object results in a diagnostic error message instead of the bizarre behavior you get in normal operation. There is also a mode where it rewrites the class and then frees the memory anyway, but this is typically much less useful since the memory will typically get reused quickly, and I'll ignore that option here.

To write our own zombies implementation, we need to hook object deallocation and build the appropriate zombie classes. Let's get started!

**Catching All Messages**  
If we make a root class without any methods, then any message sent to an instance of that class will go into the runtime's forwarding machinery. This would seem to make `forwardInvocation:` a natural point to catch messages. However, that one happens a bit too late. Before `forwardInvocation:` can run, the runtime needs a method signature to construct an `NSInvocation` object, and that means that `methodSignatureForSelector:` runs first. This, then, is the override point for catching messages sent to a zombie object.

**Dynamically Allocated Classes**  
In addition to the selector that was sent, zombies also remember the original class of the object. However, there may not be any room in the object's memory to store a reference to that original class. If the original class had no additional instance variables, then there's no space that can be repurposed for storage. The original class must therefore be stored in the zombie class rather than in the zombie object, and that means the zombie class needs to be dynamically allocated. Each class which has an instance that becomes a zombie will get its own zombie class.

The next question is where to store the reference to the original class. It's possible to allocate a class with some extra storage for things like this, but it's somewhat inconvenient to use. An easier way is to simply use the class name. Since Objective-C classes all live in one big namespace, the class name is sufficient to uniquely identify it within a process. By sticking a prefix on the original class name to generate the zombie class name, we end up with something that's both descriptive on its own and can be used to recover the original class name. We'll use `MAZombie_` as the prefix.

**Method Implementations**  
Note that all of the code here is built without ARC, since ARC memory management calls really get in the way here.

Let's start off with a simple method implementation, which is an empty one:

```
    void EmptyIMP(id obj, SEL _cmd) {}
```

It turns out that the Objective-C runtime assumes that every class implements `+initialize`. This is sent to a class before the first message sent to the class to allow it to do any setup it needs. If it's not implemented, the runtime sends it anyway and hits the forwarding machinery instead, which isn't helpful here. Adding an empty implementation of `+initialize` avoids that problem. `EmptyIMP` will be used as the implementation of `+initialize` on zombie classes.

The implementation of `-methodSignatureForSelector:` is a bit more interesting:

```
    NSMethodSignature *ZombieMethodSignatureForSelector(id obj, SEL _cmd, SEL selector) {
```

It retrieves the class of the object and that class's name. This is the name of the zombie class:

```
        Class class = object_getClass(obj);
        NSString *className = NSStringFromClass(class);
```

The original class name can be retrieved by stripping off the prefix:

```
        className = [className substringFromIndex: [@"MAZombie_" length]];
```

Then it logs the error and calls `abort()` to make sure you're paying attention:

```
        NSLog(@"Selector %@ sent to deallocated instance %p of class %@", NSStringFromSelector(selector), obj, className);
        abort();
    }
```

**Creating the Classes**  
The `ZombifyClass` function takes a normal class and returns a zombie class, creating it if necessary:

```
    Class ZombifyClass(Class class) {
```

The zombie class name is useful both for checking to see if a zombie class exists and for creating it if it doesn't:

```
        NSString *className = NSStringFromClass(class);
        NSString *zombieClassName = [@"MAZombie_" stringByAppendingString: className];
```

The existence of the zombie class can be checked using `NSClassFromString`. This also provides the zombie class so it can be returned immediately if it exists:

```
        Class zombieClass = NSClassFromString(zombieClassName);
        if(zombieClass) return zombieClass;
```

Note that there's a race condition here: if two instances of the same class are zombified from two threads simultaneously, they'll both try to create the zombie class. In real code, you'd need to wrap this whole chunk of code in a lock to ensure that doesn't happen.

A call to the `objc_allocateClassPair` function allocates the zombie class:

```
        zombieClass = objc_allocateClassPair(nil, [zombieClassName UTF8String], 0);
```

We add the implementation of `-methodSignatureForSelector:` using the `class_addMethod` function. The signature of `"@@::"` means that it returns an object, and takes three parameters: an object (`self`), a selector (`_cmd`), and another selector (the explicit selector parameter):

```
        class_addMethod(zombieClass, @selector(methodSignatureForSelector:), (IMP)ZombieMethodSignatureForSelector, "@@::");
```

The empty method is also added as the implementation of `+initialize`. There's no separate function for adding class methods. Instead, we add a method to the class's class, which is the metaclass:

```
        class_addMethod(object_getClass(zombieClass), @selector(initialize), (IMP)EmptyIMP, "v@:");
```

Now that the class is set up, it can be registered with the runtime and returned:

```
        objc_registerClassPair(zombieClass);

        return zombieClass;
    }
```

**Zombifying Objects**  
In order to turn objects into zombies, we'll replace the implementation of `NSObject`'s `dealloc` method. Subclasses' `dealloc` methods will still run, but once they go up the chain to `NSObject`, the zombie code will run. This will prevent the object from being destroyed, and provides a place to set the object's class to the zombie class. This operation gets wrapped up into a function to enable zombies:

```
    void EnableZombies(void) {
        Method m = class_getInstanceMethod([NSObject class], @selector(dealloc));
        method_setImplementation(m, (IMP)ZombieDealloc);
    }
```

We can then put a call to `EnableZombies` at the top of `main()` or similar, and the rest takes care of itself. The implementation of `ZombieDealloc` is straightforward. It calls `ZombifyClass` to obtain the zombie class for the object being deallocated, then uses `object_setClass` to change the class of the object to the zombie class:

```
    void ZombieDealloc(id obj, SEL _cmd) {
        Class c = ZombifyClass(object_getClass(obj));
        object_setClass(obj, c);
    }
```

**Testing**  
Let's make sure it works:

```
    obj = [[NSIndexSet alloc] init];
    [obj release];
    [obj count];
```

I chose `NSIndexSet` semi-arbitrarily, as a convenient class that doesn't hit CoreFoundation bridging weirdness. Running this code with zombies enabled produces:

```
    a.out[5796:527741] Selector count sent to deallocated instance 0x100111240 of class NSIndexSet
```

Success!

**Conclusion**  
Zombies are fairly simple to implement in the end. By dynamically allocating classes, we can easily keep track of the original class without needing to rely on storage within the zombie object. `methodSignatureForSelector:` provides a convenient choke point for intercepting messages sent to the zombie object. A quick hook on `-[NSObject dealloc]` lets us turn objects into zombies instead of destroying them when their retain count goes to zero.

That's it for today. Come back next time for more frightening tales. Until then, keep [sending in your suggestions for topics](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-11-07-lets-build-nszombie.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
