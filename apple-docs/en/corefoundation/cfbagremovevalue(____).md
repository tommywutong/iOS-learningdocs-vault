---
title: 'CFBagRemoveValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagremovevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagremovevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagremovevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:facc845c6d23a170'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagRemoveValue(_:_:)

<sub>Function</sub>

Removes a value from a mutable bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagRemoveValue(_ theBag: CFMutableBag!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theBag` — The bag from which `value` is to be removed.

- `value` — The value to be removed from the collection.

## See Also

### Modifying a Mutable Bag

- [CFBagAddValue](<cfbagaddvalue(____).md>) — Adds a value to a mutable bag.
- [CFBagRemoveAllValues](<cfbagremoveallvalues(__).md>) — Removes all values from a mutable bag.
- [CFBagReplaceValue](<cfbagreplacevalue(____).md>) — Replaces a value in a mutable bag.
- [CFBagSetValue](<cfbagsetvalue(____).md>) — Sets a value in a mutable bag.
