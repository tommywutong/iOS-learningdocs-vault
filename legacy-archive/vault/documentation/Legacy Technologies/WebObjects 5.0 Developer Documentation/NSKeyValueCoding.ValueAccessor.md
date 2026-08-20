---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSKVCValAcc.html
archived_at: '2026-07-15T08:13:56.102086Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSKeyValueCoding.ValueAccessor

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSKeyValueCoding.ValueAccessor is an abstract class that establishes a mechanism by which [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) can operate on objects' package access instance variables.

By default, Foundation's implementations of [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu) can't access package access instance variables. If you have package access instance variables in your NSKeyValueCoding objects, you can make them available to key-value coding in one of the three ways:

- Implement public __set___Key_ and _key_ accessor methods for those instance variables that set and return the instance variables' values.
- Make the instance variables public.
- Add a subclass of NSKeyValueCoding.ValueAccessor named KeyValueCodingProtectedAccessor to your package. This class provides a mechanism to manipulate package access instance variables.

The best solution is to implement accessor methods or to make the instance variables public. However, if you have a lot of classes with a lot of package access instance variables, you can use the short-term solution that NSKeyValueCoding.ValueAccessor provides until you make the necessary changes to your code.

To use NSKeyValueCoding.ValueAccessor's mechanism, simply create a class in your package as follows:

> ```
> package yourPackage;
> import java.lang.reflect.*;
> import com.webobjects.foundation.*;
>
> public class KeyValueCodingProtectedAccessor extends NSKeyValueCoding.ValueAccessor {
>
>     public KeyValueCodingProtectedAccessor() {
>         super();
>     }
>
>     public Object fieldValue(Field field, Object object) throws
>     IllegalArgumentException, IllegalAccessException {
>         return field.get(object);
>     }
>
>     public void setFieldValue(Field field, Object value, Object object) throws
>     IllegalArgumentException, IllegalAccessException {
>         field.set(object, value);
>     }
>
>     public Object methodValue(Method method, Object object) throws
>     IllegalArgumentException, IllegalAccessException, InvocationTargetException {
>         return method.invoke(object, null);
>     }
>
>     public void setMethodValue(Method method, Object value, Object object) throws
>     IllegalArgumentException, IllegalAccessException, InvocationTargetException {
>         method.invoke(object, new Object[] {value});
>     }
> }
> ```

## Constructors

---

### NSKeyValueCoding.ValueAccessor

`public NSKeyValueCoding.ValueAccessor()`

The no-arg constructor. Don't use this method; because NSKeyValueCoding.ValueAccessor is an abstract class, you can never create an instance of it.

---

## Static Methods

---

### protectedAccessorForPackageNamed

`public static NSKeyValueCoding.ValueAccessor protectedAccessorForPackageNamed( String packageName)`

Returns the value accessor for the package identified by _packageName_.

---

### removeProtectedAccessorForPackageNamed

`public static void removeProtectedAccessorForPackageNamed( String packageName)`

Removes (unregisters) the value accessor for the package identified by _packageName_.

---

### setProtectedAccessorForPackageWithNamed

`public static void setProtectedAccessorForPackageNamed( NSKeyValueCoding.ValueAccessor accessor, String packageName)`

Sets the value accessor for the package identified by _packageName_ to _accessor_.

---

## Instance Methods

---

### fieldValue

`public abstract Object fieldValue( Object object, reflect.Field field) throws IllegalArgumentException, IllegalAccessException`

Returns the value of _object_'s _field_.

---

### methodValue

`public abstract Object methodValue( Object object, reflect.Method method) throws IllegalArgumentException, IllegalAccessException, reflect.InvocationTargetException`

Uses _method_ to return _object_'s corresponding property value.

---

### setFieldValue

`public abstract void setFieldValue( Object object, reflect.Field field, Object value) throws IllegalArgumentException, IllegalAccessException`

Sets _object_'s _field_ value to _value_.

---

### setMethodValue

`public abstract void setMethodValue( Object object, reflect.Method method, Object value) throws IllegalArgumentException, IllegalAccessException, reflect.InvocationTargetException`

Uses _method_ to set _object_'s corresponding property to _value_.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
