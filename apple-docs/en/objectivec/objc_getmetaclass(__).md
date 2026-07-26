---
title: 'objc_getMetaClass(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getmetaclass(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getmetaclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getmetaclass%28_%3A%29.json'
content_hash: 'sha256:695afbd0603f0a8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getMetaClass(_:)

<sub>Function</sub>

Returns the metaclass definition of a specified class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getMetaClass(_ name: UnsafePointer<CChar>) -> Any!
```

## Parameters

- `name` — The name of the class to look up.

## Return Value

The `Class` object for the metaclass of the named class, or `nil` if the class is not registered with the Objective-C runtime.

## Discussion

If the definition for the named class is not registered, this function calls the class handler callback and then checks a second time to see if the class is registered. However, every class definition must have a valid metaclass definition, and so the metaclass definition is always returned, whether it’s valid or not.

## See Also

### Obtaining Class Definitions

- [objc_getClassList](<objc_getclasslist(____).md>) — Obtains the list of registered class definitions.
- [objc_copyClassList](<objc_copyclasslist(__).md>) — Creates and returns a list of pointers to all registered class definitions.
- [objc_lookUpClass](<objc_lookupclass(__).md>) — Returns the class definition of a specified class.
- [objc_getClass](<objc_getclass(__).md>) — Returns the class definition of a specified class.
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — Returns the class definition of a specified class.
