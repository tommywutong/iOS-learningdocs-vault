---
title: Cocoa-Java Integration Guide
apple_id: 10000112i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LanguageIntegration/Concepts/selectors.html
archived_at: '2026-07-15T07:16:22.703990Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa-Java Integration Guide](Introduction%20to%20Cocoa-Java%20Integration%20Guide.md)


[Next](Java%20Memory%20Management.md)[Previous](Introduction%20to%20Cocoa-Java%20Integration%20Guide.md)

# Method Selectors

Cocoa makes extensive use of the target-action design paradigm. This allows you to have one object send an arbitrary message (the action) to an arbitrary object (the target) in response to an event, such as a button being pressed or a notification being posted. The Objective-C language provides support for this paradigm by allowing any message to be sent to any object, without needing to know the class of the object first. The message is specified by the Objective-C type `SEL` (also called a selector), usually obtained with the `@selector()` directive. (See Selectors in _The Objective-C Programming Language_ for a more detailed discussion.)

Java, however, is a strongly-typed language wherein you must know the class of an object before sending it a message. To bring target-action support to Java, Cocoa implements the NSSelector class. An NSSelector object specifies a method signature, which is a method’s name and parameter list. You can later apply a selector on any object, and it performs the method that matches the selector, if there is one.

NSSelector is similar to `java.lang.reflect.Method`, which fully specifies a particular class’s implementation of a method, but you can apply it only to objects of that class. NSSelector does not specify the method’s class, so you can apply it to an object of any class. To find the `java.lang.reflect.Method` object for a method that matches an NSSelector object and that is in a particular object or class, use the NSSelector instance method `methodOnObject` or `methodOnClass`.

See [Using NSSelector](Using%20NSSelector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dslkciffeessdirdq) for examples of how you use the NSSelector class.

[Next](Java%20Memory%20Management.md)[Previous](Introduction%20to%20Cocoa-Java%20Integration%20Guide.md)

