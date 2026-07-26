---
title: 'objc_copyClassList(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_copyclasslist(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyclasslist(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyclasslist%28_%3A%29.json'
content_hash: 'sha256:0a1bcc30c935ccea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyClassList(_:)

<sub>Function</sub>

Creates and returns a list of pointers to all registered class definitions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyClassList(_ outCount: UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<AnyClass>?
```

## Parameters

- `outCount` — An integer pointer used to store the number of classes returned by this function in the list. This parameter may be `nil`.

## Return Value

A `nil` terminated array of classes. You must free the array with `free()`.

## See Also

### Obtaining Class Definitions

- [objc_getClassList](<objc_getclasslist(____).md>) — Obtains the list of registered class definitions.
- [objc_lookUpClass](<objc_lookupclass(__).md>) — Returns the class definition of a specified class.
- [objc_getClass](<objc_getclass(__).md>) — Returns the class definition of a specified class.
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — Returns the class definition of a specified class.
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — Returns the metaclass definition of a specified class.
