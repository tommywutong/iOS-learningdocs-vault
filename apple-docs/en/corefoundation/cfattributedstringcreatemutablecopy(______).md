---
title: 'CFAttributedStringCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringcreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringcreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8cc8fe01f691df82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a mutable copy of an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringCreateMutableCopy(_ alloc: CFAllocator!, _ maxLength: CFIndex, _ aStr: CFAttributedString!) -> CFMutableAttributedString!
```

## Parameters

- `alloc` — The allocator to be used to allocate memory for the new attributed string. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `maxLength` — The limit on the length of the new attributed string. The string starts empty and can grow to this length (it can be shorter). Pass `0` to specify that the maximum length is not limited. If non-`0`, `maxLength` must be greater than or equal to the length of `aStr`.

- `aStr` — The attributed string to copy.

## Return Value

A mutable copy of `aStr`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a CFMutableAttributedString

- [CFAttributedStringCreateMutable](<cfattributedstringcreatemutable(____).md>) — Creates a mutable attributed string.
