---
title: 'objc_getRequiredClass(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getrequiredclass(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getrequiredclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getrequiredclass%28_%3A%29.json'
content_hash: 'sha256:17c4dad12acef49b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getRequiredClass(_:)

<sub>Function</sub>

Returns the class definition of a specified class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getRequiredClass(_ name: UnsafePointer<CChar>) -> AnyClass
```

## Parameters

- `name` — The name of the class to look up.

## Return Value

The Class object for the named class.

## Discussion

This function is the same as [objc_getClass](<objc_getclass(__).md>), but kills the process if the class is not found.

This function is used by ZeroLink, where failing to find a class would be a compile-time link error without ZeroLink.

## See Also

### Obtaining Class Definitions

- [objc_getClassList](<objc_getclasslist(____).md>) — Obtains the list of registered class definitions.
- [objc_copyClassList](<objc_copyclasslist(__).md>) — Creates and returns a list of pointers to all registered class definitions.
- [objc_lookUpClass](<objc_lookupclass(__).md>) — Returns the class definition of a specified class.
- [objc_getClass](<objc_getclass(__).md>) — Returns the class definition of a specified class.
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — Returns the metaclass definition of a specified class.
