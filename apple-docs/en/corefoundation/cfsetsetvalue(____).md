---
title: 'CFSetSetValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetsetvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetsetvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetsetvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:a611c7a99a40e6fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetSetValue(_:_:)

<sub>Function</sub>

Sets a value in a CFMutableSet object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetSetValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theSet` — The set to modify.

- `value` — The value to be set in `theSet`. If this value already exists in `theSet`, it is replaced. You may pass the value itself instead of a pointer to it if the value is pointer-size or less. If `theSet` is fixed-size and setting the value would increase its size beyond its capacity, the behavior is undefined.

## Discussion

Depending on the implementation of the equal callback specified when creating `theSet`, the value that is replaced by `value` may not have the same pointer equality.

## See Also

### CFMutableSet Miscellaneous Functions

- [CFSetAddValue](<cfsetaddvalue(____).md>) — Adds a value to a CFMutableSet object.
- [CFSetCreateMutable](<cfsetcreatemutable(______).md>) — Creates an empty CFMutableSet object.
- [CFSetCreateMutableCopy](<cfsetcreatemutablecopy(______).md>) — Creates a new mutable set with the values from another set.
- [CFSetRemoveAllValues](<cfsetremoveallvalues(__).md>) — Removes all values from a CFMutableSet object.
- [CFSetRemoveValue](<cfsetremovevalue(____).md>) — Removes a value from a CFMutableSet object.
- [CFSetReplaceValue](<cfsetreplacevalue(____).md>) — Replaces a value in a CFMutableSet object.
