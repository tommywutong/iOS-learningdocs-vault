---
title: 'method_exchangeImplementations(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/method_exchangeimplementations(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/method_exchangeimplementations(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_exchangeimplementations%28_%3A_%3A%29.json'
content_hash: 'sha256:51763c1fa8fd1f12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_exchangeImplementations(_:_:)

<sub>Function</sub>

Exchanges the implementations of two methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method_exchangeImplementations(_ m1: Method, _ m2: Method)
```

## Discussion

This is an atomic version of the following:

```objc
IMP imp1 = method_getImplementation(m1);
IMP imp2 = method_getImplementation(m2);
method_setImplementation(m1, imp2);
method_setImplementation(m2, imp1);
```

## See Also

### Working with Methods

- [method_getName](<method_getname(__).md>) — Returns the name of a method.
- [method_getImplementation](<method_getimplementation(__).md>) — Returns the implementation of a method.
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — Returns a string describing a method’s parameter and return types.
- [method_copyReturnType](<method_copyreturntype(__).md>) — Returns a string describing a method’s return type.
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — Returns a string describing a single parameter type of a method.
- [method_getReturnType](<method_getreturntype(______).md>) — Returns by reference a string describing a method’s return type.
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — Returns the number of arguments accepted by a method.
- [method_getArgumentType](<method_getargumenttype(________).md>) — Returns by reference a string describing a single parameter type of a method.
- [method_getDescription](<method_getdescription(__).md>) — Returns a method description structure for a specified method. _(deprecated)_
- [method_setImplementation](<method_setimplementation(____).md>) — Sets the implementation of a method.
