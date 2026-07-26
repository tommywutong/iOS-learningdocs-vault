---
title: 'CFBagAddValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagaddvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagaddvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagaddvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:a14d3eb56d96dc34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagAddValue(_:_:)

<sub>Function</sub>

Adds a value to a mutable bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagAddValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theBag` — The bag to which `value` is added.

- `value` — A CFType object or a pointer value to add to `theBag` (or the value itself, if it fits into the size of a pointer).

## Discussion

The `value` parameter is retained by `theBag` using the retain callback provided when `theBag` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. If `value` already exists in the collection, it is simply retained again—no memory is allocated for the added value. Use a CFSet object if you don’t want duplicate values in your collection.

## See Also

### Modifying a Mutable Bag

- [CFBagRemoveAllValues](<cfbagremoveallvalues(__).md>) — Removes all values from a mutable bag.
- [CFBagRemoveValue](<cfbagremovevalue(____).md>) — Removes a value from a mutable bag.
- [CFBagReplaceValue](<cfbagreplacevalue(____).md>) — Replaces a value in a mutable bag.
- [CFBagSetValue](<cfbagsetvalue(____).md>) — Sets a value in a mutable bag.
