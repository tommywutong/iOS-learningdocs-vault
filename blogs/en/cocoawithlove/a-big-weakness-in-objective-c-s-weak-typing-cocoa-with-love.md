---
title: 'A big weakness in Objective-C''s weak typing | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/06/big-weakness-of-objective-c-weak-typing.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:9ff630dd88d29c83'
translated: false
---

> 原文：[A big weakness in Objective-C's weak typing | Cocoa with Love](https://www.cocoawithlove.com/2011/06/big-weakness-of-objective-c-weak-typing.html)　·　Cocoa with Love (Matt Gallagher)

We generally assume that we can send any message we want to a variable in our code typed as "`id`" and Objective-C's dynamic message handling will make the invocation work correctly at runtime. In some rare cases, this assumption is wrong. I'll look at situations where you need to be careful about sending messages to "`id`" typed variables and a situation where a limitation in the Objective-C language requires a hideous workaround to avoid serious bugs.

## Introduction

We generally assume we can send any message we like to an "`id`" variable (or a `Class` variable). In fact, that's the real purpose of the "`id`" type: it is the "any" type in Objective-C to which any Objective-C message may be sent.

We use this in lots of different situations but one of the most common is sending messages to objects store in an `NSArray`:

```objc
NSString *description = [[someArray objectAtIndex:0] substringFromIndex:5];
```

In this code sample, we don't need to cast the result of the `objectAtIndex:` invocation to an `NSString` before sending it the `substringFromIndex:` message — we know that as long as the object at index 0 actually is an object that responds to the `substringFromIndex:` selector, it will work.

> or
> 
> . This post does not apply if the variable you invoke a method on is typed to anything else (even
> 
> will count as "anything else" and avoid the issues in this post).

## False assumptions

The false assumption often applied here is that the compiler doesn't need to know any type information. In reality, even though the method lookup happens at runtime, that's only enough to ensure the correct method is invoked, it is not enough to ensure the parameters will work.

The compiler definitely does need to infer _some_ information about the method signature involved. Even though the compiler does not necessarily need to know the type of the `id`, it does need to know the byte lengths of all parameters and the explicit type of any return values. This is because marshalling of the parameters (pushing and popping them from the stack) is configured at compile time.

Normally, we don't need to take any steps for this to happen though. The parameter information is obtained by looking at the name of the method you're trying to invoke, searching through the included headers for methods matching the invoked method name and then getting the parameter lengths from the first matching method it finds.

99.99% of the time, there's no problem with this: even if there's ambiguity about the exact method you're really targeting, the parameters are likely to be the same between matching method because method names in Objective-C generally imply the types of the data, so this type of conflict is likely to cause no difference in signature.

And then there's that other 0.01% of the time...

## Catastrophic failure

Imagine you have class `MyClass` with an instance method named `currentPoint` that returns an `int`. You want to get the `currentPoint` from an object stored in an array, so you use the code:

```objc
int result = [[someArray objectAtIndex:0] currentPoint];
```

When you run the code, you know the exact value returned from invoking `currentPoint` on the first object in the array should be zero (because you set it to zero and you can see in the debugger that it is still zero) but the value that ends up in the `result` is 2,147,483,647 (or some other partial garbage value).

## What has gone wrong?

The correct method is invoked at runtime. The problem is that the compiler marshalled the parameters for this invocation incorrectly leading to data corruption of the return type.

The compiler needs to push parameters onto the stack correctly before the message send and perform the message send using the correct variant of `objc_msgSend` to get the return value back afterwards. This is what has failed.

The compiler prepares parameters using the method signature (which it gets by looking at the type of the receiver and all method names that are valid for the receiver) and trying to work out which method you're likely to be invoking. Since the type of the receiver (i.e. the result from `objectAtIndex:`) is just `id` then we have no explicit type information so the compiler will look through the list of all known methods.

Unfortunately, instead of our `MyClass` method, the compiler decided to match against the `NSBezierPath` method named `currentPoint` and has prepared the parameters to match that method's signature. The `NSBezierPath` method returns an `NSPoint` which is a `struct` and handles the return parameter very differently compared to the `int` parameter our real method actually uses. This has lead to our return type getting corrupted.

> value return type here because it is the most likely to generate a bug, since a struct return type causes the compiler to generate an
> 
> for the message invocation instead of a regular
> 
> . However, it is also possible to create problems with non-return parameters of different lengths, particularly if the conflict is between floating point and non-floating point parameters or
> 
> and non-
> 
> parameters.

## Fixing the problem (most of the time)

The best way to fix the problem is to add additional type information about the receiver, so that there will only be 1 possible match for the method name.

We do this by casting the receiver:

```objc
int result = [(MyClass *)[someArray objectAtIndex:0] currentPoint];
```

A `MyClass` receiver has only one match for `currentPoint` so there is no possible conflict with the `NSBezierPath` method and the problem here is solved.

## Why is this allowed to happen? Why isn't there a compiler error?

Technically, there is a compiler warning that will alert you to this category of problem. The compiler warning "Strict Selector Matching" (a.k.a. -Wstrict-selector-match) will tell you when there is a conflict between two different method names when you're invoking a method on either of Objective-C's two weak types (`id` or `Class`).

It would be great if Strict Selector Matching always worked and we could turn it on at all times. That Apple don't turn it on by default is either because they consider the problem rare enough to ignore or it is an admission of the significant limitations of the warning as it currently behaves:

1. . Basically, there's no reason to care if there is a conflict between two methods different but totally compatible method signatures but this compiler warning will still occur.
2. due to point (1). I'm looking at you, different implementations of

  ,

  and most methods in

  versus

  . These spurious warnings may force you to carefully typecast large numbers of method calls that won't actually cause any problem.
3. . This one is a bit absurd since a

  object is regularly handled as a generic

  .
4. . If you failed to import the declaration of the correct method but you did import the declaration of a different method with a matching name but different signature, then I'm not sure the compiler

  warn you about this problem.

## A scenario where casting won't fix the problem

Imagine in the example above, the problem was between two _class_ methods, instead of two _instance_ methods.

i.e. instead of a conflict between `-[NSBezierPath currentPoint]` and `-[MyClass currentPoint]`, the conflict was between `+[NSBezierPath currentPoint]` and `+[MyClass currentPoint]`.

For the instance methods, we fixed the problem by casting to the specific object type required but when your objects are both Class, it is not possible to cast to the specific Class involved. Seriously: you cannot cast classes in Objective-C.

I consider this a serious failing of Objective-C. It makes avoiding this scenario with conflicting class method names hideous. If you're not able to change the name of the method, then the only work around looks like this:

```objc
int result = objc_msgSend([someArray objectAtIndex:0], @selector(currentPoint));
```

That's right: we would need to bypass the compiler entirely and insert the `objc_msgSend` call ourselves.

It gets worse though, since `objc_msgSend` uses a variable argument list by default, if the parameters you need to pass/receive from `objc_msgSend` are not signature compatible with a variable argument list, then you'll need to fully cast the `objc_msgSend` yourself to make certain that the parameters are passed correctly:

```objc
SomeReturnType result =
    ((SomeReturnType(*)(id, SEL, float, short, WeirdStruct))objc_msgSend)
    (
        [someArray objectAtIndex:0],
        @selector(methodWithMultipleVariables:thatAreNot:varArgCompatible:),
        someFloat,
        someShort,
        someWeirdStruct
    );
```

And if `SomeReturnType` is a struct, you'll need to use `objc_msgSend_stret` instead and for floating point types, you'll need to use `objc_msgSend_fpret`.

## Conclusion

I would like to give a blanket suggestion that you switch on "Strict Selector Matching" in your Workspace/Project/Target settings for every project but unfortunately, the limitations of this warning make that suggestion difficult.

Spurious warnings from Apple's code, every time you try to use `objectForKey:` (or a large group of other methods) on an `id` typed variable can be infuriating and pointlessly increase your workload.

The warning doesn't catch all problems because it doesn't check conflicts between methods in the `Class` and `id` spaces. Along with the spurious warnings nuisance, the argument that you could skip the warning itself (and simply keep this potential problem in mind as a potential issue) is probably valid.

The warning itself should be fixed in GCC and Clang to make it useable enough to leave on in all situations. It shouldn't give a warning when the parameters in conflicting signatures are compatible. It should also gain cross checking between `Class` and `id` when the type in the code is `id`.

And Objective-C really needs a way to declare a type that is a specific `Class`. Even syntax as ugly as @classtype(SomeClass) would do it but I'm sure something more graceful could be found.

I've seen people argue that if you ever require a specific `Class` then you're designing things badly. I think the bugs caused by method name conflicts are a situation where you may not (if you can't rename either method) be able to cleanly design your way around this serious problem without the ability to cast a Class to something more specific.

In addition to allowing a conflict between two `Class` methods to be resolved more gracefully it would also help in the unrelated situation where a method wants a `Class` object passed as a parameter but that `Class` must be a subclass of a specific class.
