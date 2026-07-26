---
title: 'CFSetCreateMutable(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetcreatemutable(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcreatemutable(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcreatemutable%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:33cac2c9f0aa3bd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetCreateMutable(_:_:_:)

<sub>Function</sub>

Creates an empty CFMutableSet object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new set and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new set. The set starts empty and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. The value must not be negative.

- `callBacks` — A pointer to a [CFSetCallBacks](cfsetcallbacks.md) structure initialized with the callbacks to use to retain, release, describe, and compare values in the set. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in or can be reused for multiple collection creations. This parameter may be `NULL`, which is treated as if a valid structure of version `0` with all fields `NULL` had been passed in. If any of the fields are not valid pointers to functions of the correct type, or this parameter is not a valid pointer to a `CFSetCallBacks` structure, the behavior is undefined. If any value put into the collection is not one understood by one of the callback functions, the behavior when that callback function is used is undefined. If the collection contains CFType objects only, then pass [kCFTypeSetCallBacks](kcftypesetcallbacks.md) as this parameter to use the default callback functions.

## Return Value

A new mutable set, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFMutableSet Miscellaneous Functions

- [CFSetAddValue](<cfsetaddvalue(____).md>) — Adds a value to a CFMutableSet object.
- [CFSetCreateMutableCopy](<cfsetcreatemutablecopy(______).md>) — Creates a new mutable set with the values from another set.
- [CFSetRemoveAllValues](<cfsetremoveallvalues(__).md>) — Removes all values from a CFMutableSet object.
- [CFSetRemoveValue](<cfsetremovevalue(____).md>) — Removes a value from a CFMutableSet object.
- [CFSetReplaceValue](<cfsetreplacevalue(____).md>) — Replaces a value in a CFMutableSet object.
- [CFSetSetValue](<cfsetsetvalue(____).md>) — Sets a value in a CFMutableSet object.
