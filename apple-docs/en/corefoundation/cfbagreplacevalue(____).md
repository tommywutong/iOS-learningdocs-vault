---
title: 'CFBagReplaceValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagreplacevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagreplacevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagreplacevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:dcfe25b04d3ca8b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagReplaceValue(_:_:)

<sub>Function</sub>

Replaces a value in a mutable bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagReplaceValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theBag` — The bag from which `value` is to be replaced.

- `value` — The value to be replaced in the collection. If this value does not already exist in the collection, the function does nothing. You may pass the value itself instead of a pointer if it is pointer-size or less. The equal callback provided when `theBag` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theBag`, is not understood by the equal callback, the behavior is undefined.

## Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the object that is replaced by `value` may not have the same pointer equality.

## See Also

### Modifying a Mutable Bag

- [CFBagAddValue](<cfbagaddvalue(____).md>) — Adds a value to a mutable bag.
- [CFBagRemoveAllValues](<cfbagremoveallvalues(__).md>) — Removes all values from a mutable bag.
- [CFBagRemoveValue](<cfbagremovevalue(____).md>) — Removes a value from a mutable bag.
- [CFBagSetValue](<cfbagsetvalue(____).md>) — Sets a value in a mutable bag.
