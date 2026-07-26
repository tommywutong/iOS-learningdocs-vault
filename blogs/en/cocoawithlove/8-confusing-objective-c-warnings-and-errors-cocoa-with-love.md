---
title: '8 Confusing Objective-C Warnings and Errors | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/04/8-confusing-objective-c-warnings-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:d8ee76d486e249d7'
translated: false
---

> 原文：[8 Confusing Objective-C Warnings and Errors | Cocoa with Love](https://www.cocoawithlove.com/2009/04/8-confusing-objective-c-warnings-and.html)　·　Cocoa with Love (Matt Gallagher)

Objective-C's unique syntax results in unique ways of making mistakes. In this post, I look at the compiler warnings and errors GCC outputs when you make mistakes or potential mistakes in your Objective-C syntax and show you how to fix them.

## Every warning _is_ an error

Objective-C lets a lot of potentially fatal problems related to method invocations go through as warnings. This is because the method lookup system is dynamic and from the compiler's perspective you _could_ provide a resolution at runtime.

To make this overly permissive situation in Objective-C safer, you should treat every warning as a potentially fatal error. This means that you should turn on `GCC_TREAT_WARNINGS_AS_ERRORS` (`-Werror`) in your build settings so you can catch these problems and fix them instead of letting your program run until it crashes at runtime.

Every warning has an approach to eliminate the warning. These warning-less approaches invariably represent better design. I'll let you know how to fix each of the warnings/errors listed here.

## 1. Improperly nested method brackets

```objc
/path/file.m:15: error: syntax error before 'autorelease'
```

(where `autorelease` could be the first word in any method) or

```objc
/path/file.m:15: error: syntax error before ';' token
```

These are the only syntax errors I'm going to include in this list — my reason for including them is that, despite the obvious nature of the problem and its high occurrence rate, GCC presents the errors in a non-descript way that doesn't reveal the underlying problem.

The first error is "you are missing an opening bracket somewhere before this". The second error is "you are missing a closing bracket immediately before the semi-colon".

It would be great if GCC gave an error like "unmatched bracket" and pointed to the unmatched bracket. Apple [are hinting](http://clang.llvm.org/diagnostics.html) that future clang-based compilers may do this but for now, you get one of these terse errors.

## 2. Trying to use a forward class

```objc
/path/file.m:22: warning: receiver 'Test' is a forward class and corresponding @interface may not exist
```

This is a simple error but many people (especially those accustomed to other languages that don't have separate declaration and implementation) find it confusing because they may not be certain what a "forward class" is.

I'd like to take this opportunity to tell you: if you don't know what a [forward declaration](http://en.wikipedia.org/wiki/Forward_declaration) is, or you've never used `@class` before, you need to [read about it](http://developer.apple.com/DOCUMENTATION/Cocoa/Conceptual/ObjectiveC/Articles/ocDefiningClasses.html). In brief: a `@class` forward declaration tells the compiler that a given name is a class but avoids the need to import the whole declaration (which would create an undesirable cross-dependency in the header file).

> **Basic rule:** in _header_ files, never `#import` another class from the same framework/application except the super class — always use an `@class` forward definition instead. The `#import` for a class should always be in the _implementation_ (.m) file. Using `#import` for other frameworks (like `#import <Cocoa/Cocoa.h>`) is okay.

The cause of this warning is failure to follow the second part of this basic rule: you need to `#import` the actual definition in your implementation file.

Older versions of GCC (prior to 4.0) didn't always give this warning. The result was that you could accidentally use classes that didn't exist (resulting in runtime crashes). This warning is a big improvement.

## 3. Recursive headers

```objc
/path/file.h:13: warning: duplicate interface declaration for class 'Test'
/path/file.h:15: error: redefinition of 'struct Test'
```

There are two ways to get this error. The first is mundane: you have declared two classes with the same name — not an Objective-C specific problem.

The second is that you have used `#include` to import the header declaration instead of `#import`. This is especially recognizable when you see the error dozens (or hundreds) of times in a row, especially if it is further accompanied by:

```objc
/path/file.h:9:35: error: #include nested too deeply
```

Objective-C expects that all header files are imported using `#import` which prevents recursive inclusion, so files don't guard against repeat inclusion as they normally do in standard C.

Solution: always use `#import` to import header declarations (and don't listen to Richard Stallman's rants against the `#import` keyword — he is... different).

## 4. Interface not imported

```objc
/path/file.m:26: warning: no '-blah' method found
/path/file.m:26: warning: (Messages without a matching method signature
/path/file.m:26: warning: will be assumed to return 'id' and accept
/path/file.m:26: warning: '...' as arguments.)
```

The mundane explanation is that there is no `blah` method (you've simply mistyped it).

However, Objective-C provides a few ways to get this error, even when the method _does_ exist.

- The class where `-blah` is defined may not be in the set of imported classes. This can happen when the object you tried to invoke `-blah` on is declared as an `id` or the class is only forward declared.
- You have imported the base class but the method is declared on a `@category`, which is not imported.

In either case, the solution is to find the header that defines the method and `#import` it.

There is one further situation where this error can occur: when there is no implementation of the method at compile-time at all. This can further be broken into two cases:

- Runtime handled methods with clear association with a particular class. For example: accessor methods for the attributes of a Core Data `NSManagedObject`s. For methods like this, you should declare the method in a category (even though there will be no implementation at compile-time) and import this category.
- Runtime handled methods with no clear class association. To highlight the runtime and unusual situation involved in this situation you should use `[object performSelector:@selector(weirdRuntimeMethod)]` instead of writing `[object weirdRuntimeMethod]` and causing compiler warnings.

## 5. Multiple, incompatible methods

```objc
/path/file.m:24: warning: multiple methods named '-setStringValue:' found
```

Normally, Objective-C won't complain if there are multiple methods matching a given name (it assumes runtime lookup will work it out) so this warning may be surprising when it occurs.

This type of problem occurs when you have multiple declarations with the same method name but the arguments to the method are different sizes (e.g. one declaration expects a 32-bit long parameter and one declaration expects a 64-bit long parameter). This is important because parameter sizes are fixed at compile-time (runtime lookup can't change it).

The solution is to tell the compiler which method is the correct method by casting your object to the exact class involved. For example:

```objc
[(NSXMLNode *)myObject setStringValue:@"value"];
```

or

```objc
NSXMLNode *myXMLNodeObject = myObject;
[myXMLNodeObject setStringValue:@"value"];
```

Both of these solutions produce the same compiled output.

## 6. Accessing a property on the wrong type

```objc
/path/file.m:23: error: request for member 'value' in something not a structure or union
```

This error can occur in standard C code when using `struct` or `union` as the error reports.

In Objective-C 2.0, it also occurs when accessing an Objective-C 2.0 property on a class and the compiler can't find the property.

If this error occurs and you have typed the name correctly, you probably need to cast the object to the correct class. i.e. if `value` is a property of `MyClass`:

```objc
id value = ((MyClass *)object).value;
```

or

```objc
MyClass *myClassObject = object;
id value = myClassObject.value;
```

These solutions are, as before, both equivalent.

The other potential cause of this error is that `MyClass` is not imported correctly, so be certain to check this as well.

## 7. Implicit downcasting on assignment

```objc
/path/file.m:22: warning: initialization from distinct Objective-C type
```

The mundane cause of this error is that you've tried to assign the return value of a method to an unrelated object type. That's just an error and you need to fix it.

The trickier case is an implicit downcast. By this I mean: the method has returned a super class (like `NSObject`) but you know it is actually a child class (like `MyClass`).

In this situation you must explicitly cast:

```objc
MyClass *myClassObject = (MyClass *)[someObject getObject];
```

C++ has the `dynamic_cast` operator for this type of action, which verifies that `myClassObject` is correctly a `MyClass` object. In Objective-C if you're concerned about runtime type, you should use:

```objc
NSAssert([myClassObject isKindOfClass:[MyClass class]],
    @"Return value is not of type MyClass as expected.");
```

You can use your own `AssertCast` macro to make this operation easier if you do it a lot.

There are two cases where implict casts are allowed:

- upcasts (i.e. `NSObject *myObject = myClassObject;` is okay)
- implicit conversions from `id` to anything (`id` is the universal object and can be implicitly cast or used as anything)

This error can also occur in the case where the assignment is actually an upcast but the source class has only a forward declaration — so you may also need to import the declaration if it is not imported.

## 8. Implicit downcasting of parameters

```objc
/path/file.m:24: warning: passing argument 1 of 'test:' from distinct Objective-C type
```

The causes and solutions for this are identical to downcasting on assignment. Cast correctly and import declarations as appropriate.

I know, this warning seems like a duplicate of number 7 but it's a programming blog: I had to have 8 things. In my head, I've stored them all in an array indexed from 0 to 7.

## Conclusion

Never be content with warnings in your code. Always work to understand why GCC is issuing the warning and fix your code. Your code will be easier to understand and be safer at runtime.
