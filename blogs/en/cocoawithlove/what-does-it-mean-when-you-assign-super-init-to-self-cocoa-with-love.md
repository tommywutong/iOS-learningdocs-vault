---
title: 'What does it mean when you assign [super init] to self? | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/04/what-does-it-mean-when-you-assign-super.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:60f2313a4c234b76'
translated: false
---

> 原文：[What does it mean when you assign [super init] to self? | Cocoa with Love](https://www.cocoawithlove.com/2009/04/what-does-it-mean-when-you-assign-super.html)　·　Cocoa with Love (Matt Gallagher)

One of the strangest pieces of common syntax in Objective-C is the line `self = [super init];`. Without any explanation, this arrangement raises a few questions. Does this line set the `self` value for the instance? Is `self` just a variable like any other? If so, why have it at all? I'll address each of these questions and show how the compiler converts uses of `self` and method invocations.

## Converting a method invocation

The first step to understanding the `self` parameter is to look at how the compiler converts a standard method invocation.

When you type the following:

```objc
MyClass *myObject = [[MyClass alloc] initWithString:@"someString"];
```

The compiler converts this into function calls that look like this:

```objc
class myClass = objc_getClass("MyClass");
SEL allocSelector = @selector(alloc);
MyClass *myObject1 = objc_msgSend(myClass, allocSelector);

SEL initSelector = @selector(initWithString:);
MyClass *myObject2 = objc_msgSend(myObject1, initSelector, @"someString");
```

The compiler has slightly more efficient means of getting the `class` and `SEL` values but if you look at assembly code, you will see `objc_msgSend` calls for every method invocation.

## So what is "self"?

Every method that you declare has two hidden parameters: `self` and `_cmd`.

The following method:

```objc
- (id)initWithString:(NSString *)aString;
```

is converted by the compiler to the following function call:

```objc
id initWithString(id self, SEL _cmd, NSString *aString);
```

The reality is that `self` is simply a hidden parameter on every method. Like any other parameter, it receives its value from the function invocation.

Yes, `_cmd` is also a hidden parameter on every method that you can access if you choose. In reality, there are few uses for the `_cmd` parameter except in [obscure cases](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html).

You can experiment with this by eliminating `objc_msgSend` and invoking the function for a method directly. Instead of calling:

```objc
[myObject someMethodWithParameter:someValue];
```

You can reach your method implementation directly by recreating the work done by `objc_msgSend`.

```objc
SEL methodSelector = @selector(someMethodWithParameter:);
IMP someMethodFunction = class_getMethodImplementation([myObject class], methodSelector);
someMethodFunction(myObject, methodSelector, someValue);
```

The only reason why `self` has a value on the inside of the `someMethodWithParameter:` implementation is because the pointer `myObject` is passed as the first parameter into `someMethodFunction`. If you pass a different value as this first parameter, then `self` will have a different value on the inside of the method.

If you pass a value of a different class, you have a good chance of crashing the program. The following section explains why.

## Why have a "self" parameter at all?

A method needs to know what data to act upon. The `self` parameter tells the class the data to act upon and so is essential to object oriented programming.

This statement may seem a little strange, since you can easily implement a method without using the `self` parameter by name. The reality is that the compiler uses the `self` parameter to resolve any reference to an instance variable inside a method.

If you had a class defined like this:

```objc
@interface MyClass : NSObject
{
    NSInteger value;
}
- (void)setValueToZero;
@end
```

then the method:

```objc
- (void)setValueToZero
{
    value = 0;
}
```

is converted by the compiler into:

```objc
void setValueToZero(id self, SEL _cmd)
{
    self->value = 0;
}
```

So `self` is essential for accessing any instance variables, even if you never literally type "`self`".

## So does self already have a value when init is called?

If you remember back at the start, I said that the `initWithString:` part of a typical `[[MyClass alloc] initWithString:@"someString"]` invocation is converted into an `objc_msgSend` call:

```objc
MyClass *myObject2 = objc_msgSend(myObject1, initSelector, @"someString");
```

So by the time we get to the inside of the method, `self` already has a value; its value is `myObject1` (i.e. the allocated object, as returned from the `[MyClass alloc]` call. This is essential because without it, the `super` invocation wouldn't be possible — the `self` value is used by the compiler to send the invocation:

```objc
[super init];
```

becomes:

```objc
objc_msgSendSuper(self, @selector(init));
```

Yes, `self` already has a value when your initializer starts. In fact, it is almost guaranteed to be the correct, final value.

## So why assign the value returned from [super init] to self?

Looking at a typical initializer method:

```objc
- (id)initWithString:(NSString *)aString
{
    self = [super init];
    if (self)
    {
        instanceString = [aString retain];
    }
    return self;
}
```

Why do we assign `[super init]` to self here?

The textbook reason is because `[super init]` is permitted to do one of three things:

1. Return its own receiver (the `self` pointer doesn't change) with inherited instance values initialized.
2. Return a different object with inherited instance values initialized.
3. Return `nil`, indicating failure.

In the first case, the assignment has no effect on `self` and the `instanceString` is set on in the original object (the line `instanceString = [aString retain];` could have been the first line of the method and the result would be the same).

In the third case, the initialization has failed. `self` is set to `nil`, no further action is taken and `nil` is returned.

The rationale for assigning to `self` is associated with the second case: if the returned object is different, we want the:

```objc
        instanceString = [aString retain];
```

which gets converted to

```objc
        self->instanceString = [aString retain];
```

to act on the correct value, so we have to change the value of `self` to point to this new object.

## It's almost never required to initialize self

So the rationale for assigning to `self` is that the `[super init]` could return a different object and should initialize that different object instead of the old (likely invalid) object.

The question to consider is then: when would `[super init]` return a different object?

The answer is that it will return different objects in one of the following situations:

- Singleton object (always returns the singleton instead of any subsequent allocation)
- Other unique objects (`[NSNumber numberWithInteger:0]` always returns the global "zero" object)
- Class clusters substitute private subclasses when you initialize an instance of the superclass.
- Classes which choose to reallocate the same (or compatible) class based on parameters passed into the initializer.

In all but the final case, continuing to initialize the returned object if it changes is a mistake — the returned object is already completely initialized and isn't necessary related to your class anymore.

So the list of three things that `[super init]` is permitted to return can now be expanded to four by splitting the "Return a different object" point into two:

1. Return its own receiver (the `self` pointer doesn't change) with inherited instance values initialized.
2. Return an object of the same class, requiring further initialization.
3. Return a different object that is already completely initialized.
4. Return `nil`, indicating failure.

In this list, we now have two cases (2 and 3) which are incompatible. The typical "assign `[super init]` to `self`" initializer handles cases 1, 2 and 4.

An `init` approach to handle cases 1, 3 and 4 would actually be:

```objc
- (id)initWithString:(NSString *)aString
{
    id result = [super init];
    if (self == result)
    {
        instanceString = [aString retain];
    }
    return result;
}
```

So class clusters, singletons and unique objects all use case 3, putting dozens of Cocoa classes in this category. I'm only aware of `NSManagedObject` that uses case 2. Curiously then, while case 3 is overwhelmingly more common, initializers that support 1, 2 and 4 but are incompatible with case 3 have become the standard.

## Conclusion

> _Update_: I have rewritten this conclusion to reflect the fact that I'm not actually suggesting you should stop using "assign `[super init]` to `self`" initializers. Thank you to everyone who invented creative ways to tell me I was wrong about this implication.

You don't _need_ to assign `[super init]` to `self` to make most classes work. In some obscure cases, it is actually the wrong thing to do.

So why do we continue to assign to `self`? It's the traditional template for an initializer, and although it's wrong in some cases, it is right in other cases which have been written to expect this approach.

Further to this is the consideration that class clusters and other classes likely to return unrelated or different, fully initialized objects from their init methods are not supposed to be subclassed in a normal way — making code which favors them less relevant.

The number of cases where `super` returns an unrelated object are so small that they can easily be dealt with on a case-by-case basis — a class will normally make it very clear when its initializers might return something other than the receiver or `nil`.
