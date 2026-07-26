---
title: 'object_setClass(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_setclass(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_setclass(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_setclass%28_%3A_%3A%29.json'
content_hash: 'sha256:60a48a9a2c0d943b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_setClass(_:_:)

<sub>Function</sub>

Sets the class of an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_setClass(_ obj: Any?, _ cls: AnyClass) -> AnyClass?
```

## Parameters

- `obj` — The object to modify.

- `cls` — A class object.

## Return Value

The previous value of `object`’s class, or `Nil` if `object` is `nil`.

## See Also

### Working with Instances

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
