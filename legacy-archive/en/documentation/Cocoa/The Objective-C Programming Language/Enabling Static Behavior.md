---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocStaticBehavior.html
archived_at: '2026-07-15T07:17:31.919742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Next](Selectors.md)[Previous](Fast%20Enumeration.md)

# Enabling Static Behavior

This chapter explains how static typing works and discusses some other features of Objective-C, including ways to temporarily overcome its inherent dynamism.

By design, Objective-C objects are dynamic entities. As many decisions about them as possible are pushed from compile time to runtime:

- The memory for objects is _dynamically allocated_ at runtime by class methods that create new instances.
- Objects are _dynamically typed_. In source code (at compile time), any object variable can be of type `id` no matter what the object’s class is. The exact class of an `id` variable (and therefore its particular methods and data structure) isn’t determined until the program runs.
- Messages and methods are _dynamically bound_, as described in [Dynamic Binding](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmmrwga). A runtime procedure matches the method selector in the message to a method implementation that “belongs to” the receiver.

These features give object-oriented programs a great deal of flexibility and power, but there’s a price to pay. In particular, the compiler can’t check the exact types (classes) of `id` variables. To permit better compile-time type checking, and to make code more self-documenting, Objective-C allows objects to be statically typed with a class name rather than generically typed as `id`. Objective-C also lets you turn off some of its object-oriented features in order to shift operations from runtime back to compile time.

If a pointer to a class name is used in place of `id` in an object declaration such as

```
Rectangle *thisObject;
```

the compiler restricts the value of the declared variable to be either an instance of the class named in the declaration or an instance of a class that inherits from the named class. In the example above, `thisObject` can be only a `Rectangle` object of some kind.

Statically typed objects have the same internal data structures as objects declared to be of type `id`. The type doesn’t affect the object; it affects only the amount of information given to the compiler about the object and the amount of information available to those reading the source code.

Static typing also doesn’t affect how the object is treated at runtime. Statically typed objects are dynamically allocated by the same class methods that create instances of type `id`. If `Square` is a subclass of `Rectangle`, the following code would still produce an object with all the instance variables of a `Square` object, not just those of a `Rectangle` object:

```
Rectangle *thisObject = [[Square alloc] init];
```

Messages sent to statically typed objects are dynamically bound, just as messages to objects typed `id` are. The exact type of a statically typed receiver is still determined at runtime as part of the messaging process. A `display` message sent to the `thisObject` object:

```
[thisObject display];
```

performs the version of the method defined in the `Square` class, not the one in its `Rectangle` superclass.

By giving the compiler more information about an object, static typing opens up possibilities that are absent for objects typed `id`:

- In certain situations, it allows for compile-time type checking.
- It can free objects from the restriction that identically named methods must have identical return and parameter types.
- It permits you to use the structure pointer operator to directly access an object’s instance variables.

The first two possibilities are discussed in the sections that follow. The third is covered in [Defining a Class](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfvjvomi).

With the additional information provided by static typing, the compiler can deliver better type-checking services in two situations:

- When a message is sent to a statically typed receiver, the compiler can make sure the receiver can respond. A warning is issued if the receiver doesn’t have access to the method named in the message.
- When a statically typed object is assigned to a statically typed variable, the compiler makes sure the types are compatible. A warning is issued if they’re not.

An assignment can be made without warning, provided the class of the object being assigned is identical to, or inherits from, the class of the variable receiving the assignment. The following example illustrates this:

```
Shape     *aShape;
Rectangle *aRect;

aRect = [[Rectangle alloc] init];
aShape = aRect;
```

Here `aRect` can be assigned to `aShape` because a rectangle is a kind of shape—the `Rectangle` class inherits from `Shape`. However, if the roles of the two variables are reversed and `aShape` is assigned to `aRect`, the compiler generates a warning; not every shape is a rectangle. (For reference, see [Figure 1-2](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmnjqge), which shows the class hierarchy including `Shape` and `Rectangle`.)

There’s no check when the expression on either side of the assignment operator is of type `id`. A statically typed object can be freely assigned to an `id` object, or an `id` object to a statically typed object. Because methods like `alloc` and `init` return objects of type `id`, the compiler doesn’t ensure that a compatible object is returned to a statically typed variable. The following code is error-prone, but is allowed nonetheless:

```
Rectangle *aRect;
aRect = [[Shape alloc] init];
```


In general, methods in different classes that have the same selector (the same name) must also share the same return and parameter types. This constraint is imposed by the compiler to allow dynamic binding. Because the class of a message receiver (and therefore class-specific details about the method it’s asked to perform), can’t be known at compile time, the compiler must treat all methods with the same name alike. When it prepares information on method return and parameter types for the runtime system, it creates just one method description for each method selector.

However, when a message is sent to a statically typed object, the class of the receiver is known by the compiler. The compiler has access to class-specific information about the methods. Therefore, the message is freed from the restrictions on its return and parameter types.

An instance can be statically typed to its own class or to any class that it inherits from. All instances, for example, can be statically typed as `NSObject`.

However, the compiler understands the class of a statically typed object only from the class name in the type designation, and it does its type checking accordingly. Typing an instance to an inherited class can therefore result in discrepancies between what the compiler thinks would happen at runtime and what actually happens.

For example, if you statically type a `Rectangle` instance as `Shape` as shown here:

```
Shape *myRectangle = [[Rectangle alloc] init];
```

the compiler treats it as a `Shape` instance. If you send the object a message to perform a `Rectangle` method,

```
BOOL solid = [myRectangle isFilled];
```

the compiler complains. The `isFilled` method is defined in the `Rectangle` class, not in `Shape`.

However, if you send it a message to perform a method that the `Shape` class knows about such as

```
[myRectangle display];
```

the compiler doesn’t complain, even though `Rectangle` overrides the method. At runtime, the `Rectangle` version of the method is performed.

Similarly, suppose that the `Upper` class declares a `worry` method that returns a `double` as shown here:

```objc
- (double)worry;
```

and the `Middle` subclass of `Upper` overrides the method and declares a new return type:

```objc
- (int)worry;
```

If an instance is statically typed to the `Upper` class, the compiler thinks that its `worry` method returns a `double`, and if an instance is typed to the `Middle` class, the compiler thinks that `worry` returns an `int`. Errors result if a `Middle` instance is typed to the `Upper` class: The compiler informs the runtime system that a `worry` message sent to the object returns a `double`, but at runtime it actually returns an `int` and generates an error.

Static typing can free identically named methods from the restriction that they must have identical return and parameter types, but it can do so reliably only if the methods are declared in different branches of the class hierarchy.

[Next](Selectors.md)[Previous](Fast%20Enumeration.md)

