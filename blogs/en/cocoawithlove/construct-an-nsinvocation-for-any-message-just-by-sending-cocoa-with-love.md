---
title: 'Construct an NSInvocation for any message, just by sending | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/construct-nsinvocation-for-any-message.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:77c5ac28ecd1d29a'
translated: false
---

> 原文：[Construct an NSInvocation for any message, just by sending | Cocoa with Love](https://www.cocoawithlove.com/2008/03/construct-nsinvocation-for-any-message.html)　·　Cocoa with Love (Matt Gallagher)

I will show you how to use object forwarding to record any message in an NSInvocation, by simply sending the message to an object. Unlike techniques shown elsewhere, this will allow you to record any message, including NSObject messages and even the forwarding messages themselves.

## NSInvocation is painful to construct

This article appears to be the second in an ad hoc series I'm writing on Cocoa. If it is, then series title might be something like:

> Doing tricky things simply in Cocoa with one line of code

I refer you to my earlier post [Core Data: one line fetch](https://www.cocoawithlove.com/2008/03/core-data-one-line-fetch.html) where I show a single line fetch for Core Data instead of the suggested 10 line common approach.

NSInvocation has a very similar problem where the its shortest possible usage case using the default methods is 4 lines and the common case is closer to 6.

So, I'm going to reduce that to 1 (compound) line and make the code conceptually cleaner too.

## Creating an NSInvocation using the default methods

According to Apple's documentation on the page [Distributed Object Programming Topics: Using NSInvocation](http://developer.apple.com/documentation/Cocoa/Conceptual/DistrObjects/Tasks/invocations.html), to create an invocation for the MyCalendar method:

```objc
– (BOOL)updateAppointmentsForDate:(NSDate *)aDate
```

with a target and argument respectively of:

```objc
MyCalendar *userDatebook;    /* Assume this exists. */
NSDate *todaysDate;          /* Assume this exists. */
```

will require the following code:

```objc
SEL theSelector;
NSMethodSignature *aSignature;
NSInvocation *anInvocation;
 
theSelector = @selector(updateAppointmentsForDate:);
aSignature = [MyCalendar instanceMethodSignatureForSelector:theSelector];
anInvocation = [NSInvocation invocationWithMethodSignature:aSignature];
[anInvocation setSelector:theSelector];
[anInvocation setTarget:userDatebook];
[anInvocation setArgument:&todaysDate atIndex:2];
```

This isn't the largest or most cumbersome block of code but it does seem a little large for packaging a method invocation.

Obviously, you could pass just theSelector, the target userDatebook and all the arguments (in a nil terminated variable argument list) through to a constructor method. I've seen this approach used before. It tidies the code up a lot, but it makes the assumption that none of your arguments are nil. It also makes a cumbersome, unstructured, method invocation.

## Message forwarding

To spoil the ending for you, I'm going to show you a way to cut all this code down to one line. Like so:

```objc
NSInvocation *anInvocation;
[[NSInvocation invocationWithTarget:userDatebook invocationOut:&anInvocation]
    updateAppointmentsForDate:todaysDate];
```

The biggest advantage to this approach is that you are sending the updateAppointmentsForDate: message as normal, with parameters.

Now, this is not the most revolutionary concept. The designers of Cocoa use a similar, but more limited, technique in the NSUndoManager class. From Apple's [Undo Architecture: Registering Undo Operations](http://developer.apple.com/documentation/Cocoa/Conceptual/UndoArchitecture/Tasks/RegisteringUndo.html):

```objc
[[myUndoManager prepareWithInvocationTarget:drawObject]
    setFont:[drawObject font] color:[drawObject color]];
```

This is a 1 line reduction of NSInvocation creation for the message:

```objc
[drawObject setFont:[drawObject font] color:[drawObject color]]
```

The NSInvocation isn't returned to the calling function (it's held internally by NSUndoManager) but it is creating this NSInvocation for its own internal use, just by recording the unhandled message.

It relies on the Objective-C methods:

- - (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
- - (void)forwardInvocation:(NSInvocation *)anInvocation

to capture any message sent to an object which the object does not handle itself and save the parameter anInvocation.

This is a very good solution but it can't handle every situation. It only lets you capture those messages that the object does not already handle. NSUndoManager is unable to handle NSObject instance methods and any NSUndoManager instance method.

For example, NSUndoManager cannot create an NSInvocation of:

- init
- class
- release

or any other NSObject or NSUndoManager method since it already has methods for these. Even if we were to create a non-NSObject derived class, it still wouldn't be able to create an NSInvocation for:

- methodSignatureForSelector:
- forwardInvocation:

using this approach because the forwarding system can't automatically catch and forward its own methods.

## How to capture any message

The trick to capturing any message is to send the message for capture to an object which only responds to:

- - (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
- - (void)forwardInvocation:(NSInvocation *)anInvocation

and for those two methods, the object must be able to distinguish between a forwarded message (where the parameter anInvocation just needs to be saved) and a message sent directly to those methods (for which an NSInvocation must be manually constructed).

By distinguishing forwarding from invocation in those two cases, we will be able to build an NSInvocation for absolutely any valid message.

## Approach

To summarize all steps, we need:

1. A base class (one which doesn't inherit from any other class)
2. Only instance methods are:

    - - (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
    - - (void)forwardInvocation:(NSInvocation *)anInvocation

  all other work must be done through class methods.
3. An approach to distinguish a message forwarded through methodSignatureForSelector: from a direct invocation of methodSignatureForSelector:
4. An approach to distinguish a message forwarded through  forwardInvocation: from a direct invocation of  forwardInvocation:

Steps 1 and 2 are straightforward class construction. Allocating a base class is a bit unusual but not very hard.

Step 4 can be done by checking if the "target" of the anInvocation parameter is equal to the self parameter inside the method. If it is, then it's a direct invocation, otherwise it's a forwarded message.

Step 3 is trickier. The parameters passed are no different for a regular invocation to a forwarded invocation. Instead, we need to be get little dirtier. We can deliberately pass an unhandled message (which will go through the forwarding code) in a controlled situation and record the return address. By recording the known return address into the forwarding code, we can thus distinguish subsequent forwarded invocations from direct invocations. The return address can be obtained using a gcc built in function that [I've used before](https://www.cocoawithlove.com/2008/02/imp-of-current-method.html), __builtin_return_address(0).

Of course, there's no absolute guarantee that multiple paths through the forwarding code (which would result in different return addresses) won't happen. For this reason, we'll use an approach that is tolerant of mistakes. Since forwardInvocation: is always called after methodSignatureforSelector: for forwarded invocations, then we can correct false direct invocation determinations afterwards by overwriting their result.

## Solution

We have a category with the following structure:

```objc
@interface NSInvocation (ForwardedConstruction)

+ (id)invocationWithTarget:(id)target
    invocationOut:(NSInvocation **)invocationOut;
+ (id)retainedInvocationWithTarget:(id)target
    invocationOut:(NSInvocation **)invocationOut;

@end
```

Those are our entry and exit points in one. The invocationOut parameter is only set _after_ the message to be recorded is sent.

The id returned is actually an instance of the following class:

```objc
@interface InvocationProxy
{
    Class isa;
    NSInvocation **invocation;
    id target;
    BOOL retainArguments;
    NSUInteger forwardingAddress;
}

+ (id)alloc;
+ (void)setValuesForInstance:(InvocationProxy *)instance
    target:(id)target
    destinationInvocation:(NSInvocation **)destinationInvocation
    retainArguments:(BOOL)retain;
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector;
- (void)forwardInvocation:(NSInvocation *)forwardedInvocation;

@end
```

This is our special base class. It handles it own alloc. It also requires that init be sent to it after allocation (even though the class doesn't implement init) to record the return address for message forwarding.

The setValues... method configures the instance so that the next message sent to it will have its invocation recorded and store in destinationInvocation and the two instance methods  methodSignatureForSelector: and  forwardInvocation: perform the work of capturing the forwarded message as earlier described.

There's also another privately declared class in the implementation named DeallocatorHelper. This class is used because InvocationProxy doesn't have an autorelease, release or dealloc method but needs to be freed by the NSAutoreleasePool. Instead we create and autorelease the DeallocatorHelper which then deallocates the InvocationProxy in its own dealloc method. This code is all #ifdef'd out when compiled under garbage collection.

## Conclusion

Get the code here: [NSInvocationForwardedConstruction.zip](https://www.cocoawithlove.com/assets/objc-era/NSInvocationForwardedConstruction.zip) (4kb)

It will let you create an NSInvocation as follows:

```objc
NSInvocation *anInvocation;
[[NSInvocation invocationWithTarget:target invocationOut:&anInvocation]
    methodParam1:argument1
    methodParam2:argument2
    methodParam3:argument3
    methodParam4:argument4];
```

for any method with any number of and type of parameters and any valid value of arguments. Invoking retainedInvocationWithTarget:invocationOut: if you want to retain the arguments of the NSInvocation.

If want to create an NSInvocation for a selector (for example aSelector) instead of a method, with known arguments, you can invoke as follows:

```objc
NSInvocation *invocation;
id proxy = [NSInvocation invocationWithTarget:target invocationOut:&invocation];
objc_msgSend(proxy, aSelector, argument1, argument2, argument3, argument4);
```

You will need to use objc_msgSend_stret or objc_msgSend_fpret instead of objc_msgSend for methods returning structs or doubles respectively.
