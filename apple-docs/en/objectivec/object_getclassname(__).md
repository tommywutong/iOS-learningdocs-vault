---
title: 'object_getClassName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getclassname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getclassname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getclassname%28_%3A%29.json'
content_hash: 'sha256:a1951b234e25bda4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getClassName(_:)

<sub>Function</sub>

Returns the class name of a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getClassName(_ obj: Any?) -> UnsafePointer<CChar>
```

## Parameters

- `obj` — An Objective-C object.

## Return Value

The name of the class of which `obj` is an instance.

## See Also

### Working with Instances

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.
