---
title: 'CFBagSetValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagsetvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagsetvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagsetvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:3a317c5af084b4ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagSetValue(_:_:)

<sub>Function</sub>

Sets a value in a mutable bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagSetValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theBag` — The bag in which `value` is to be set.

- `value` — The value to be set in the collection. If this value already exists in `theBag`, it is replaced. You may pass the value itself instead of a pointer to it if the value is pointer-size or less. If `theBag` is fixed-size and the value is beyond its capacity, the behavior is undefined.

## Discussion

Depending on the implementation of the equal callback specified when creating `theBag`, the value that is replaced by `value` may not have the same pointer equality.

## See Also

### Modifying a Mutable Bag

- [CFBagAddValue](<cfbagaddvalue(____).md>) — Adds a value to a mutable bag.
- [CFBagRemoveAllValues](<cfbagremoveallvalues(__).md>) — Removes all values from a mutable bag.
- [CFBagRemoveValue](<cfbagremovevalue(____).md>) — Removes a value from a mutable bag.
- [CFBagReplaceValue](<cfbagreplacevalue(____).md>) — Replaces a value in a mutable bag.
