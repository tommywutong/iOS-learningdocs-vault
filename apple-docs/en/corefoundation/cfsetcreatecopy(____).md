---
title: 'CFSetCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetcreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:98154d7e09ea8c47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetCreateCopy(_:_:)

<sub>Function</sub>

Creates an immutable set containing the values of an existing set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetCreateCopy(_ allocator: CFAllocator!, _ theSet: CFSet!) -> CFSet!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new set and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theSet` — The set to copy.

## Return Value

A new set that contains the same values as `theSet`, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The pointer values from `theSet` are copied into the new set, and the values are retained by the new set. The count of the new set is the same as the count of `theSet`. The new set uses the same callbacks as `theSet`.

## See Also

### Creating Sets

- [CFSetCreate](<cfsetcreate(________).md>) — Creates an immutable CFSet object containing supplied values.
