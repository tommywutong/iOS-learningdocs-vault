---
title: 'Doing things in Cocoa with "nil" | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/06/doing-things-in-cocoa-with.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:09587b4ad7ac0ee3'
translated: false
---

> 原文：[Doing things in Cocoa with "nil" | Cocoa with Love](https://www.cocoawithlove.com/2008/06/doing-things-in-cocoa-with.html)　·　Cocoa with Love (Matt Gallagher)

"nil" is a pointer to nothing. Here are some useful things that you can do with that pointer to nothing in Objective-C and Cocoa.

## A quick definition of "nil"

It is possible you don't know what "nil" means in Objective-C. Just so there's no confusion let me quickly explain:

> _**nil**_ is the value an object pointer has when it isn't pointing to anything

If you're familiar with other C derived languages, you might think: "doesn't 'NULL' do the same thing?"

The answer is: almost. Where "NULL" is used for C pointers in a general sense, "nil" in Objective-C is reserved exclusively for pointers to objects. If you right-click on "nil" in XCode though, you'll find that "nil", "NULL" and "__DARWIN_NULL" are all defined to have the same value: (void *)0.

Objective-C also defines the constant "Nil" (notice the capital 'N') with the same value as "nil" for use as a class pointer instead of an object pointer. In practice though, since classes are objects, "nil" is commonly used for both.

## In the beginning, everything is zero

In Objective-C, instance variables (except isa) in a newly allocated object [will be set to zero](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSObject_Class/Reference/Reference.html). This is the same behavior as a calloc in Standard C.

This means that all of your object's pointers to other objects are already "nil". Since this is the case, you should behave accordingly. Don't redundantly initialize variables to "nil", "NULL", 0, "false" or "NO".

In fact, you should consider choosing meanings for your booleans such that false is the appropriate state on object allocation. For example "isInitialized" instead of "needsInitialization".

## You can send messages to "nil"

You can validly [send any message to a "nil" pointer](http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/Articles/chapter_2_section_3.html#//apple_ref/doc/uid/TP30001163-CH11-SW5) in Objective-C. This is very different to languages like C++ where invoking a method on a "NULL" pointer will likely crash your program.

Sending a message to "nil" will have only one effect: it will return a zero value. No other action will occur. This means that the following code:

```objc
if (myObject == nil || ![myObject isEqualTo:anotherObject])
{
    ...
}
```

can be shortened to:

```objc
if (![myObject isEqualTo:anotherObject])
{
    ...
}
```

which allows the false return value from sending a message to "nil" as one of potential code paths in the boolean expression.

Sending messages to "nil" does have some drawbacks:

- The returned zero value will only work if the size of the expected return type from the method is less or equal to the size of a pointer, or if the return type is a long long, double or struct. Support for long long, double and struct is new in Mac OS X 10.5.
- Sometimes code is clearer when you account for "nil" values as a separate case (acknowledging that you've considered and planned for it as an input case).
- If the object is not supposed to be "nil", the fact that Objective-C will quietly continue can hide the misbehaviour. You should consider this when debugging.

## NSNull

NSNull is a placeholder that Cocoa uses to represent "nil" in the Foundation collection classes (NSArray, NSSet, NSDictionary, etc) since these classes can't contain "nil" values.

You can insert NSNull into your own collections to represent "nil" values but its real use is when Cocoa inserts it for you. Consider the following:

```objc
NSArray *namesOfObjects = [arrayOfObjects valueForKey:@"name"];
```

The valueForKey: fetches the "name" of each object in the array arrayOfObjects using [key value coding](http://developer.apple.com/documentation/Cocoa/Conceptual/KeyValueCoding/KeyValueCoding.html#//apple_ref/doc/uid/10000107) and builds an NSArray of the results. If any of the "name" properties is "nil", we will get an NSNull value instead.

Some points to note about this: you must test for NSNull yourself. NSSet will not create NSNull entries when using key value coding (it simply omits them).

## Setting NSMutableDictionary values with "nil"

Since you're not allowed to add a "nil" valued object to an  NSMutableDictionary , the following:

```objc
[myMutable Dictionary setObject:nil forKey:@"key"];
```

will throw an exception.

What if you have a few objects that you want to insert into an NSMutableDictionary but you're not sure if any of them are "nil"?

You could test each one first, to see if it's "nil", like this:

```objc
NSMutableDictionary *newDictionary = [NSMutableDictionary dictionary];
id firstObject = [source getFirstObject];
if (firstObject)
{
    [newDictionary setObject:firstObject forKey:@"firstObjectKey"];
}
// ... and so on for all other objects
```

Or, assuming your keys are strings, you could take advantage of the key value coding methods on NSMutableDictionary and simply write:

```objc
NSMutableDictionary *newDictionary = [NSMutableDictionary dictionary];
[newDictionary setValue:[source getFirstObject] forKey:@"firstObjectKey"];
// ... and so on for all other objects
```

Notice the "setValue:forKey:" instead of "setObject:forKey:". The setValue:forKey: version tests the value first, to see if it's "nil". If it is, it treats the instruction as though you had called removeObjectForKey: instead — which will gracefully do nothing if the object isn't there.

Key value coding (the setValue:forKey: case) requires NSString keys, so if your NSDictionary is keyed by something other than strings, the approach shown in the second example would not be possible.

## Other zero values

"nil" is a zero valued object pointer. Cocoa conveniently provides a few other zero values for different purposes. They include:

- NSZeroPoint — an NSPoint at the origin
- NSZeroSize — a zero width and height NSSize
- NSZeroRect — a zero width and height NSRect at the origin
