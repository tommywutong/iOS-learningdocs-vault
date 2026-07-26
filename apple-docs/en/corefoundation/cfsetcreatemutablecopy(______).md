---
title: 'CFSetCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetcreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ed31716a274914cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a new mutable set with the values from another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theSet: CFSet!) -> CFMutableSet!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new set and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new set. The set starts with the same number of values as `theSet` and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the count of `theSet`.

- `theSet` — The set to copy. The pointer values from `theSet` are copied into the new set. The values are also retained by the new set. The count of the new set is the same as the count of `theSet`. The new set uses the same callbacks as `theSet`.

## Return Value

A new mutable set that contains the same values as `theSet`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFMutableSet Miscellaneous Functions

- [CFSetAddValue](<cfsetaddvalue(____).md>) — Adds a value to a CFMutableSet object.
- [CFSetCreateMutable](<cfsetcreatemutable(______).md>) — Creates an empty CFMutableSet object.
- [CFSetRemoveAllValues](<cfsetremoveallvalues(__).md>) — Removes all values from a CFMutableSet object.
- [CFSetRemoveValue](<cfsetremovevalue(____).md>) — Removes a value from a CFMutableSet object.
- [CFSetReplaceValue](<cfsetreplacevalue(____).md>) — Replaces a value in a CFMutableSet object.
- [CFSetSetValue](<cfsetsetvalue(____).md>) — Sets a value in a CFMutableSet object.
