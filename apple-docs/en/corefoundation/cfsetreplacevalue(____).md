---
title: 'CFSetReplaceValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetreplacevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetreplacevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetreplacevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:8fe7cdb7154b5db0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetReplaceValue(_:_:)

<sub>Function</sub>

Replaces a value in a CFMutableSet object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetReplaceValue(_ theSet: CFMutableSet!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theSet` — The set to modify.

- `value` — The value to replace in `theSet`. If this value does not already exist in `theSet`, the function does nothing. You may pass the value itself instead of a pointer if it is pointer-size or less. The equal callback provided when `theSet` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theSet`, is not understood by the equal callback, the behavior is undefined.

## See Also

### CFMutableSet Miscellaneous Functions

- [CFSetAddValue](<cfsetaddvalue(____).md>) — Adds a value to a CFMutableSet object.
- [CFSetCreateMutable](<cfsetcreatemutable(______).md>) — Creates an empty CFMutableSet object.
- [CFSetCreateMutableCopy](<cfsetcreatemutablecopy(______).md>) — Creates a new mutable set with the values from another set.
- [CFSetRemoveAllValues](<cfsetremoveallvalues(__).md>) — Removes all values from a CFMutableSet object.
- [CFSetRemoveValue](<cfsetremovevalue(____).md>) — Removes a value from a CFMutableSet object.
- [CFSetSetValue](<cfsetsetvalue(____).md>) — Sets a value in a CFMutableSet object.
