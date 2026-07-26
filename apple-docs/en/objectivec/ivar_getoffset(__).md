---
title: 'ivar_getOffset(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/ivar_getoffset(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/ivar_getoffset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/ivar_getoffset%28_%3A%29.json'
content_hash: 'sha256:7721a32aafc6e319'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# ivar_getOffset(_:)

<sub>Function</sub>

Returns the offset of an instance variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ivar_getOffset(_ v: Ivar) -> Int
```

## Discussion

For instance variables of type `id` or other object types, call [object_getIvar](<object_getivar(____).md>) and [object_setIvar](<object_setivar(______).md>) instead of using this offset to access the instance variable data directly.

## See Also

### Working with Instance Variables

- [ivar_getName](<ivar_getname(__).md>) — Returns the name of an instance variable.
- [ivar_getTypeEncoding](<ivar_gettypeencoding(__).md>) — Returns the type string of an instance variable.
