---
title: Object Oriented Programming and the Objective-C Programming Language 1.0
apple_id: TP40005191
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOPandObjC1/Articles/ocRuntimeSystem.html
archived_at: '2026-07-15T07:17:25.028774Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object Oriented Programming and the Objective-C Programming Language 1.0](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)


[Next](Language%20Summary.md)[Previous](The%20Language.md)

# The Runtime System

The Objective-C language defers as many decisions as it can from compile time and link time to runtime. Whenever possible, it does things dynamically. This means that the language requires not just a compiler, but also a runtime system to execute the compiled code. The runtime system acts as a kind of operating system for the Objective-C language; it’s what makes the language work.

The following sections look in particular at three areas where the `NSObject` class provides a framework and defines conventions:

- Allocating and initializing new instances of a class, and deallocating instances when they’re no longer needed
- Forwarding messages to another object
- Dynamically loading new modules into a running program

Additional conventions of the `NSObject` class are described in the `NSObject` class specification in the Foundation framework reference.

Other sections look at how you interact with the runtime at an abstract level; how you can use the Distributed Objects system for sending messages between objects in different address spaces; and how the compiler encodes the return and argument types for each method.

Objective-C programs interact with the runtime system at three distinct levels:

1. Through Objective-C source code.

   For the most part, the runtime system works automatically and behind the scenes. You use it just by writing and compiling Objective-C source code.

   When you compile code containing Objective-C classes and methods, the compiler creates the data structures and function calls that implement the dynamic characteristics of the language. The data structures capture information found in class and category definitions and in protocol declarations; they include the class and protocol objects discussed in [Extending Classes](The%20Language.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznhe2tenzw), as well as method selectors, instance variable templates, and other information distilled from source code. The principal runtime function is the one that sends messages, as described in [How Messaging Works](The%20Language.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznha4dqnbw). It’s invoked by source-code message expressions.
2. Through the methods defined in the `NSObject` class of the Foundation framework.

   Most objects in Cocoa are subclasses of the `NSObject` class, so most objects inherit the methods it defines. (The notable exception is the `NSProxy` class; see [Forwarding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojnha3tamrs) for more information.)

   Some of the `NSObject` methods simply query the runtime system for information. These methods allow objects to perform introspection. Examples of such methods are the `class` method, which asks an object to identify its class; `isKindOfClass:` and `isMemberOfClass:`, which test an object’s position in the inheritance hierarchy; `respondsToSelector:`, which indicates whether an object can accept a particular message; `conformsToProtocol:`, which indicates whether an object claims to implement the methods defined in a specific protocol; and `methodForSelector:`, which provides the address of a method’s implementation. Methods like these give an object the ability to introspect about itself.

   All these methods were mentioned in previous chapters and are described in detail in the `NSObject` class specification in the Foundation framework reference.
3. Through direct calls to runtime functions.

   The runtime system is a dynamic shared library with a public interface consisting of a set of functions and data structures in the header files located within the directory `/usr/include/objc`. Many of these functions allow you to use plain C to replicate what the compiler does when you write Objective-C code. Others form the basis for functionality exported through the methods of the `NSObject` class. These functions make it possible to develop other interfaces to the runtime system and produce tools that augment the development environment; they’re not needed when programming in Objective-C. However, a few of the runtime functions might on occasion be useful when writing an Objective-C program. All of these functions are documented in _[Objective-C 2.0 Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_.

Because the `NSObject` class is at the root of the inheritance hierarchy of the Foundation framework, the methods it defines are usually inherited by all classes. Its methods therefore establish behaviors that are inherent to every instance and every class object. However, in a few cases, the `NSObject` class merely defines a template for how something should be done; it doesn’t provide all the necessary code itself.

For example, the `NSObject` class defines a `description` instance method that returns a string describing the contents of the class. This is primarily used for debugging—the GDB `print-object` command prints the string returned from this method. `NSObject`’s implementation of this method doesn’t know what the class contains, so it returns a string with the name and address of the object. Subclasses of `NSObject` can implement this method to return more details. For example, the Foundation class `NSArray` returns a list of descriptions of the objects it contains.

This section describes how to allocate, initialize, and deallocate objects, and the fundamentals of the methods you use for memory management in Cocoa. This section does not provide a complete description of memory management—or more accurately, object ownership—in Cocoa; this subject is discussed in _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ which you should consider as required reading.

It takes two steps to create an object using Objective-C. You must:

- Dynamically allocate memory for the new object
- Initialize the newly allocated memory to appropriate values

An object isn’t fully functional until both steps have been completed. Each step is accomplished by a separate method but typically in a single line of code:

```
id anObject = [[Rectangle alloc] init];
```

Separating allocation from initialization gives you individual control over each step so that each can be modified independently of the other. The following sections look first at allocation and then at initialization, and discuss how they are controlled and modified.

In Objective-C, memory for new objects is allocated using class methods defined in the `NSObject` class. `NSObject` defines two principal methods for this purpose, `alloc` and `allocWithZone:`.

```objc
+ (id)alloc;
+ (id)allocWithZone:(NSZone *)zone;
```

These methods allocate enough memory to hold all the instance variables for an object belonging to the receiving class. They don’t need to be overridden and modified in subclasses.

The `alloc` and `allocWithZone:` methods initialize a newly allocated object’s `isa` instance variable so that it points to the object’s class (the class object). All other instance variables are set to `0`. Usually, an object needs to be more specifically initialized before it can be safely used.

This initialization is the responsibility of class-specific instance methods that, by convention, begin with the abbreviation “init”. If the method takes no arguments, the method name is just those four letters, `init`. If it takes arguments, labels for the arguments follow the “init” prefix. For example, an `NSView` object can be initialized with an `initWithFrame:` method.

Every class that declares instance variables must provide an `init...` method to initialize them. The `NSObject` class declares the `isa` variable and defines an `init` method. However, since `isa` is initialized when memory for an object is allocated, all `NSObject`’s `init` method does is return `self`. `NSObject` declares the method mainly to establish the naming convention described earlier.

An `init...` method normally initializes the instance variables of the receiver, then returns it. It’s the responsibility of the method to return an object that can be used without error.

However, in some cases, this responsibility can mean returning a different object than the receiver. For example, if a class keeps a list of named objects, it might provide an `initWithName:` method to initialize new instances. If there can be no more than one object per name, `initWithName:` might refuse to assign the same name to two objects. When asked to assign a new instance a name that’s already being used by another object, it might free the newly allocated instance and return the other object—thus ensuring the uniqueness of the name while at the same time providing what was asked for, an instance with the requested name.

In a few cases, it might be impossible for an `init...` method to do what it’s asked to do. For example, an `initFromFile:` method might get the data it needs from a file passed as an argument. If the file name it’s passed doesn’t correspond to an actual file, it won’t be able to complete the initialization. In such a case, the `init...` method could free the receiver and return `nil`, indicating that the requested object can’t be created.

Because an `init...` method might return an object other than the newly allocated receiver, or even return `nil`, it’s important that programs use the value returned by the initialization method, not just that returned by `alloc` or `allocWithZone:`. The following code is very dangerous, since it ignores the return of `init`.

```
id anObject = [SomeClass alloc];
[anObject init];
[anObject someOtherMessage];
```

Instead, to safely initialize an object, you should combine allocation and initialization messages in one line of code.

```
id anObject = [[SomeClass alloc] init];
[anObject someOtherMessage];
```

If there’s a chance that the `init...` method might return `nil`, then you should check the return value before proceeding:

```
id anObject = [[SomeClass alloc] init];
if ( anObject )
    [anObject someOtherMessage];
else
    ...
```


An `init...` method must ensure that all of an object’s instance variables have reasonable values. This doesn’t mean that it needs to provide an argument for each variable. It can set some to default values or depend on the fact that (except for `isa`) all bits of memory allocated for a new object are set to `0`. For example, if a class requires its instances to have a name and a data source, it might provide an `initWithName:fromFile:` method, but set nonessential instance variables to arbitrary values or allow them to have the null values set by default. It could then rely on methods like `setEnabled:`, `setFriend:`, and `setDimensions:` to modify default values after the initialization phase had been completed.

Any `init...` method that takes arguments must be prepared to handle cases where an inappropriate value is passed.

Every class that declares instance variables must provide an `init...` method to initialize them (unless the variables require no initialization). The `init...` methods the class defines initialize only those variables declared in the class. Inherited instance variables are initialized by sending a message to `super` to perform an initialization method defined somewhere farther up the inheritance hierarchy:

```
- initWithName:(char *)string
{
    if ( self = [super init] ) {
        name = (char *)NSZoneMalloc([self zone],
            strlen(string) + 1);
        strcpy(name, string);
    }
    return self;
}
```

The message to `super` chains together initialization methods in all inherited classes. Because it comes first, it ensures that superclass variables are initialized before those declared in subclasses. For example, a Rectangle object must be initialized as an `NSObject`, a Graphic, and a Shape before it’s initialized as a Rectangle.

The connection between the `initWithName:` method illustrated above and the inherited `init` method it incorporates is illustrated in Figure 2-1:

__Figure 2-1__  Incorporating an Inherited Initialization Method

!

A class must also make sure that all inherited initialization methods work. For example, if class A defines an `init` method and its subclass B defines an `initWithName:` method, as shown in Figure 2-1, B must also make sure that an `init` message successfully initializes B instances. The easiest way to do that is to replace the inherited `init` method with a version that invokes `initWithName:`:

```
- init
{
    return [self initWithName:"default"];
}
```

The `initWithName:` method would, in turn, invoke the inherited method, as shown earlier. Figure 2-2 includes B’s version of `init`:

__Figure 2-2__  Covering an Inherited Initialization Model

!

Covering inherited initialization methods makes the class you define more portable to other applications. If you leave an inherited method uncovered, someone else may use it to produce incorrectly initialized instances of your class.

In the example above, `initWithName:` would be the _designated initializer_ for its class (class B). The designated initializer is the method in each class that guarantees inherited instance variables are initialized (by sending a message to `super` to perform an inherited method). It’s also the method that does most of the work, and the one that other initialization methods in the same class invoke. It’s a Cocoa convention that the designated initializer is always the method that allows the most freedom to determine the character of a new instance (usually this is the one with the most arguments, but not always).

It’s important to know the designated initializer when defining a subclass. For example, suppose we define class C, a subclass of B, and implement an `initWithName:fromFile:` method. In addition to this method, we have to make sure that the inherited `init` and `initWithName:` methods also work for instances of C. This can be done just by covering B’s `initWithName:` with a version that invokes `initWithName:fromFile:`.

```
- initWithName:(char *)string
{
    return [self initWithName:string fromFile:NULL];
}
```

For an instance of the C class, the inherited `init` method invokes this new version of `initWithName:` which invokes `initWithName:fromFile:`. The relationship between these methods is shown in Figure 2-3:

__Figure 2-3__  Covering the Designated Initializer

!

This figure omits an important detail. The `initWithName:fromFile:` method, being the designated initializer for the C class, sends a message to `super` to invoke an inherited initialization method. But which of B’s methods should it invoke, `init` or `initWithName:`? It can’t invoke `init`, for two reasons:

- Circularity would result (`init` invokes C’s `initWithName:`, which invokes `initWithName:fromFile:`, which invokes `init` again).
- It won’t be able to take advantage of the initialization code in B’s version of `initWithName:`.

Therefore, `initWithName:fromFile:` must invoke `initWithName:`:

```
- initWithName:(char *)string fromFile:(char *)pathname
{
    if ( self = [super initWithName:string] )
        ...
}
```

Designated initializers are chained to each other through messages to `super`, while other initialization methods are chained to designated initializers through messages to `self`.

Figure 2-4 shows how all the initialization methods in classes A, B, and C are linked. Messages to `self` are shown on the left and messages to `super` are shown on the right.

__Figure 2-4__  Initialization Chain

!

Note that B’s version of `init` sends a message to `self` to invoke the `initWithName:` method. Therefore, when the receiver is an instance of the B class, it invokes B’s version of `initWithName:`, and when the receiver is an instance of the C class, it invokes C’s version.

In Cocoa, some classes define creation methods that combine the two steps of allocating and initializing to return new, initialized instances of the class. These methods typically take the form `+` _className..._ where _className_ is the name of the class. For instance, `NSString` has the following methods (among others):

```objc
+ (NSString *)stringWithCString:(const char *)bytes;
+ (NSString *)stringWithFormat:(NSString *)format, ...;
```

Similarly, `NSArray` defines the following class methods that combine allocation and initialization:

```objc
+ (id)array;
+ (id)arrayWithObject:(id)anObject;
+ (id)arrayWithObjects:(id)firstObj, ...;
```

Instances created with any of these methods are deallocated automatically (as described in [Marking Objects for Later Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydomztgq)), so you don’t have to release them unless you have retained them (as described in [Retaining Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydonruga)). Usually there are equivalent `-init...` methods provided along with these conveniences.

Methods that combine allocation and initialization are particularly valuable if the allocation must somehow be informed by the initialization. For example, if the data for the initialization is taken from a file, and the file might contain enough data to initialize more than one object, it would be impossible to know how many objects to allocate until the file is opened. In this case, you might implement a `listFromFile:` method that takes the name of the file as an argument. It would open the file, see how many objects to allocate, and create a List object large enough to hold all the new objects. It would then allocate and initialize the objects from data in the file, put them in the List, and finally return the List.

It also makes sense to combine allocation and initialization in a single method if you want to avoid the step of blindly allocating memory for a new object that you might not use. As mentioned in [The Returned Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydkojvgi), an `init...` method might sometimes substitute another object for the receiver. For example, when `initWithName:` is passed a name that’s already taken, it might free the receiver and in its place return the object that was previously assigned the name. This means, of course, that an object is allocated and freed immediately without ever being used.

If the code that determines whether the receiver should be initialized is placed inside the method that does the allocation instead of inside `init...`, you can avoid the step of allocating a new instance when one isn’t needed.

In the following example, the `soloist` method ensures that there’s no more than one instance of the Soloist class. It allocates and initializes an instance only once:

```
+ soloist
{
    static Soloist *instance = nil;

    if ( instance == nil )
    {
        instance = [[self alloc] init];
    }
    return instance;
}
```


In an Objective-C program, objects are constantly creating and disposing of other objects. Much of the time an object creates things for private use and can dispose of them as it needs. However, when an object passes something to another object through a method invocation, the lines of ownership—and responsibility for disposal—blur. Object ownership and memory management are discussed in greater detail in _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_; the following three sections describe the mechanism of memory management in Cocoa, but not the policy. _You must read_ _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ _to fully understand the issues._

Cocoa uses a memory-management technique called _reference counting_ (also known as _refcounting_), in which each entity that claims ownership of an object increments the object’s reference count and decrements the reference count when finished with the object. When the reference count reaches zero, the object is deallocated (as will be explained in [Deallocation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydmojyga)). This technique allows one instance of an object to be safely shared among several other objects.

If you _create_ a _new_ object, you own it (note that there are precise definitions for what create means here—again see _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_). The new object has a refcount of 1. It is your responsibility to relinquish ownership of the object when you have finished with it. You can do this by sending it a `release` message, which decrements the refcount by 1.

```
[anObject release];
```


When you write a method that creates and returns a new object, that method is responsible for releasing the object. However, it’s clearly not fruitful to dispose of an object before the recipient of the object gets it. What is needed is a way to mark an object for release at a later time, so that it’s properly disposed of after the recipient has had a chance to use it. Cocoa provides just such a mechanism.

```
[anObject autorelease];
```

The `autorelease` method, defined by `NSObject`, marks the receiver for later release. By autoreleasing an object—that is, by sending it an `autorelease` message—you cause the autoreleased object to be sent a `release` message at some stage in the future by the current _autorelease pool_ The mechanism by which the release message is sent and the timing of the release message are discussed in greater detail in [Autorelease Pools](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html#//apple_ref/doc/uid/20000047).

There are times when you don’t want a received object to be disposed of; for example, you may need to cache the object in an instance variable. In this case, only you know when the object is no longer needed, so you need the power to ensure that the object is not disposed of while you are still using it.

```
[anObject retain];
```

You do this with the `retain` method, which stays the effect of a pending `autorelease` (or preempts a later `release` or `autorelease` message; see [Deallocation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydmojyga) for details on the `autorelease` message). By retaining an object you ensure that it isn’t deallocated until you’re done with it:

The `NSObject` class defines a `dealloc` method that relinquishes the memory originally allocated for an object. You must never invoke `dealloc` directly; you should instead invoke either the `release` method or the `autorelease` method to decrement the method’s refcount. When the object’s refcount reaches zero, the `release` method invokes `dealloc`. In some situations, you don’t release an object at all.

The purpose of a `dealloc` message is to deallocate all the memory occupied by the receiver. `NSObject`’s version of the method deallocates the receiver’s instance variables, but doesn’t follow any variable that points to other memory. If the receiver allocated any additional memory—to store a character string or an array of structures, for example—that memory must also be deallocated (unless it’s shared by other objects). If the receiver had claimed ownership of any other objects, it must also relinquish ownership.

Every class that has its objects allocate additional memory or claim ownership of other objects (typically using object instance variables) must have its own `dealloc` method. Each version of `dealloc` ends with a message to `super` to perform an inherited version of the method, as illustrated in the following example:

```
- dealloc {
    [ownedObject release];
    free(privateMemory);
    vm_deallocate(task_self(), sharedMemory, memorySize);
    [super dealloc];
}
```

By working its way up the inheritance hierarchy, every `dealloc` message eventually invokes `NSObject`’s version of the method.

Sending a message to an object that does not handle that message is an error. However, before announcing the error, the runtime system gives the receiving object a second chance to handle the message. It sends the object a `forwardInvocation:` message with an `NSInvocation` object as its sole argument—the `NSInvocation` object encapsulates the original message and the arguments that were passed with it.

You can implement a `forwardInvocation:` method to give a default response to the message, or to avoid the error in some other way. As its name implies, `forwardInvocation:` is commonly used to forward the message to another object.

To see the scope and intent of forwarding, imagine the following scenarios: Suppose, first, that you’re designing an object that can respond to a message called `negotiate`, and you want its response to include the response of another kind of object. You could accomplish this easily by passing a `negotiate` message to the other object somewhere in the body of the `negotiate` method you implement.

Take this a step further, and suppose that you want your object’s response to a `negotiate` message to be exactly the response implemented in another class. One way to accomplish this would be to make your class inherit the method from the other class. However, it might not be possible to arrange things this way. There may be good reasons why your class and the class that implements `negotiate` are in different branches of the inheritance hierarchy.

Even if your class can’t inherit the `negotiate` method, you can still “borrow” it by implementing a version of the method that simply passes the message on to an instance of the other class:

```
- negotiate
{
    if ( [someOtherObject respondsTo:@selector(negotiate)] )
        return [someOtherObject negotiate];
    return self;
}
```

This way of doing things could get a little cumbersome, especially if there were a number of messages you wanted your object to pass on to the other object. You’d have to implement one method to cover each method you wanted to borrow from the other class. Moreover, it would be impossible to handle cases where you didn’t know, at the time you wrote the code, the full set of messages you might want to forward. That set might depend on events at runtime, and it might change as new methods and classes are implemented in the future.

The second chance offered by a `forwardInvocation:` message provides a less ad hoc solution to this problem, and one that’s dynamic rather than static. It works like this: When an object can’t respond to a message because it doesn’t have a method matching the selector in the message, the runtime system informs the object by sending it a `forwardInvocation:` message. Every object inherits a `forwardInvocation:` method from the `NSObject` class. However, `NSObject`’s version of the method simply invokes `doesNotRecognizeSelector:`. By overriding `NSObject`’s version and implementing your own, you can take advantage of the opportunity that the `forwardInvocation:` message provides to forward messages to other objects.

To forward a message, all a `forwardInvocation:` method needs to do is:

- Determine where the message should go, and
- Send it there with its original arguments.

The message can be sent with the `invokeWithTarget:` method:

```objc
- (void)forwardInvocation:(NSInvocation *)anInvocation
{
    if ([someOtherObject respondsToSelector:
            [anInvocation selector]])
        [anInvocation invokeWithTarget:someOtherObject];
    else
        [super forwardInvocation:anInvocation];
}
```

The return value of the message that’s forwarded is returned to the original sender. All types of return values can be delivered to the sender, including `id`s, structures, and double-precision floating-point numbers.

A `forwardInvocation:` method can act as a distribution center for unrecognized messages, parceling them out to different receivers. Or it can be a transfer station, sending all messages to the same destination. It can translate one message into another, or simply “swallow” some messages so there’s no response and no error. A `forwardInvocation:` method can also consolidate several messages into a single response. What `forwardInvocation:` does is up to the implementor. However, the opportunity it provides for linking objects in a forwarding chain opens up possibilities for program design.

For more information on forwarding and invocations, see the `NSInvocation` class specification in the Foundation framework reference.

Forwarding mimics inheritance, and can be used to lend some of the effects of multiple inheritance to Objective-C programs. As shown in [Figure 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojnha3tgmjx), an object that responds to a message by forwarding it appears to borrow or “inherit” a method implementation defined in another class.

__Figure 2-5__  Forwarding

!

In this illustration, an instance of the Warrior class forwards a `negotiate` message to an instance of the Diplomat class. The Warrior will appear to negotiate like a Diplomat. It will seem to respond to the `negotiate` message, and for all practical purposes it does respond (although it’s really a Diplomat that’s doing the work).

The object that forwards a message thus “inherits” methods from two branches of the inheritance hierarchy—its own branch and that of the object that responds to the message. In the example above, it appears as if the Warrior class inherits from Diplomat as well as its own superclass.

Forwarding addresses most needs that lead programmers to value multiple inheritance. However, there’s an important difference between the two: Multiple inheritance combines different capabilities in a single object. It tends toward large, multifaceted objects. Forwarding, on the other hand, assigns separate responsibilities to disparate objects. It decomposes problems into smaller objects, but associates those objects in a way that’s transparent to the message sender.

Forwarding not only mimics multiple inheritance, it also makes it possible to develop lightweight objects that represent or “cover” more substantial objects. The surrogate stands in for the other object and funnels messages to it.

The proxy discussed in [Remote Messaging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydgnrug4) is such a surrogate. A proxy takes care of the administrative details of forwarding messages to a remote receiver, making sure argument values are copied and retrieved across the connection, and so on. But it doesn’t attempt to do much else; it doesn’t duplicate the functionality of the remote object but simply gives the remote object a local address, a place where it can receive messages in another application.

Other kinds of surrogate objects are also possible. Suppose, for example, that you have an object that manipulates a lot of data—perhaps it creates a complicated image or reads the contents of a file on disk. Setting this object up could be time-consuming, so you prefer to do it lazily—when it’s really needed or when system resources are temporarily idle. At the same time, you need at least a placeholder for this object in order for the other objects in the application to function properly.

In this circumstance, you could initially create, not the full-fledged object, but a lightweight surrogate for it. This object could do some things on its own, such as answer questions about the data, but mostly it would just hold a place for the larger object and, when the time came, forward messages to it. When the surrogate’s `forwardInvocation:` method first receives a message destined for the other object, it would ensure that the object existed and would create it if it didn’t. All messages for the larger object go through the surrogate, so, as far as the rest of the program is concerned, the surrogate and the larger object would be the same.

Although forwarding mimics inheritance, the `NSObject` class never confuses the two. Methods like `respondsToSelector:` and `isKindOfClass:` look only at the inheritance hierarchy, never at the forwarding chain. If, for example, a Warrior object is asked whether it responds to a `negotiate` message,

```
if ( [aWarrior respondsToSelector:@selector(negotiate)] )
    ...
```

the answer is `NO`, even though it can receive `negotiate` messages without error and respond to them, in a sense, by forwarding them to a Diplomat. (See [Figure 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojnha3tgmjx).)

In many cases, `NO` is the right answer. But it may not be. If you use forwarding to set up a surrogate object or to extend the capabilities of a class, the forwarding mechanism should probably be as transparent as inheritance. If you want your objects to act as if they truly inherited the behavior of the objects they forward messages to, you’ll need to re-implement the `respondsToSelector:` and `isKindOfClass:` methods to include your forwarding algorithm:

```objc
- (BOOL)respondsToSelector:(SEL)aSelector
{
    if ( [super respondsToSelector:aSelector] )
        return YES;
    else {
        /* Here, test whether the aSelector message can     *
         * be forwarded to another object and whether that  *
         * object can respond to it. Return YES if it can.  */
    }
    return NO;
}
```

In addition to `respondsToSelector:` and `isKindOfClass:`, the `instancesRespondToSelector:` method should also mirror the forwarding algorithm. If protocols are used, the `conformsToProtocol:` method should likewise be added to the list. Similarly, if an object forwards any remote messages it receives, it should have a version of `methodSignatureForSelector:` that can return accurate descriptions of the methods that ultimately respond to the forwarded messages.

You might consider putting the forwarding algorithm somewhere in private code and have all these methods, `forwardInvocation:` included, call it.

The methods mentioned in this section are described in the `NSObject` class specification in the Foundation framework reference. For information on `invokeWithTarget:`, see the [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation) class specification in the Foundation framework reference.

An Objective-C program can load and link new classes and categories while it’s running. The new code is incorporated into the program and treated identically to classes and categories loaded at the start.

Dynamic loading can be used to do a lot of different things. For example, the various modules in the System Preferences application are dynamically loaded.

In the Cocoa environment, dynamic loading is commonly used to allow applications to be customized. Others can write modules that your program loads at runtime—much as Interface Builder loads custom palettes and the Mac OS X System Preferences application loads custom preference modules. The loadable modules extend what your application can do. They contribute to it in ways that you permit but could not have anticipated or defined yourself. You provide the framework, but others provide the code.

Although there is a runtime function that performs dynamic loading of Objective-C modules in Mach-O files (`objc_loadModules`, defined in `objc/objc-load.h`), Cocoa’s `NSBundle` class provides a significantly more convenient interface for dynamic loading—one that’s object-oriented and integrated with related services. See the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) class specification in the Foundation framework reference for information on the `NSBundle` class and its use. See _Mac OS X ABI Mach-O File Format Reference_ for information on Mach-O files.

Like most other programming languages, Objective-C was initially designed for programs that are executed as a single process in a single address space.

Nevertheless, the object-oriented model, where communication takes place between relatively self-contained units through messages that are resolved at runtime, would seem well suited for interprocess communication as well. It’s not hard to imagine Objective-C messages between objects that reside in different address spaces (that is, in different tasks) or in different threads of execution of the same task.

For example, in a typical server-client interaction, the client task might send its requests to a designated object in the server, and the server might target specific client objects for the notifications and other information it sends.

Or imagine an interactive application that needs to do a good deal of computation to carry out a user command. It could simply display a dialog telling the user to wait while it was busy, or it could isolate the processing work in a subordinate task, leaving the main part of the application free to accept user input. Objects in the two tasks would communicate through Objective-C messages.

Similarly, several separate processes could cooperate on the editing of a single document. There could be a different editing tool for each type of data in the document. One task might be in charge of presenting a unified onscreen user interface and of sorting out which user instructions are the responsibility of the various editing tools. Each cooperating task could be written in Objective-C, with Objective-C messages being the vehicle of communication between the user interface and the tools and between one tool and another.

Remote messaging in Objective-C requires a runtime system that can establish connections between objects in different address spaces, recognize when a message is intended for an object in a remote address space, and transfer data from one address space to another. It must also mediate between the separate schedules of the two tasks; it has to hold messages until their remote receivers are free to respond to them.

Cocoa includes a _distributed objects_ architecture that is essentially this kind of extension to the runtime system. Using distributed objects, you can send Objective-C messages to objects in other tasks or have messages executed in other threads of the same task. (When remote messages are sent between two threads of the same task, the threads are treated exactly like threads in different tasks.) Note that Cocoa’s distributed objects system is built on top of the runtime system; it doesn’t alter the fundamental behavior of your Cocoa objects.

To send a remote message, an application must first establish a connection with the remote receiver. Establishing the connection gives the application a proxy for the remote object in its own address space. It then communicates with the remote object through the proxy. The proxy assumes the identity of the remote object; it has no identity of its own. The application is able to regard the proxy as if it were the remote object; for most purposes, it is the remote object.

Remote messaging is illustrated in [Figure 2-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojngeydgnzrg4), where object A communicates with object B through a proxy, and messages for B wait in a queue until B is ready to respond to them:

__Figure 2-6__  Remote Messages

!

The sender and receiver are in different tasks and are scheduled independently of each other. So there’s no guarantee that the receiver is free to accept a message when the sender is ready to send it. Therefore, arriving messages are placed in a queue and retrieved at the convenience of the receiving application.

A proxy doesn’t act on behalf of the remote object or need access to its class. It isn’t a copy of the object, but a lightweight substitute for it. In a sense, it’s transparent; it simply passes the messages it receives on to the remote receiver and manages the interprocess communication. Its main function is to provide a local address for an object that wouldn’t otherwise have one. A proxy isn’t fully transparent, however. For instance, a proxy doesn’t allow you to directly set and get an object’s instance variables.

A remote receiver is typically anonymous. Its class is hidden inside the remote application. The sending application doesn’t need to know how that application is designed or what classes it uses. It doesn’t need to use the same classes itself. All it needs to know is what messages the remote object responds to.

Because of this, an object that’s designated to receive remote messages advertises its interface in a formal protocol. Both the sending and the receiving application declare the protocol—they both import the same protocol declaration. The receiving application declares it because the remote object must conform to the protocol. The sending application declares it to inform the compiler about the messages it sends and because it may use the `conformsToProtocol:` method and the `@protocol()` directive to test the remote receiver. The sending application doesn’t have to implement any of the methods in the protocol; it declares the protocol only because it initiates messages to the remote receiver.

The distributed objects architecture, including the [NSProxy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProxy/Description.html#//apple_ref/occ/cl/NSProxy) and [NSConnection](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConnection/Description.html#//apple_ref/occ/cl/NSConnection) classes, is documented in the Foundation framework reference and _[Distributed Objects Programming Topics](../Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_.

Remote messaging raises not only a number of intriguing possibilities for program design, it also raises some interesting issues for the Objective-C language. Most of the issues are related to the efficiency of remote messaging and the degree of separation that the two tasks should maintain while they’re communicating with each other.

So that programmers can give explicit instructions about the intent of a remote message, Objective-C defines six type qualifiers that can be used when declaring methods inside a formal protocol:

- `oneway`
- `in`
- `out`
- `inout`
- `bycopy`
- `byref`

These modifiers are restricted to formal protocols; they can’t be used inside class and category declarations. However, if a class or category adopts a protocol, its implementation of the protocol methods can use the same modifiers that are used to declare the methods.

The following sections explain how these modifiers are used.

Consider first a method with just a simple return value:

```objc
- (BOOL)canDance;
```

When a `canDance` message is sent to a receiver in the same application, the method is invoked and the return value provided directly to the sender. But when the receiver is in a remote application, two underlying messages are required—one message to get the remote object to invoke the method, and the other message to send back the result of the remote calculation. This is illustrated in the figure below:

__Figure 2-7__  Round-Trip Message

!

Most remote messages are, at bottom, two-way (or “round trip”) remote procedure calls (RPCs) like this one. The sending application waits for the receiving application to invoke the method, complete its processing, and send back an indication that it has finished, along with any return information requested. Waiting for the receiver to finish, even if no information is returned, has the advantage of coordinating the two communicating applications, of keeping them both “in sync.” For this reason, round-trip messages are often called _synchronous_. Synchronous messages are the default.

However, it’s not always necessary or a good idea to wait for a reply. Sometimes it’s sufficient simply to dispatch the remote message and return, allowing the receiver to get to the task when it can. In the meantime, the sender can go on to other things. Objective-C provides a return type modifier, `oneway`, to indicate that a method is used only for _asynchronous_ messages:

```objc
- (oneway void)waltzAtWill;
```

Although `oneway` is a type qualifier (like `const`) and can be used in combination with a specific type name, such as `oneway float` or `oneway id`, the only such combination that makes any sense is `oneway void`. An asynchronous message can’t have a valid return value.

Next, consider methods that take pointer arguments. A pointer can be used to pass information to the receiver by reference. When invoked, the method looks at what’s stored in the address it’s passed.

```
- setTune:(struct tune *)aSong
{
    tune = *aSong;
    ...
}
```

The same sort of argument can also be used to return information by reference. The method uses the pointer to find where it should place information requested in the message.

```
- getTune:(struct tune *)theSong
{
    ...
    *theSong = tune;
}
```

The way the pointer is used makes a difference in how the remote message is carried out. In neither case can the pointer simply be passed to the remote object unchanged; it points to a memory location in the sender’s address space and would not be meaningful in the address space of the remote receiver. The runtime system for remote messaging must make some adjustments behind the scenes.

If the argument is used to pass information by reference, the runtime system must dereference the pointer, ship the value it points to over to the remote application, store the value in an address local to that application, and pass that address to the remote receiver.

If, on the other hand, the pointer is used to return information by reference, the value it points to doesn’t have to be sent to the other application. Instead, a value from the other application must be sent back and written into the location indicated by the pointer.

In the first case, information is passed on the first leg of the round trip. In the second case, information is returned on the second leg of the round trip. Because these cases result in very different actions on the part of the runtime system for remote messaging, Objective-C provides type modifiers that can clarify the programmer’s intention:

- The type modifier`in` indicates that information is being passed in a message:

```
- setTune:(in struct tune *)aSong;
```
- The modifier `out` indicates that an argument is being used to return information by reference:

```
- getTune:(out struct tune *)theSong;
```
- A third modifier, `inout`, indicates that an argument is used both to provide information and to get information back:

```
- adjustTune:(inout struct tune *)aSong;
```

The Cocoa distributed objects system takes `inout` to be the default modifier for all pointer arguments except those declared `const`, for which `in` is the default. `inout` is the safest assumption but also the most time-consuming since it requires passing information in both directions. The only modifier that makes sense for arguments passed by value (non-pointers) is `in`. While `in` can be used with any kind of argument, `out` and `inout` make sense only for pointers.

In C, pointers are sometimes used to represent composite values. For example, a string is represented as a character pointer (`char *`). Although in notation and implementation there’s a level of indirection here, in concept there’s not. Conceptually, a string is an entity in and of itself, not a pointer to something else.

In cases like this, the distributed objects system automatically dereferences the pointer and passes whatever it points to as if by value. Therefore, the `out` and `inout` modifiers make no sense with simple character pointers. It takes an additional level of indirection in a remote message to pass or return a string by reference:

```
- getTuneTitle:(out char **)theTitle;
```

The same is true of objects:

```
- adjustRectangle:(inout Rectangle **)theRect;
```

These conventions are enforced at runtime, not by the compiler.

Finally, consider a method that takes an object as an argument:

```
- danceWith:(id)aPartner;
```

A `danceWith:` message passes an object `id` to the receiver. If the sender and the receiver are in the same application, they would both be able to refer to the same _aPartner_ object.

This is true even if the receiver is in a remote application, except that the receiver needs to refer to the object through a proxy (since the object isn’t in its address space). The pointer that `danceWith:` delivers to a remote receiver is actually a pointer to the proxy. Messages sent to the proxy would be passed across the connection to the real object and any return information would be passed back to the remote application.

There are times when proxies may be unnecessarily inefficient, when it’s better to send a copy of the object to the remote process so that it can interact with it directly in its own address space. To give programmers a way to indicate that this is intended, Objective-C provides a `bycopy` type modifier:

```
- danceWith:(bycopy id)aClone;
```

`bycopy` can also be used for return values:

```objc
- (bycopy)dancer;
```

It can similarly be used with `out` to indicate that an object returned by reference should be copied rather than delivered in the form of a proxy:

```
- getDancer:(bycopy out id *)theDancer;
```

`bycopy` makes so much sense for certain classes—classes that are intended to contain a collection of other objects, for instance—that often these classes are written so that a copy is sent to a remote receiver, instead of the usual reference. You can override this behavior with `byref`, however, thereby specifying that objects passed to a method or objects returned from a method should be passed or returned by reference. Since passing by reference is the default behavior for the vast majority of Objective-C objects, you will rarely, if ever, make use of the `byref` keyword.

The only type that it makes sense for `bycopy` or `byref` to modify is an object, whether dynamically typed `id` or statically typed by a class name.

Although `bycopy` and `byref` can’t be used inside class and category declarations, they can be used within formal protocols. For instance, you could write a formal protocol `foo` as follows:

```objc
@Protocol foo
- (bycopy)array;
@end
```

A class or category can then adopt your protocol `foo`. This allows you to construct protocols so that they provide “hints” as to how objects should be passed and returned by the methods described by the protocol.

To assist the runtime system, the compiler encodes the return and argument types for each method in a character string and associates the string with the method selector. The coding scheme it uses is also useful in other contexts and so is made publicly available with the `@encode()` compiler directive. When given a type specification, `@encode()` returns a string encoding that type. The type can be a basic type such as an `int`, a pointer, a tagged structure or union, or a class name—anything, in fact, that can be used as an argument to the C `sizeof()` operator.

```
char *buf1 = @encode(int **);
char *buf2 = @encode(struct key);
char *buf3 = @encode(Rectangle);
```

The table below lists the type codes. Note that many of them overlap with the codes you use when encoding an object for purposes of archiving or distribution. However, there are codes listed here that you can’t use when writing a coder, and there are codes that you may want to use when writing a coder that aren’t generated by `@encode()`. (See the [NSCoder](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/cl/NSCoder) class specification in the Foundation Framework reference for more information on encoding objects for archiving or distribution.)

__Table 2-1__  Objective-C type encodings

| Code | Meaning |
| `c` | A `char` |
| `i` | An `int` |
| `s` | A `short` |
| `l` | A `long` |
| `q` | A `long long` |
| `C` | An `unsigned char` |
| `I` | An `unsigned int` |
| `S` | An `unsigned short` |
| `L` | An `unsigned long` |
| `Q` | An `unsigned long long` |
| `f` | A `float` |
| `d` | A `double` |
| `B` | A C++ `bool` or a C99 `_Bool` |
| `v` | A `void` |
| `*` | A character string (`char *`) |
| `@` | An object (whether statically typed or typed `id`) |
| `#` | A class object (`Class`) |
| `:` | A method selector (`SEL`) |
| [_array type_] | An array |
| {_name=type..._} | A structure |
| (_name_=_type..._) | A union |
| `b`num | A bit field of _num_ bits |
| `^`type | A pointer to _type_ |
| `?` | An unknown type (among other things, this code is used for function pointers) |

The type code for an array is enclosed within square brackets; the number of elements in the array is specified immediately after the open bracket, before the array type. For example, an array of 12 pointers to `float`s would be encoded as:

```
[12^f]
```

Structures are specified within braces, and unions within parentheses. The structure tag is listed first, followed by an equal sign and the codes for the fields of the structure listed in sequence. For example, the structure

```
typedef struct example {
    id   anObject;
    char *aString;
    int  anInt;
} Example;
```

would be encoded like this:

```
{example=@*i}
```

The same encoding results whether the defined type name (`Example`) or the structure tag (`example`) is passed to `@encode()`. The encoding for a structure pointer carries the same amount of information about the structure’s fields:

```
^{example=@*i}
```

However, another level of indirection removes the internal type specification:

```
^^{example}
```

Objects are treated like structures. For example, passing the `NSObject` class name to `@encode()` yields this encoding:

```
{NSObject=#}
```

The `NSObject` class declares just one instance variable, `isa`, of type Class.

Note that although the `@encode()` directive doesn’t return them, the runtime system uses the additional encodings listed in Table 2-2 for type qualifiers when they’re used to declare methods in a protocol.

__Table 2-2__  Objective-C method encodings

| Code | Meaning |
| `r` | `const` |
| `n` | `in` |
| `N` | `inout` |
| `o` | `out` |
| `O` | `bycopy` |
| `R` | `byref` |
| `V` | `oneway` |

[Next](Language%20Summary.md)[Previous](The%20Language.md)

