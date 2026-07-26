---
title: 'Assign, retain, copy: pitfalls in Obj-C property accessors | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/06/assign-retain-copy-pitfalls-in-obj-c.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:f9e7e2f8c212bc57'
translated: false
---

> 原文：[Assign, retain, copy: pitfalls in Obj-C property accessors | Cocoa with Love](https://www.cocoawithlove.com/2010/06/assign-retain-copy-pitfalls-in-obj-c.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I'll look at some very subtle problems that can occur if a getter or setter method chooses the wrong memory management pattern and in the process, explain why NSDictionary copies its keys rather than simply retains them.

> : in this post I'll be discussing basic memory and mutability considerations in Objective-C accessor methods. If you're interested in atomicity and thread safety issues in accessor methods, please read my earlier post on
> 
> Memory and thread-safe custom property methods
> 
> . This post will only look at non-atomic accessors.

## Why implement your own accessors?

If you know about Objective-C's properties, you may already be asking, "Why implement your own accessors at all?". For simple accessors, you can (and probably should) use the synthesized `@property` accessors and not worry about the implementation. The reason for this post is that you will often need to implement accessor methods yourself to attach additional behaviors to the get or set action, so you always need to know how the accessor should work.

## The one you already know: the assign pattern

Since you're reading this blog, it's probably safe to assume that you already know how a basic assign accessor looks:

```objc
- (SomeVariable)someValue
{
    return someValue;
}
```

and a setter method looks like this:

```objc
- (void)setSomeValue:(SomeVariable)aSomeVariableValue
{
    someValue = aSomeVariableValue;
}
```

For most non-object data, that's all you need. This is the implementation you'd get with a non-atomic `assign` synthesized `@property`.

## Retain: first opportunities for failure

If you're working with retain/released objects in Objective-C, your object will become invalid if your setter does not retain it, so the setter must handle this.

The most completely thorough, all purpose way of handling `retain` and `release` issues in a setter looks like this:

```objc
- (void)setSomeInstance:(SomeClass *)aSomeInstanceValue
{
    if (someInstance == aSomeInstanceValue)
    {
        return;
    }
    SomeClass *oldValue = someInstance;
    someInstance = [aSomeInstanceValue retain];
    [oldValue release];
}
```

This is obviously much more complicated than a simple assignment.

The biggest point that stands out i the weird `retain`/`release` dance occupying the last three lines of this code block. We do this to avoid problems where the object pointed to by `aSomeInstanceValue` and `someInstance` is the same. Imagine the following:

```objc
- (void)setSomeInstance:(SomeClass *)aSomeInstanceValue
{
    [someInstance release]; // <-- original value is released
    someInstance = [aSomeInstanceValue retain];
}
```

If `aSomeInstanceValue` and `someInstance` are the same object, then the first line could release the underlying object before the second line retains it — meaning that the object is destroyed and invalid by the time it is retained again.

You'll notice that we use the C equality operator to compare the two objects instead of the `isEqual:` method. Normally, this is a bad idea (Objective-C objects may be "equal" even if they do not point to the same location in memory) but in this case, we are specifically interested in cases where the memory location (and hence the retain counts) are identical. The comparison is not strictly necessary to prevent premature release (since the `retain` precedes the `release`) but it's an optimization and safety measure.

In reality though, all this is a bit painful to write: the comparison, the annoying temporary value and the careful ordering of everything. In practice, we normally use a shorter version of the setter method that is basically just as good and is certainly far easier to write:

```objc
- (void)setSomeInstance:(SomeClass *)aSomeInstanceValue
{
    [someInstance autorelease];
    someInstance = [aSomeInstanceValue retain];
}
```

In this case, we don't care about the comparison optimisation and we use the autorelease pool to temporarily hold the original value instead of our own stack value.

This method has the same safety as the `retain`/`release` dance but requires an autorelease pool and is marginally slower if someInstance and aSomeInstanceValue are actually the same. In reality, there's almost always an autorelease pool in a Cocoa application and the performance difference is more theoretical than real (you'd have difficulty constructing a test program to ever show a difference) until you start creating copy setters (see below).

> : There are some situations where a setter method that takes an Objective-C object should
> 
> retain its parameter. Specifically: objects in a hierarchy should not normally retain their parents. Look at
> 
> Rules to avoid retain cycles
> 
> for more on this topic.

## The other half of the retain access pattern

In reality, even if you forget to perform the `if (newInstance == oldInstance) return;` check in your accessor method, you are highly unlikely to see a problem even if you actually do pass the current value to a setter method.

The reason why you are normally safe, even if you make a mistake, is because the parameter you pass into a method normally has another retain count held elsewhere.

Specifically: most objects you access on the stack have an autoreleased retain count held by an autorelease pool on the stack or a longer lived object somewhere in the heap.

Theoretically, you could help this idea along by implementing your getter methods like this for retained objects:

```objc
- (SomeClass *)someInstance
{
    return [[someInstance retain] autorelease];
}
```

This will ensure that if your object is used like this:

```objc
SomeClass *stackInstance = [anObject someInstance];
[anObject release]; // anObject releases its someInstance ivar in its dealloc method
[stackInstance doSomething];
```

Then the `stackInstance` variable will still be valid when `doSomething` is invoked on it.

Generally though, I don't bother doing this in non-atomic getter methods.

Why not? Speed, redundancy and common sense.

While retaining and autoreleasing something is not a gigantic overhead, it is normally just not needed for a get accessor method. The programmer using the get accessor should understand that the lifetime is bound to the source object.

However, you may want to use this pattern in a situation where it is not immediately clear that the value returned is a getter method. For example:

```objc
@implementation ThisClassIsReallyJustAString

- (NSString *)description
{
    return [[internalValue retain] autorelease];
}

@end
```

The `description` method (which returns an `NSString` representation of an object) does not normally return an instance variable directly so it would not ordinarily be considered an accessor method. In this situation, it is implemented as an accessor but due to the expectation that the description is a generated value, we need to retain and autorelease the returned value.

Any instance variable returned from a method where the method is not obviously an accessor method should always go through a `retain`/`autorelease` since it is not immediately obvious that its lifetime would be bound to the lifetime of the source object.

## Copy accessors

The reason why `retain` accessors exist is obvious — you don't want the value to be deallocated while it is set on the object.

The reason for the final accessor pattern in Objective-C — copy accessors — is less broadly understood but nonetheless relevant.

You should use a copy accessor when the setter parameter may be mutable but you can't have the internal state of a property changing without warning. Consider the following example:

```objc
NSMutableString *mutableString = [NSMutableString stringWithString:@"initial value"];
[someObject setStringValue:mutableString];
[mutableString setString:@"different value"];
```

In this situation, if the `setStringValue:` method followed the `retain` pattern, then the `setString:` method invoked on the next line would change the internal value of this property without warning `someObject`.

Sometimes, you don't care if the internal state of a property change without warning. However, if you do care about the internal state of a property changing, then you'll want to use a `copy` setter.

The implementation of a non-atomic copy setter is as simple as you'd imagine:

```objc
- (void)setStringValue:(NSString *)aString
{
    if (stringValue == aString)
    {
        return;
    }
    NSString *oldValue = stringValue;
    stringValue = [aString copy];
    [oldValue release];
}
```

> : I had previously stated that you don't need the equality comparison for a copy (since I wrongly claimed the
> 
> would ensure you always have a different block of memory). I was wrong, of course. As was immediately pointed out in the comments:
> 
> does not always return a copy; for immutable objects,
> 
> can return the
> 
> object. I forgot about this, even though I've certainly written copy setters that work this way (see the
> 
> SynthesizeSingleton code
> 
> ). The result is that we still need the comparison to ensure that setting the property to the same value doesn't cause the same potential release problems that the previous retain pattern had. Did I mention it is possible to screw up property accessors?

This finally explains why `NSDictionary` copies its keys.

`NSDictionary` stores all its value objects in locations according to the result of each corresponding key object's `hash` method.

If a key object were to change in such a way that the `hash` method result changed, then the `NSDictionary` would not be able to find the corresponding value object any more.

Key objects are not set by a property accessor on an `NSDictionary` but the effect is the same: the copy pattern is used to ensure that outside objects cannot change the internal state of the dictionary without warning.

Of course, the downside to properties that follow the copy pattern is speed. It's not normally an issue for objects up to a few kilobytes but beyond that point, you'll need to consider whether copy is the right pattern for the resources involved.

## Conclusion

Getter and setter methods are frequently given as the simplest kind of method to implement. But you can see that even within this very simple kind of method, there are subtle ways that they can go wrong.

Overall, this post is a much simpler level than my typical posts but that doesn't mean its only for novice Objective-C developers. Experienced programmers are far from immune to mistakes in this area. Some of the potential quirks with getter and setter methods are so rare you may never see a problem (even if your code is doing things in an unsafe manner) so learning from experience can take time in this area.

Of course, if you don't need any customization in your accessor methods, you should simply use a synthesized `@property` implementation. This will avoid any possibility of introducing mistakes.
