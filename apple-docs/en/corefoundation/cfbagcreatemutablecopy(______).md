---
title: 'CFBagCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagcreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:814f00d0b22d8e54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a new mutable bag with the values from another bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theBag: CFBag!) -> CFMutableBag!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new bag and its storage for values. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new bag. The bag starts with the same count as `theBag`, and can grow to this number of values (and it can have less). If this value is `0`, the bag’s maximum capacity is not limited. This value must be greater than or equal to the count of `theBag`, and must not be negative.

- `theBag` — The bag to copy. The pointer values from `theBag` are copied into the new bag. However, the values are also retained by the new bag. The count of the new bag is the same as the count of `theBag`. The new bag uses the same callbacks as `theBag`.

## Return Value

A new mutable bag that contains the same values as `theBag`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Mutable Bag

- [CFBagCreateMutable](<cfbagcreatemutable(______).md>) — Creates a new empty mutable bag.
