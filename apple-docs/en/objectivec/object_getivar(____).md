---
title: 'object_getIvar(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getivar(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getivar(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getivar%28_%3A_%3A%29.json'
content_hash: 'sha256:8f069ad76e9ed94f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getIvar(_:_:)

<sub>Function</sub>

Reads the value of an instance variable in an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getIvar(_ obj: Any?, _ ivar: Ivar) -> Any?
```

## Parameters

- `obj` — The object containing the instance variable whose value you want to read.

- `ivar` — The Ivar describing the instance variable whose value you want to read.

## Return Value

The value of the instance variable specified by `ivar`, or `nil` if `object` is `nil`.

## Discussion

[object_getIvar](<object_getivar(____).md>) is faster than [object_getInstanceVariable](object_getinstancevariable.md) if the Ivar for the instance variable is already known.

## See Also

### Working with Instances

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.
