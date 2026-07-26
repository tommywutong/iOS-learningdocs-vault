---
title: object_copy
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/object_copy
source_url: 'https://developer.apple.com/documentation/objectivec/object_copy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_copy.json'
content_hash: 'sha256:daddd602791a428d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_copy

<sub>Function</sub>

Returns a copy of a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern idobject_copy(id obj, size_t size);
```

## Parameters

- `obj` — An Objective-C object.

- `size` — The size of the object `obj`.

## Return Value

A copy of `obj`.

## See Also

### Working with Instances

- [object_dispose](object_dispose.md) — Frees the memory occupied by a given object.
- [object_setInstanceVariable](object_setinstancevariable.md) — Changes the value of an instance variable of a class instance.
- [object_getInstanceVariable](object_getinstancevariable.md) — Obtains the value of an instance variable of a class instance.
- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.
