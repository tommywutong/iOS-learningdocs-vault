---
title: 'Objective-C Internals: Class Architecture Objective-C has an unique class architecture where classes are objects. Its elegant design enables dynamic method dispatch for all object types through the us'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/01/02/objc-class-arch'
original_language: en
published: 2023-01-02
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5f6e0907d814dbc4'
translated: false
---

> 原文：[Objective-C Internals: Class Architecture Objective-C has an unique class architecture where classes are objects. Its elegant design enables dynamic method dispatch for all object types through the us](https://alwaysprocessing.blog/2023/01/02/objc-class-arch)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Class Architecture

![Two yellow English Labradors on a work table with pencils, paper, and other design instruments.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/bbda3229-a843-497b-efad-887288209a00/public)

Objective-C has an unique class architecture where classes _are_ objects. Its elegant design enables dynamic method dispatch for all object types through the use of a compiler generated metaclass.

Objective-C, like many popular languages, uses a [class-based style](https://en.wikipedia.org/wiki/Class-based_programming) of [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming). For the purposes of discussing Objective-C’s class architecture, we’ll focus on class behavior (methods and properties) and set aside class state (i.e., instance variables, which are covered [in this post](https://alwaysprocessing.blog/2023/03/12/objc-ivar-abi)).

The following six lines of code are all we need to explore Objective-C’s class architecture:

```
@interface MyObject: NSObject
+ (void)classMethod;
- (void)instanceMethod;
@end

MyObject *object = [[MyObject alloc] init];
```

## Method Dispatch

Line 6 instantiates the class `MyObject` and assigns the new object instance to the variable `object`. The new object instance has its own state and can respond to messages (i.e. method calls) like `-instanceMethod` and `-init`.

Objective-C uses [dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch)[[1](#_footnotedef_1)] for each message send (i.e. for each method call). The runtime finds the method implementation by looking up the selector (i.e. method name) in the class object referenced by the instance’s `isa` variable. (The first instance variable in all Objective-C objects is the `isa` pointer, which is automatically inserted by the compiler and initialized by the runtime.)

The use of the term _class object_ in the previous paragraph was intentional: in Objective-C, classes are also objects! This ingenious design is the basis for the _class methods_ language feature (e.g. calling `[NSObject alloc]` or `[MyObject classMethod]`): it enables class methods to be fully polymorphic (i.e. a subclass can override a class method), and it erases any runtime distinction between class methods and instance methods (both class and instance methods are dispatched via `objc_msgSend`).

Because classes are objects, they too have an `isa` pointer, which references the _metaclass_. The metaclass provides the selector-to-class method implementation map for the class object in the same way the class object provides the selector-to-instance method implementation map for a class instance (i.e. object).

## Inheritance

Any class or metaclass only provides selector-to-method implementation mappings for methods implemented by the class. In the code example above, the class object for `MyObject` has a mapping for `instanceMethod` and the metaclass for `MyObject` has a mapping for `classMethod`.

`MyObject` also responds to `+alloc` and `-init`, which are implemented in `NSObject`. Each class object (including each metaclass) has a reference to its super class. When resolving a selector, if the class/metaclass object does not define a mapping, the runtime searches the next super class for a definition. (The runtime will throw an exception if no definition is found at the end of the super class chain, though the runtime also provides escape hatches to handle the scenario.)

## Architecture Diagram

The following diagram illustrates the Objective-C class design discussed above:

- The `object` instance has an `isa` variable that points to the `MyClass` class object.
- The `MyClass` class object has:

    - An `isa` variable that points to the `MyClass` metaclass.
    - A `super` variable that points to the `NSObject` class object.
- The `MyClass` metaclass has:

    - An `isa` variable that points to the `NSObject` (root object) metaclass.
    - A `super` variable that points to the `NSObject` metaclass.

The diagram also shows a few points not captured by the discussion above:

- The `isa` variable of each metaclass points to the metaclass of the root object, including the root object metaclass itself. It makes sense that the `isa` isn’t `nil` (an object has to have _some_ type), but I’m not sure why all metaclasses are of the type of the root metaclass as opposed to, say, a type provided by the runtime. I suppose, though, it doesn’t actually matter as the metaclass itself never receives messages.
- The super class of the root metaclass is the root class object. I was surprised to learn this when researching for the diagram. It’s not immediately clear to me why this link exists—​I thought its super class would be `nil`.

If anyone has insight into the rationale for these design artifacts, please reach out and let me know!

---

[1](#_footnoteref_1). Clang, beginning in either [Xcode 11.x](https://pspdfkit.com/blog/2020/improving-performance-via-objc-direct/) or [Xcode 12](https://nshipster.com/direct/), added support for _direct_ (i.e. [static](https://en.wikipedia.org/wiki/Static_dispatch)) dispatch. However, I’ve not been able to locate any reference to the feature in Xcode Release Notes or in WWDC sessions.
