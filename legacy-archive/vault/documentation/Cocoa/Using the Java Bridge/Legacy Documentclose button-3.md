---
title: Using the Java Bridge
apple_id: TP40001404
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.2.html
archived_at: '2026-07-15T07:16:24.116894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Using the Java Bridge](Legacy%20Documentclose%20button.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/index.html)  __>__  [Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/index.html) __>__
Using the Java Bridge

---

# Legacy Documentclose button

__Important:__
The information in this document is obsolete and should not be used for new development.

[Previous](Legacy%20Documentclose%20button-2.md) | [Next](Legacy%20Documentclose%20button-4.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)

[Using the Java Bridge](Legacy%20Documentclose%20button.md)

#  How the Bridge Works

The term _bridge_
refers to the fact that there is a connection between two different worlds: the Objective-C world and the Java world. To use the bridge effectively, it's helpful to understand what's happening on each side of the bridge.

The Java bridge allows you to write code in one language that references an object from the other language. For example, you can send a message to a Java object from Objective-C:


```
myInt = [myJavaObject numberOfItems];
```


And you can send a message to an Objective-C object from Java:


```
myInt = myObjCObject.numberOfItems();
```


The bridge uses two basic approaches to allow this type of communication:

- Objects of certain commonly used classes are transparently converted, or _morphed_
  , into a corresponding object on the other side of the bridge. An example would be using a Java String object in a method call that expects an Objective-C NSString. See [Morphing](#apple-ijdugqsgijeus)
  for more information.
- 

  For all other objects, the bridge builds a _proxy_
  object that references the actual object on the other side of the bridge that is being messaged.

Exposing Objective-C classes to Java code requires a bit more work than the converse. Because Java is a strongly typed language, it requires more information about the classes and interfaces it manipulates at compile time. Therefore, before using Objective-C classes as Java ones, a description of them has to be written and compiled. This is called _wrapping_
the Objective-C classes. The wrapping process involves creating a _Java to Objective-C Bridging Specification_
(`.jobs`
) file--either with the WrapIt application or by hand--and processing it with a tool called `bridget`
. See [Wrapping Objective-C Frameworks](Legacy%20Documentclose%20button-5.md#apple-ijdugqsfizcui)
for more information.

Java has a facility called the Java Native Interface, which allows a Java programmer to write methods that are implemented in another language (such as C or Objective-C). The Java bridge makes use of this capability to allow you to send messages from Java to Objective-C:

- It provides a native method for each Objective-C method that is being wrapped.
- 

  It generates stub code that dispatches to the Objective-C method.

Suppose you have an Objective-C framework containing a class called Foo with a method called `ping`
, as follows:


```objc
@interface Foo:NSObject
     - (void) ping;  //the actual Objective-C method
@end
```


To use this method from Java, you specify in your `.jobs`
file that you want to expose the Foo class, and that its corresponding Java name should be Foo (you must also specify the package name, for example, `com.yourFirm.whatever.Foo`
). You also specify that you want to expose the `ping`
method (and its Java name, if different).

The `bridget`
tool generates a native method declaration (in `Foo.java`
) that looks like this:

public class Foo() extends com.apple.cocoa.foundation.NSObject { public native void ping(); //native method declaration}

The `native`
keyword indicates that the code for the method is in a language other than Java.

`Bridget`
also generates a file containing _stub_
code, which is the actual code that gets called on the Objective-C side. This stub code lives in a file called packageName_className_ `stubs.m`
. By convention, the stub routine for the native method has the name _Java_className_methodName_
. The following code illustrates what such a stub routine might look like:


```
void Java_Foo_ping(JAVAHandle object) {
    [BRIDGEJavaHandleToId(object) ping]; //the Objective-C method call
}
```


__Note:__
JAVAHandle is the way the bridge points to a Java object. BRIDGEJavaHandleToId is a function that converts the Java handle to an Objective-C id. These examples are intended to give a sense of how the bridge works. Normally, you don't need to understand these internal bridge data types in detail, unless you are writing morphing conversion routines, for example. In that case, you can refer to the bridge header files (located in `/System/Developer/Java/Headers/`
) for more information.

To call this method from Java, you'd write code such as the following:


```
myFooObject = new Foo();
myFooObject.ping();
```


When you instantiate a Foo object, the Java bridge creates a proxy object on the Java side and a "real" object on the Objective-C side, which is the receiver of any messages that you send to it.

##  Morphing

There are some frequently used classes for which the Java bridge supplies automatic conversion functions, so that you don't need to provide a wrapper. When you use an instance of one of these classes, it is transparently converted (or _morphed_
) into the corresponding class on the other side of the bridge.

For example, suppose the `ping`
method took an NSString argument:


```objc
@interface Foo:NSObject
     - (void) ping:(NSString *) theString);
@end
```


When you call this method from Java, you pass in a Java String object:


```
myFooObject.ping(myString);
```


The stub code looks something like this:


```
Java_Foo_ping(JAVAHandle object, JAVAHandle str) {
    [BRIDGEJavaHandleToId(object) ping:JavaStringToNSString(str)];
}
```


The first argument to this function points to the object to which the message is being sent (that is, myFooObject on the Java side). The second argument points to the Java String object `myString`
. JavaStringToNSString is a function provided by the bridge that converts a Java String to an NSString. Its inverse is NSStringToJavaString. This means that you can use these types on both sides of the bridge, and the conversion takes place automatically.

You may want to provide your own conversion functions that transparently morph classes. For example, you might want to expose a C `struct`
as a Java class. See [Editing the Specification File](Legacy%20Documentclose%20button-5.md#apple-ijdugrcgjfbem)
for information on how to specify them.

Other classes that are morphed include Number (NSNumber) and Exception (NSException). In the case of NSException, this means that your Java code can handle exceptions as it normally would, regardless of whether the exception might have arisen in an Objective-C method.

---

[Previous](Legacy%20Documentclose%20button-2.md) | [Next](Legacy%20Documentclose%20button-4.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)

[Using the Java Bridge](Legacy%20Documentclose%20button.md)
\xA9 1998 Apple Computer, Inc.
