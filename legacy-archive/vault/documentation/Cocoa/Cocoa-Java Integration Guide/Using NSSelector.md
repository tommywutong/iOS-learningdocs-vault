---
title: Cocoa-Java Integration Guide
apple_id: 10000112i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LanguageIntegration/Tasks/usingselectors.html
archived_at: '2026-07-15T07:16:23.720239Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa-Java Integration Guide](Introduction%20to%20Cocoa-Java%20Integration%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Java%20Memory%20Management.md)

# Using NSSelector

To create a selector in Java, use NSSelector’s single constructor, which takes the method’s name and an array of the parameter types. Note that to obtain a Class object for a type, append `.class` to the type’s name. For example, the Class object for NSObject is `NSObject.class` and the Class object for boolean is `boolean.class`.

This code sample creates a selector for the `doIt` method:

```
void doIt(String str, int i) { . . . }
NSSelector sel =
    new NSSelector("doIt", new Class[] {String.class, int.class} );
```

To apply a selector on an object, use the overloaded instance method `invoke`. It performs the method that matches the selector and returns the result. If the target object does not have a method matching the selector, it throws NoSuchMethodException. The most basic form of `invoke` takes the target object and an Object array of the arguments. Other forms are convenience methods for selectors with no, one, or two arguments. Note that to pass an argument of a primitive type to `invoke`, use an object of the corresponding wrapper class. `invoke` converts the object back to the primitive type when it invokes the method. For example, to pass the float `f`, use `new Float(f)`; and to pass the boolean value `true`, use `new
Boolean(true)`.

This code sample gives you two ways to apply the selector `sel` (defined above) to an object:

```
MyClass obj1 = new MyClass(), obj2 = new MyClass();
int i = 5;
sel.invoke(obj1, new Object[] { "hi", new Integer(i) });
sel.invoke(obj2, "bye", new Integer(10));
```

To create and apply a selector in one step, use the overloaded static method `invoke`. The basic form takes four arguments: the method name, an array of the parameter types, the target object, and an array of the arguments. Other forms are convenience methods for selectors with one or two arguments. This code sample shows two ways to create and apply a selector for the `doIt` method:

```
void doIt(String str, int i) { . . . }
MyClass obj1 = new MyClass(), obj2 = new MyClass();
int i = 5;

NSSelector.invoke("doIt", new Class[] {String.class, int.class},
    obj1, new Object[] {"hi", new Integer(i)});
NSSelector.invoke("doIt", String.class, int.class,
    obj1, "bye", new Integer(10));
```

Other methods return whether an object or class has a method that matches a selector (`implementedByObject` and `implementedByClass`) and returns the method name and parameter types for a selector (`name` and `parameterTypes`).

[Next](Document%20Revision%20History.md)[Previous](Java%20Memory%20Management.md)

