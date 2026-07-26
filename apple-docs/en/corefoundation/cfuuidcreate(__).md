---
title: 'CFUUIDCreate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfuuidcreate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuidcreate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuidcreate%28_%3A%29.json'
content_hash: 'sha256:5a99fa44c8859928'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUIDCreate(_:)

<sub>Function</sub>

Creates a Universally Unique Identifier (UUID) object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFUUIDCreate(_ alloc: CFAllocator!) -> CFUUID!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

## Return Value

A new CFUUID object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating CFUUID Objects

- [CFUUIDCreateFromString](<cfuuidcreatefromstring(____).md>) — Creates a CFUUID object for a specified string.
- [CFUUIDCreateFromUUIDBytes](<cfuuidcreatefromuuidbytes(____).md>) — Creates a CFUUID object from raw UUID bytes.
- [CFUUIDCreateWithBytes](<cfuuidcreatewithbytes(__________________________________).md>) — Creates a CFUUID object from raw UUID bytes.
