---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Java/AccessingObjectiveC.html
archived_at: '2026-07-15T07:49:20.578129Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](TOC.md)
[!Previous Section](WritingJavaApps.md)

## Accessing Java Objects from WebScript and Objective-C

The WebObjects Java Extensions enable communication between WebScript, Objective-C, and Java objects. From either WebScript or Objective-C, the Extensions provide access to Java objects as follows:

- If the Java object is a common one that has a direct Objective-C counterpart, it's simply copied into that counterpart. Such objects are referred to as _morphed_ objects. Among the morphed objects are Strings, Numbers, and Dates, since they all have their equivalent in Objective-C. With morphed objects, no correspondence is maintained between the Java and Objective-C objects.
- If the object isn't morphed, the Extensions automatically build a per-Java-object Objective-C proxy that references the Java object. Objective-C messages are trapped, and the selector name is transformed into a Java method name. If you've specified an explicit mapping between the selector name and a Java method name in a __.jobs__ file (see ["Wrapping Your Objective-C Classes"](WrappingObjectiveC.md#apple-kjcummjtgm3de)), this transformation is simple: your specified Java method name is used. This allows you to map, for example, __-description__ to __toString()__ or __-performSelector:withObject:withObjects:__ to __performMethodWithObjects()__. If you haven't mapped the selector name to a Java method name in a __.jobs__ file, the Extensions automatically derive the Java method name from the Objective-C selector name by removing everything beyond the first colon. Thus, a method such as __sendBar:x foo:y__ would map to __sendBar(x,y)__). In either case, once the Java method name is determined the Java object implementation is searched for that method and, if it's found, the Extensions use its type signature information to transform the Objective-C call stack into a Java call frame. The Java method is then dispatched.

However the Java object is accessed, exceptions raised within the Java code are caught and transformed into NSExceptions, which can then be handled by your code on the Objective-C side.

## Accessing Objective-C Objects from Java

The previous section discussed how the WebObjects Java Extensions allow Objective-C objects to message Java objects. In a similar fashion, the Extensions also allow Java objects to message Objective-C objects. From the Java side, the Extensions represent Objective-C objects as custom Java objects which inherit from the Java class __next.util.NextObject__. The Extensions use a combination of native methods and stub code to call from Java into Objective-C.

The WebObjects Java Extensions provide a number of useful Java classes in the __next.util__, __next.eo__, and __next.wo__ packages (see ["The Java Packages"](Packages.md#apple-kjcumnbuge3tk) for more information). These classes encapsulate the functionality of some of NeXT's more useful Objective-C classes and can be used by your Java code as-is.

To access an Objective-C object from Java, you simply create a Java "wrapper" around the Objective-C object using "bridget," a tool provided with the WebObjects Java Extensions for this purpose. The Java wrapper contains native stub functions that transform the Java arguments and dispatch an Objective-C method to the wrapped object, along with initialization code for the wrapped object. Note that these wrappers only work for method invocations: you cannot directly access the instance variables of an Objective-C object from its wrapped Java counterpart. The Objective-C object must either provide accessor functions, or you must us the __next.util.KeyValueCoding__ interface (which is implemented by __next.util.NextObject__). For information on how to use "bridget," see ["Wrapping Your Objective-C Classes."](WrappingObjectiveC.md#apple-kjcummjtgm3de)

### Subclassing Objective-C Classes in Java

You build a Java subclass of a wrapped class quite naturally by simply extending the Java wrapper class as you would any ordinary Java class. This works because the Java Extensions search the superclass chain of every new class of Java object that crosses from Java to the Objective-C side. If a wrapped class is discovered (such as __next.eo.CustomObject__) the Extensions dynamically build an Objective-C "shadow" class for this custom Java subclass. The shadow class mirrors every Java method discovered with a corresponding selector and a common implementation function. The implementation function dynamically looks up the Java method signature for guidance in transforming the stack into a Java call frame, giving the Java side the first chance at any invocation from the Objective-C side.

As expected, calling __super__ from a Java subclass of an Objective-C class messages the Objective-C class's implementation of the method.

Constructors of subclasses pose special problems since Java constructors have only a type signature. This means that the Extensions can't distinguish __-initWithReversedArray:__ from __-initWithArray:__. Because of this, bridget

requires you to specify the name of the init method that should map to a Java constructor with a corresponding type signature.

[!Table of Contents](TOC.md)
[!Next Section](Packages.md)
