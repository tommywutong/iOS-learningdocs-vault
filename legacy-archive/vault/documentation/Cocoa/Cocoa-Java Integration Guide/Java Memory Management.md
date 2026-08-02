---
title: Cocoa-Java Integration Guide
apple_id: 10000112i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LanguageIntegration/Concepts/memory.html
archived_at: '2026-07-15T07:16:22.223416Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa-Java Integration Guide](Introduction%20to%20Cocoa-Java%20Integration%20Guide.md)


[Next](Using%20NSSelector.md)[Previous](Method%20Selectors.md)

# Java Memory Management

Under most circumstances, Java applications do not need to concern themselves with memory management. Because Cocoa is an Objective-C framework without automatic garbage collection, however, Java applications sometimes need to take steps to handle peculiarities in this mixed-language environment.

Creating and destroying Cocoa objects in Java is the same as creating and destroying any object in Java. You create an object with a constructor and the object persists as long as a reference is maintained. When the last reference is eliminated, the object is automatically destroyed. The Java Bridge, which handles the communication between the Objective-C and Java environments, works with the Java garbage collector to track references to Objective-C objects in the Java environment (and Java objects in the Objective-C environment) to make sure the objects persist as long as references exist. (See [Weak References in Java](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaydcljzgy4dioa) for a special case when this is not strictly true.)

Also note that although Cocoa object constructors do not declare `throws` clauses, they can still throw a runtime exception. The thrown exception is an instance of the NSException class, a subclass of `java.lang.RuntimeException`.

Objective-C does not implement automatic reference counting, so applications need to explicitly `retain` objects that need to persist and `release` objects when a reference is no longer needed. In some cases, however, Cocoa uses a weak reference to objects wherein a pointer to an object is recorded but the object is not retained. (See Weak References to Objects for details.)

Weak references are mostly used to break circular references where retaining each object would prevent the objects from deallocating when they should. Child-parent relationships, such as in the view hierarchy, are cases where weak references are used. Cocoa also uses weak references for table data sources, outline view items, notification observers, and miscellaneous targets and delegates.

Weak references pose a problem for Java applications when a pure Java object, one not descended from Cocoa’s NSObject, is passed to a Cocoa object using a weak reference. When the Java object is passed through the Java bridge to the Objective-C Cocoa object, a proxy is created to represent the Java object. Because only a weak reference is used, when control passes back to the Java side, the proxy object is left with a reference count of zero, so it is deallocated. Messages sent to that object, messages that should be forwarded to the Java object, instead find a deallocated object, so an error occurs.

To work around the problem, the proxy object needs to get retained by an Objective-C object. The easiest way to do this is to store the Java object inside an NSArray. An NSArray, an Objective-C object exported into Java, retains its elements, releasing them when the array is deallocated. The Java application thus needs to keep a reference to the NSArray in addition to (or perhaps instead of) the pure Java object.

[Next](Using%20NSSelector.md)[Previous](Method%20Selectors.md)

