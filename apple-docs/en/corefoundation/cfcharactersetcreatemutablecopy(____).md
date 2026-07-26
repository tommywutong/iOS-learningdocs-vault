---
title: 'CFCharacterSetCreateMutableCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreatemutablecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatemutablecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreatemutablecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:7b802effc12ab808'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateMutableCopy(_:_:)

<sub>Function</sub>

Creates a new mutable character set with the values from another character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateMutableCopy(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFMutableCharacterSet!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theSet` — The character set to copy.

## Return Value

A new mutable character set containing the same characters as `theSet`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Mutable Character Set

- [CFCharacterSetCreateMutable](<cfcharactersetcreatemutable(__).md>) — Creates a new empty mutable character set.
