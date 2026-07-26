---
title: 'object_setIvar(_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_setivar(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_setivar(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_setivar%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:327eab2b5fddb0b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_setIvar(_:_:_:)

<sub>Function</sub>

Sets the value of an instance variable in an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_setIvar(_ obj: Any?, _ ivar: Ivar, _ value: Any?)
```

## Parameters

- `obj` — The object containing the instance variable whose value you want to set.

- `ivar` — The Ivar describing the instance variable whose value you want to set.

- `value` — The new value for the instance variable.

## Discussion

[object_setIvar](<object_setivar(______).md>) is faster than [object_setInstanceVariable](object_setinstancevariable.md) if the Ivar for the instance variable is already known.

## See Also

### Working with Instances

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.
