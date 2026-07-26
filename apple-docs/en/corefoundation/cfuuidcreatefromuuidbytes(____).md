---
title: 'CFUUIDCreateFromUUIDBytes(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfuuidcreatefromuuidbytes(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuidcreatefromuuidbytes(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuidcreatefromuuidbytes%28_%3A_%3A%29.json'
content_hash: 'sha256:c86f8a482ecba4af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUIDCreateFromUUIDBytes(_:_:)

<sub>Function</sub>

Creates a CFUUID object from raw UUID bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFUUIDCreateFromUUIDBytes(_ alloc: CFAllocator!, _ bytes: CFUUIDBytes) -> CFUUID!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `bytes` — Raw UUID bytes to use to create the CFUUID object.

## Return Value

A new CFUUID object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating CFUUID Objects

- [CFUUIDCreate](<cfuuidcreate(__).md>) — Creates a Universally Unique Identifier (UUID) object.
- [CFUUIDCreateFromString](<cfuuidcreatefromstring(____).md>) — Creates a CFUUID object for a specified string.
- [CFUUIDCreateWithBytes](<cfuuidcreatewithbytes(__________________________________).md>) — Creates a CFUUID object from raw UUID bytes.
