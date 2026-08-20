---
title: Using the Java Bridge
apple_id: TP40001404
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.3.html
archived_at: '2026-07-15T07:16:24.126979Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Using the Java Bridge](Legacy%20Documentclose%20button.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/index.html)  __>__  [Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/index.html) __>__
Using the Java Bridge

---

# Legacy Documentclose button

__Important:__
The information in this document is obsolete and should not be used for new development.

[Previous](Legacy%20Documentclose%20button-3.md) | [Next](Legacy%20Documentclose%20button-6.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)

[Using the Java Bridge](Legacy%20Documentclose%20button.md)

#  Using Java from Objective-C

In Objective-C, you can use Java classes and interfaces as if they were Objective-C classes and protocols.

To reference class objects, you must use the function `NSClassFromString()`
, since the Objective-C compiler can't generate static references to bridged Java classes. For example, to instantiate an object from the `AJavaClass`
class, you would write code such as the following:


```
MyJavaClass = NSClassFromString(@"java.util.AJavaClass");
MyJavaObj = [[MyJavaClass alloc] init];
```


You can instantiate Java classes from Objective-C and see them as if they were pure Objective-C objects. You can also pass Objective-C objects as parameters to Java methods.

To invoke a Java method from Objective-C:

- If you've specified an explicit mapping between the selector name and a Java method name in a `.jobs`
  file, your specified Java method name is used.
- 

  If you haven't mapped the selector name to a Java method name in a `.jobs`
  file, the bridge automatically derives the Java method name from the Objective-C selector name by removing everything beyond the first colon. Thus, a method such as `sendBar:x foo:y`
  would map to `sendBar(x,y)`

Exceptions raised within the Java code are caught and transformed into NSExceptions, which can then be handled by your code on the Objective-C side.

---

[Previous](Legacy%20Documentclose%20button-3.md) | [Next](Legacy%20Documentclose%20button-6.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)
\xA9 1998 Apple Computer, Inc.
