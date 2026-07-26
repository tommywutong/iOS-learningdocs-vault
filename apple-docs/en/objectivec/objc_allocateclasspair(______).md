---
title: 'objc_allocateClassPair(_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_allocateclasspair(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_allocateclasspair(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_allocateclasspair%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8a602261667470d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_allocateClassPair(_:_:_:)

<sub>Function</sub>

Creates a new class and metaclass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_allocateClassPair(_ superclass: AnyClass?, _ name: UnsafePointer<CChar>, _ extraBytes: Int) -> AnyClass?
```

## Parameters

- `superclass` — The class to use as the new class’s superclass, or `Nil` to create a new root class.

- `name` — The string to use as the new class’s name. The string will be copied.

- `extraBytes` — The number of bytes to allocate for indexed ivars at the end of the class and metaclass objects. This should usually be `0`.

## Return Value

The new class, or `Nil` if the class could not be created (for example, the desired name is already in use).

## Discussion

You can get a pointer to the new metaclass by calling `object_getClass(newClass)`.

To create a new class, start by calling [objc_allocateClassPair](<objc_allocateclasspair(______).md>). Then set the class’s attributes with functions like [class_addMethod](<class_addmethod(________).md>) and [class_addIvar](<class_addivar(__________).md>). When you are done building the class, call [objc_registerClassPair](<objc_registerclasspair(__).md>). The new class is now ready for use.

Instance methods and instance variables should be added to the class itself. Class methods should be added to the metaclass.

## See Also

### Adding Classes

- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — Destroys a class and its associated metaclass.
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — Registers a class that was allocated using [objc_allocateClassPair](<objc_allocateclasspair(______).md>).
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — Used by Foundation’s Key-Value Observing.
