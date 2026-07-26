---
title: 'ivar_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/ivar_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/ivar_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/ivar_getname%28_%3A%29.json'
content_hash: 'sha256:a30f8e985fd44460'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# ivar_getName(_:)

<sub>Function</sub>

Returns the name of an instance variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ivar_getName(_ v: Ivar) -> UnsafePointer<CChar>?
```

## Return Value

A C string containing the instance variable’s name.

## See Also

### Working with Instance Variables

- [ivar_getTypeEncoding](<ivar_gettypeencoding(__).md>) — Returns the type string of an instance variable.
- [ivar_getOffset](<ivar_getoffset(__).md>) — Returns the offset of an instance variable.
