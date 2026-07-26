---
title: 'CFBagCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagcreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:8574749ad5286446'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagCreateCopy(_:_:)

<sub>Function</sub>

Creates an immutable bag with the values of another bag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagCreateCopy(_ allocator: CFAllocator!, _ theBag: CFBag!) -> CFBag!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new bag and its storage for values. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theBag` — The bag to copy. The pointer values from `theBag` are copied into the new bag. However, the values are also retained by the new bag. The count of the new bag is the same as the count of `theBag`. The new bag uses the same callbacks as `theBag`.

## Return Value

A new bag that contains the same values as `theBag`, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Bag

- [CFBagCreate](<cfbagcreate(________).md>) — Creates an immutable bag containing specified values.
