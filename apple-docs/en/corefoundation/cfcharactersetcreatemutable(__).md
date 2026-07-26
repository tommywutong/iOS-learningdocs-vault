---
title: 'CFCharacterSetCreateMutable(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreatemutable(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatemutable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreatemutable%28_%3A%29.json'
content_hash: 'sha256:5e2819a46b463fe0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateMutable(_:)

<sub>Function</sub>

Creates a new empty mutable character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateMutable(_ alloc: CFAllocator!) -> CFMutableCharacterSet!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

## Return Value

A new empty mutable character set. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Mutable Character Set

- [CFCharacterSetCreateMutableCopy](<cfcharactersetcreatemutablecopy(____).md>) — Creates a new mutable character set with the values from another character set.
