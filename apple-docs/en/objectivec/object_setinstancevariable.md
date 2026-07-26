---
title: object_setInstanceVariable
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/object_setinstancevariable
source_url: 'https://developer.apple.com/documentation/objectivec/object_setinstancevariable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_setinstancevariable.json'
content_hash: 'sha256:af86731e08ad5f9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_setInstanceVariable

<sub>Function</sub>

Changes the value of an instance variable of a class instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern Ivarobject_setInstanceVariable(id obj, const char *name, void *value);
```

## Parameters

- `obj` — A pointer to an instance of a class. Pass the object containing the instance variable whose value you wish to modify.

- `name` — A C string. Pass the name of the instance variable whose value you wish to modify.

- `value` — The new value for the instance variable.

## Return Value

A pointer to the [Ivar](ivar.md) data structure that defines the type and name of the instance variable specified by `name`.

## See Also

### Working with Instances

- [object_copy](object_copy.md) — Returns a copy of a given object.
- [object_dispose](object_dispose.md) — Frees the memory occupied by a given object.
- [object_getInstanceVariable](object_getinstancevariable.md) — Obtains the value of an instance variable of a class instance.
- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.
