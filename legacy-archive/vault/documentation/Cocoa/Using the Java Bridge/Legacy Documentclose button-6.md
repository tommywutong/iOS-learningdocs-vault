---
title: Using the Java Bridge
apple_id: TP40001404
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.4.html
archived_at: '2026-07-15T07:16:24.134242Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Using the Java Bridge](Legacy%20Documentclose%20button.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/index.html)  __>__  [Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/index.html) __>__
Using the Java Bridge

---

# Legacy Documentclose button

__Important:__
The information in this document is obsolete and should not be used for new development.

[Previous](Legacy%20Documentclose%20button-4.md) | [Next](Legacy%20Documentclose%20button-5.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)

[Using the Java Bridge](Legacy%20Documentclose%20button.md)

#  Using Java-Wrapped Objective-C Classes

This section describes how to use wrapped Objective-C classes from Java. The next section, [Wrapping Objective-C Frameworks](Legacy%20Documentclose%20button-5.md#apple-ijdugqsfizcui)
explains how to wrap Objective-C frameworks.

To get information about the classes in a wrapped framework, you can't look at header files as you would in Objective-C. Instead, you can:

- Look at documentation provided with wrapped frameworks from Apple, such as Foundation Kit, AppKit, WebObjects, and Enterprise Objects.
- 

  Use the Java Class Browser. This application allows you to browse Java packages found in your `CLASSPATH`
  (an environment variable that specifies the search path for Java `.class`
  files. It lists the classes and the syntax of their methods, even for classes for which you don't have the source code.

##### Java Class Browser

!

Objective-C methods use keywords for method arguments, while Java uses comma-separated lists (as with C and C++). For example, in Objective-C, the following declares an instance method that takes two parameters:


```objc
-(void)setObject:(id)anObject forKey:(id)aKey;
```


In Java, the same method is declared as follows:


```
void setObjectForKey(Object anObject, Object aKey);
```


The Java names for methods and classes may or may not be the same as their Objective-C counterparts. It's up to the developer of the wrapped framework to decide how Objective-C names are exposed in Java. [Wrapping Objective-C Frameworks](Legacy%20Documentclose%20button-5.md#apple-ijdugqsfizcui)
explains the rules and options for mapping names between the two languages.

For the most part, you can use the classes in a wrapped Objective-C framework just as you would use any Java class. The bridge transparently loads in any needed Objective-C framework whenever a bridged class is used. You can invoke Objective-C instance methods as you'd expect:


```
myInt = myObjCObject.aMethod();
```


Java objects can be passed back to the Objective-C world and manipulated by the code there as if they really were Objective-C classes.

You can invoke a class method by referencing the class name directly:


```
ObjCClassName.classMethod();
```


One restriction is that instance variables in Objective-C classes are not exposed in Java. The class must provide accessor methods that set and get their values.

You can subclass Objective-C classes in Java just like you can any other class:


```
class MySubClass extends MyObjCClass {
    ...
}
```


Again, the original class's instance variables aren't exposed; therefore, they aren't inherited. You can, however, add your own instance variables to the subclass.

As with other classes, you can call `super`
from a Java subclass of an Objective-C class to invoke the Objective-C class's implementation.

In Objective-C, you create objects with `alloc`
and initialize them with class initialization methods such as `init`. In Java, you create objects with `new`
and initialize them with the class's constructor.

For example, to create an instance of the Foo class in Objective-C:


```
someObject = [[Foo alloc] init];
```


In Java:


```
someObject = new Foo();
```


In Objective-C, initialization methods are instance methods, applied to newly created objects. In Java, constructors are not used in the same way as instance methods. Therefore, Objective-C initialization methods must be explicitly specified as constructors when the classes are wrapped. If there is more than one initialization method, they become Java constructors with different argument types. See [Editing the Specification File](Legacy%20Documentclose%20button-5.md#apple-ijdugrcgjfbem)
for specifics on how to do this.

One difference between Java and Objective-C is memory management. In Java, unused objects are garbage-collected. In Objective-C, you must keep track of object references and release objects when they are no longer needed.

For the most part, you don't need to worry about these differences. One possible occurs if you create a new thread in Java, and that thread manipulates some objects with Objective-C counterparts. In that case, you must explicitly create an autorelease pool at the beginning of the thread, and remove it at the end of the thread.

---

[Previous](Legacy%20Documentclose%20button-4.md) | [Next](Legacy%20Documentclose%20button-5.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)
\xA9 1998 Apple Computer, Inc.
