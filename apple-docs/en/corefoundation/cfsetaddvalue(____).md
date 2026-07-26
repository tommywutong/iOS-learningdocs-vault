---
title: 'CFSetAddValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetaddvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetaddvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetaddvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:cf8c94a55622ff49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetAddValue(_:_:)

<sub>Function</sub>

Adds a value to a CFMutableSet object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetAddValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theSet` — The set to modify.

- `value` — A CFType object or a pointer value to add to `theSet` (or the value itself, if it fits into the size of a pointer). `value` is retained by `theSet` using the retain callback provided when `theSet` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. If `value` already exists in the collection, this function returns without doing anything.

## See Also

### CFMutableSet Miscellaneous Functions

- [CFSetCreateMutable](<cfsetcreatemutable(______).md>) — Creates an empty CFMutableSet object.
- [CFSetCreateMutableCopy](<cfsetcreatemutablecopy(______).md>) — Creates a new mutable set with the values from another set.
- [CFSetRemoveAllValues](<cfsetremoveallvalues(__).md>) — Removes all values from a CFMutableSet object.
- [CFSetRemoveValue](<cfsetremovevalue(____).md>) — Removes a value from a CFMutableSet object.
- [CFSetReplaceValue](<cfsetreplacevalue(____).md>) — Replaces a value in a CFMutableSet object.
- [CFSetSetValue](<cfsetsetvalue(____).md>) — Sets a value in a CFMutableSet object.
