---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocSelectors.html
archived_at: '2026-07-15T07:17:31.911439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [The Objective-C Programming Language](Introduction.md)


[Next](Exception%20Handling.md)[Previous](Enabling%20Static%20Behavior.md)

# Selectors

In Objective-C, _selector_ has two meanings. It can be used to refer simply to the name of a method when it’s used in a source-code message to an object. It also, though, refers to the unique identifier that replaces the name when the source code is compiled. Compiled selectors are of type `SEL`. All methods with the same name have the same selector. You can use a selector to invoke a method on an object—this provides the basis for the implementation of the target-action design pattern in Cocoa.

For efficiency, full ASCII names are not used as method selectors in compiled code. Instead, the compiler writes each method name into a table, then pairs the name with a unique identifier that represents the method at runtime. The runtime system makes sure each identifier is unique: No two selectors are the same, and all methods with the same name have the same selector.

Compiled selectors are assigned to a special type, `SEL`, to distinguish them from other data. Valid selectors are never `0`. You must let the system assign `SEL` identifiers to methods; it’s futile to assign them arbitrarily.

The `@selector()` directive lets you refer to the compiled selector, rather than to the full method name. Here, the selector for `setWidth:height:` is assigned to the `setWidthHeight` variable:

```
SEL setWidthHeight;
setWidthHeight = @selector(setWidth:height:);
```

It’s most efficient to assign values to `SEL` variables at compile time with the `@selector()` directive. However, in some cases, you may need to convert a character string to a selector at runtime. You can do this with the [NSSelectorFromString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSSelectorFromString) function:

```
setWidthHeight = NSSelectorFromString(aBuffer);
```

Conversion in the opposite direction is also possible. The [NSStringFromSelector](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSStringFromSelector) function returns a method name for a selector:

```
NSString *method;
method = NSStringFromSelector(setWidthHeight);
```


Compiled selectors identify method names, not method implementations. The `display` method for one class, for example, has the same selector as `display` methods defined in other classes. This is essential for polymorphism and dynamic binding; it lets you send the same message to receivers belonging to different classes. If there were one selector per method implementation, a message would be no different from a function call.

A class method and an instance method with the same name are assigned the same selector. However, because of their separate domains, there’s no confusion between the two. A class could define a `display` class method in addition to a `display` instance method.

The messaging routine has access to method implementations only through selectors, so it treats all methods with the same selector alike. It discovers the return type of a method, and the data types of its parameters, from the selector. Therefore, except for messages sent to statically typed receivers, dynamic binding requires all implementations of identically named methods to have the same return type and the same parameter types. (Statically typed receivers are an exception to this rule because the compiler can learn about the method implementation from the class type.)

Although identically named class methods and instance methods are represented by the same selector, they can have different parameter types and return types.

The `performSelector:`, `performSelector:withObject:`, and `performSelector:withObject:withObject:` methods, defined in the `NSObject` protocol, take `SEL` identifiers as their initial parameters. All three methods map directly into the messaging function. For example,

```
[friend performSelector:@selector(gossipAbout:)
    withObject:aNeighbor];
```

is equivalent to:

```
[friend gossipAbout:aNeighbor];
```

These methods make it possible to vary a message at runtime, just as it’s possible to vary the object that receives the message. Variable names can be used in both halves of a message expression:

```
id   helper = getTheReceiver();
SEL  request = getTheSelector();
[helper performSelector:request];
```

In this example, the receiver (`helper`) is chosen at runtime (by the fictitious `getTheReceiver` function), and the method the receiver is asked to perform (`request`) is also determined at runtime (by the equally fictitious `getTheSelector` function).

In its treatment of user-interface controls, AppKit makes good use of the ability to vary both the receiver and the message at runtime.

`NSControl` objects are graphical devices that can be used to give instructions to an application. Most resemble real-world control devices such as buttons, switches, knobs, text fields, dials, menu items, and the like. In software, these devices stand between the application and the user. They interpret events coming from hardware devices such as the keyboard and mouse and translate them into application-specific instructions. For example, a button labeled “Find” would translate a mouse click into an instruction for the application to start searching for something.

AppKit defines a template for creating control devices and defines a few off-the-shelf devices of its own. For example, the `NSButtonCell` class defines an object that you can assign to an `NSMatrix` instance and initialize with a size, a label, a picture, a font, and a keyboard shortcut. When the user clicks the button (or uses the keyboard shortcut), the `NSButtonCell` object sends a message instructing the application to do something. To do this, an `NSButtonCell` object must be initialized not just with an image, a size, and a label, but with directions on what message to send and who to send it to. Accordingly, an `NSButtonCell` instance can be initialized for an action message (the method selector it should use in the message it sends) and a target (the object that should receive the message).

```
[myButtonCell setAction:@selector(reapTheWind:)];
[myButtonCell setTarget:anObject];
```

When the user clicks the corresponding button, the button cell sends the message using the `NSObject` protocol method `performSelector:withObject:`. All action messages take a single parameter, the `id` of the control device sending the message.

If Objective-C didn’t allow the message to be varied, all `NSButtonCell` objects would have to send the same message; the name of the method would be frozen in the `NSButtonCell` source code. Instead of simply implementing a mechanism for translating user actions into action messages, button cells and other controls would have to constrain the content of the message. Constrained messaging would make it difficult for any object to respond to more than one button cell. There would either have to be one target for each button, or the target object would have to discover which button the message came from and act accordingly. Each time you rearranged the user interface, you would also have to reimplement the method that responds to the action message. An absence of dynamic messaging would create an unnecessary complication that Objective-C happily avoids.

If an object receives a message to perform a method that isn’t in its repertoire, an error results. It’s the same sort of error as calling a nonexistent function. But because messaging occurs at runtime, the error often isn’t evident until the program executes.

It’s relatively easy to avoid this error when the message selector is constant and the class of the receiving object is known. As you write your programs, you can make sure that the receiver is able to respond. If the receiver is statically typed, the compiler performs this test for you.

However, if the message selector or the class of the receiver varies, it may be necessary to postpone this test until runtime. The `respondsToSelector:` method, defined in the `NSObject` class, tests whether a receiver can respond to a message. It takes the method selector as a parameter and returns whether the receiver has access to a method matching the selector:

```
if ( [anObject respondsToSelector:@selector(setOrigin::)] )
    [anObject setOrigin:0.0 :0.0];
else
    fprintf(stderr, "%s can’t be placed\n",
        [NSStringFromClass([anObject class]) UTF8String]);
```

The `respondsToSelector:` runtime test is especially important when you send messages to objects that you don’t have control over at compile time. For example, if you write code that sends a message to an object represented by a variable that others can set, you should make sure the receiver implements a method that can respond to the message.

[Next](Exception%20Handling.md)[Previous](Enabling%20Static%20Behavior.md)

