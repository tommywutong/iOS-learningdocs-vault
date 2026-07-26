---
title: 'object_getIndexedIvars(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getindexedivars(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getindexedivars(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getindexedivars%28_%3A%29.json'
content_hash: 'sha256:1899b7587dbc2f92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getIndexedIvars(_:)

<sub>Function</sub>

Returns a pointer to any extra bytes allocated with a instance given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getIndexedIvars(_ obj: Any?) -> UnsafeMutableRawPointer?
```

## Parameters

- `obj` — An Objective-C object.

## Return Value

A pointer to any extra bytes allocated with `obj`. If `obj` was not allocated with any extra bytes, then dereferencing the returned pointer is undefined.

## Discussion

This function returns a pointer to any extra bytes allocated with the instance (as specified by [class_createInstance](<class_createinstance(____).md>) with extraBytes\>0). This memory follows the object’s ordinary ivars, but may not be adjacent to the last ivar.

The returned pointer is guaranteed to be pointer-size aligned, even if the area following the object’s last ivar is less aligned than that. Alignment greater than pointer-size is never guaranteed, even if the area following the object’s last ivar is more aligned than that.

In a garbage-collected environment, the memory is scanned conservatively.

## See Also

### Working with Instances

- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.
