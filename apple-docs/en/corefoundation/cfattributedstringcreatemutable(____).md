---
title: 'CFAttributedStringCreateMutable(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringcreatemutable(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatemutable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringcreatemutable%28_%3A_%3A%29.json'
content_hash: 'sha256:212ce63de8190cf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringCreateMutable(_:_:)

<sub>Function</sub>

Creates a mutable attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringCreateMutable(_ alloc: CFAllocator!, _ maxLength: CFIndex) -> CFMutableAttributedString!
```

## Parameters

- `alloc` — An allocator to be used to allocate memory for the new attributed string. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `maxLength` — The limit on the length of the new attributed string. The string starts empty and can grow to this length (it can be shorter). Pass `0` to specify that the maximum length is not limited. The value must not be negative.

## Return Value

A new mutable attributed string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a CFMutableAttributedString

- [CFAttributedStringCreateMutableCopy](<cfattributedstringcreatemutablecopy(______).md>) — Creates a mutable copy of an attributed string.
