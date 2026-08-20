---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSSelector.html
archived_at: '2026-07-15T08:13:56.502129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSSelector

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Serializable

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSSelector object (also called a selector) specifies a method signature, which is a method's name and parameter list. You can later apply a selector on any object, and it performs the method that matches the selector, if there is one.

To create a selector, use NSSelector's single constructor, which takes the method's name and an array of the parameter types. Note that to obtain a Class object for a type, append `.class` to the type's name. For example, the Class object for Object is `Object.class` and the Class object for boolean is `boolean.class`

This code sample creates a selector for the __doIt__ method:

> ```
> void doIt(String str, int i) { . . . }
> NSSelector sel =
>     new NSSelector("doIt", new Class[] {String.class, int.class} );
> ```

To apply a selector on an object, use the overloaded instance method [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f). It performs the method that matches the selector and returns the result. If the target object doesn't have a method matching the selector, it throws NoSuchMethodException. The most basic form of __invoke__ takes the target object and an Object array of the arguments. Other forms are convenience methods for selectors with no, one, or two arguments. Note that to pass an argument of a primitive type to __invoke__, use an object of the corresponding wrapper class. __invoke__ converts the object back to the primitive type when it invokes the method. For example, to pass the float `f`, use `new Float(f)`; and to pass the boolean value true, use `new Boolean(true)`.

This code sample gives you two ways to apply the selector `sel` (defined above) to an object:

> ```
> MyClass obj1 = new MyClass(), obj2 = new MyClass();
> int i = 5;
> sel.invoke(obj1, new Object[] { "hi", new Integer(i) });
> sel.invoke(obj2, "bye", new Integer(10));
> ```

To create and apply a selector in one step, use the overloaded static method [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3fnrswg5dpoixws3twn5vwk). The basic form takes four arguments: the method name, an array of the parameter types, the target object, and an array of the arguments. Other forms are convenience methods for selectors with one or two arguments. This code sample shows two ways to create and apply a selector for the __doIt__ method:

> ```
> void doIt(String str, int i) { . . . } MyClass obj1 = new MyClass(), obj2 = new MyClass(); int i = 5;  NSSelector.invoke("doIt", new Class[] {String.class, int.class},      obj1, new Object[] {"hi", new Integer(i)}); NSSelector.invoke("doIt", String.class, int.class,     obj1, "bye", new Integer(10));
> ```

Other methods return whether an object or class has a method that matches a selector ( [implementedByObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnvygyzlnmvxhizleij4u6ytkmvrxi) and [implementedByClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnvygyzlnmvxhizleij4ug3dbonzq)) and returns the method name and parameter types for a selector ( [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3omfwwk) and [parameterTypes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3qmfzgc3lforsxevdzobsxg)).

NSSelector is similar to java.lang.reflect.Method, which fully specifies a particular class's implementation of a method, and you can apply it only to objects of that class. NSSelector doesn't specify the method's class, so you can apply it to an object of any class. To find the java.lang.reflect.Method object for a method that matches a selector and that's in a particular object or class, use [methodOnObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3nmv2gq33ej5xe6ytkmvrxi) or [methodOnClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3nmv2gq33ej5xeg3dbonzq).

## Method Types

---

> **Constructors**
>
> : [NSSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel2oknjwk3dfmn2g64q)
>
> **Static methods**
>
> : [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3fnrswg5dpoixws3twn5vwk)
>
> **Invoking selectors**
>
> : [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f)
>
> **Testing selectors**
>
> : [implementedByClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnvygyzlnmvxhizleij4ug3dbonzq): [implementedByObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnvygyzlnmvxhizleij4u6ytkmvrxi)
>
> **Converting selectors to java.lang.reflect.Methods**
>
> : [methodOnClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3nmv2gq33ej5xeg3dbonzq): [methodOnObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3nmv2gq33ej5xe6ytkmvrxi)
>
> **Accessing selector elements**
>
> : [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3omfwwk): [parameterTypes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3qmfzgc3lforsxevdzobsxg)
>
> **Methods inherited from Object**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3fof2wc3dt): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3imfzwqq3pmrsq): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3un5jxi4tjnztq)

## Constructors

---

### NSSelector

`public NSSelector(String methodName)`

Creates a selector for the method that's named _methodName_ and takes no parameters.

`public NSSelector( String methodName, Class[] parameterTypes)`

Creates a selector for the method that's named _methodName_ and takes parameters _parameterTypes_. To create a selector for a method that takes no arguments, use `null` for _parameterTypes_. For an example, see the class description for this class.

---

## Static Methods

---

### invoke

`public static Object invoke( String methodName, Class[] parameterTypes, Object target, Object[] arguments) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Creates and applies a selector that has any number of arguments. This method creates a selector with _methodName_ and the parameter types in the array _parameterTypes_, applies that selector to _target_ with the arguments in the array _arguments_, and returns the result. To apply a method that takes no arguments, use `null` for the arrays _parameterTypes_ and _arguments_. As part of its implementation, this method uses the NSSelector constructor and the instance method [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f). For more information, see those method descriptions.

`public static Object invoke( String methodName, Class parameterType, Object target, Object argument) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Creates and applies a selector that has one argument. This method creates a selector with _methodName_ and _parameterType_, applies that selector to _target_ with _argument_, and returns the result. As part of its implementation, this method uses the NSSelector constructor and the instance method [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f). For more information, see those method descriptions.

`public static Object invoke( String methodName, Class parameterType1, Class parameterType2, Object target, Object argument1, Object argument2) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Creates and applies a selector that has two arguments. This method creates a selector with _methodName_ and the parameter types _parameterType1_ and _parameterType2_, applies that selector to _target_ with the arguments _argument1_ and _argument2_, and returns the result. As part of its implementation, this method uses the NSSelector constructor and the instance method [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f). For more information, see those method descriptions.

---

## Instance Methods

---

### equals

`public boolean equals(Object anObject)`

Compares the receiving NSSelector object to _anObject_. If _anObject_ is an NSSelector and the contents of _anObject_ are equal to the contents of the receiver, this method returns true. If not, it returns false. Two selectors are equal if their names and parameter types are equal.

---

### hashCode

`public int hashCode()`

Provide an appropriate hash code useful for storing the receiver in a hash-based data structure.

---

### implementedByClass

`public boolean implementedByClass(Class targetClass)`

Returns whether the class _targetClass_ implements a method that matches the selector.

---

### implementedByObject

`public boolean implementedByObject(Object target)`

Returns whether the object _target_ implements a method that matches the selector. As part of its implementation, this method uses [implementedByClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnvygyzlnmvxhizleij4ug3dbonzq).

---

### invoke

`public Object invoke( Object target, Object[] arguments) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Invokes the method specified by the selector on _target_ with _arguments_, and returns the result. If that method is `void`, it returns `null`. Note that the method may be a static or instance method.

[invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f) can't handle arguments or return values of primitive types (such as boolean, int, or float). If the method matching the selector returns a value of a primitive type, __invoke__ returns the value in an object of the corresponding wrapper type (such as Boolean, Integer, or Float). To pass an argument of a primitive type to __invoke__, use an object of the corresponding wrapper class. __invoke__ converts the object back to the primitive type when it invokes the method.

__invoke__ throws an exception in the following cases:

- If _target_ has no method that matches the selector, it throws NoSuchMethodException.
- If a method matches the selector but is inaccessible to _target_, it throws IllegalAccessException.
- If it can't convert an argument to the type specified in the selector, it throws IllegalArgumentException.
- If the invoked method throws an exception, it wraps that exception in a java.lang.reflect.InvocationTargetException and throws the new exception without completing.

As part of its implementation, this method uses [methodOnClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3nmv2gq33ej5xeg3dbonzq).

For an example, see the class description for this class.

`public Object invoke( Object target) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Invokes the method specified by the selector on _target_ with no arguments, and returns the result. If that method is `void`, it returns `null`. Note that the method may be a static or instance method.

As part of its implementation, this method calls the [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f) instance method that takes an array of arguments. For more information, see that method's description.

`public Object invoke( Object target, Object argument) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Invokes the method specified by the selector on _target_ with one argument (_argument_), and returns the result. If that method is `void`, it returns `null`. Note that the method may be a static or instance method.

As part of its implementation, this method calls the [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f) instance method that takes an array of arguments. For more information, see that method's description.

`public Object invoke( Object target, Object argument1, Object argument2) throws IllegalAccessException, IllegalArgumentException, java.lang.reflect.InvocationTargetException, NoSuchMethodException`

Invokes the method specified by the selector on _target_ with two arguments (_argument1_ and _argument2_), and returns the result. If that method is `void`, it returns `null`. Note that the method may be a static or instance method.

As part of its implementation, this method calls the [invoke](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknswyzldorxxel3jnz3g623f) instance method that takes an array of arguments. For more information, see that method's description.

---

### methodOnClass

`public java.lang.reflect.Method methodOnClass(Class targetClass) throws NoSuchMethodException`

Returns the method on the class _targetClass_ that matches the selector. If _targetClass_ has no method that matches the selector, this method throws NoSuchMethodException.

---

### methodOnObject

`public java.lang.reflect.Method methodOnObject(Object target) throws NoSuchMethodException`

Returns the method on the object _target_ that matches the selector. If _target_ has no method that matches the selector, this method throws NoSuchMethodException.

---

### name

`public String name()`

Returns the name of the method specified by the selector.

---

### parameterTypes

`public Class[] parameterTypes()`

Copies and returns the array of parameter types specified by the selector.

---

### toString

`public String toString()`

Returns a string representation of the receiver indicating its class and method name.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
