---
title: 'class_copyProtocolList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_copyprotocollist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_copyprotocollist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_copyprotocollist%28_%3A_%3A%29.json'
content_hash: 'sha256:8904dd497d727199'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_copyProtocolList(_:_:)

<sub>Function</sub>

Describes the protocols adopted by a class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_copyProtocolList(_ cls: AnyClass?, _ outCount: UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?
```

## Parameters

- `cls` — The class you want to inspect.

- `outCount` — On return, contains the length of the returned array. If `outCount` is `NULL`, the length is not returned.

## Return Value

An array of pointers of type `Protocol*` describing the protocols adopted by the class. Any protocols adopted by superclasses or other protocols are not included. The array contains `*outCount` pointers followed by a `NULL` terminator. You must free the array with `free()`.

If `cls` adopts no protocols, or `cls` is `Nil`, returns `NULL` and `*outCount` is `0`.

## See Also

### Working with Classes

- [class_getName](<class_getname(__).md>) — Returns the name of a class.
- [class_getSuperclass](<class_getsuperclass(__).md>) — Returns the superclass of a class.
- [class_setSuperclass](<class_setsuperclass(____).md>) — Sets the superclass of a given class. _(deprecated)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — Returns a Boolean value that indicates whether a class object is a metaclass.
- [class_getInstanceSize](<class_getinstancesize(__).md>) — Returns the size of instances of a class.
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — Returns the `Ivar` for a specified instance variable of a given class.
- [class_getClassVariable](<class_getclassvariable(____).md>) — Returns the `Ivar` for a specified class variable of a given class.
- [class_addIvar](<class_addivar(__________).md>) — Adds a new instance variable to a class.
- [class_copyIvarList](<class_copyivarlist(____).md>) — Describes the instance variables declared by a class.
- [class_getIvarLayout](<class_getivarlayout(__).md>) — Returns a description of the `Ivar` layout for a given class.
- [class_setIvarLayout](<class_setivarlayout(____).md>) — Sets the `Ivar` layout for a given class.
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — Returns a description of the layout of weak `Ivar`s for a given class.
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — Sets the layout for weak `Ivar`s for a given class.
- [class_getProperty](<class_getproperty(____).md>) — Returns a property with a given name of a given class.
- [class_copyPropertyList](<class_copypropertylist(____).md>) — Describes the properties declared by a class.
