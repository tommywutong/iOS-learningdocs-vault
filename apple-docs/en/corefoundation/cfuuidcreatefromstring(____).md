---
title: 'CFUUIDCreateFromString(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfuuidcreatefromstring(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuidcreatefromstring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuidcreatefromstring%28_%3A_%3A%29.json'
content_hash: 'sha256:a39e9c3836649578'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUIDCreateFromString(_:_:)

<sub>Function</sub>

Creates a CFUUID object for a specified string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFUUIDCreateFromString(_ alloc: CFAllocator!, _ uuidStr: CFString!) -> CFUUID!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `uuidStr` — A string containing a UUID. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`.

## Return Value

A new CFUUID object, or if a CFUUID object of the same value already exists, the existing instance with its reference count incremented. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating CFUUID Objects

- [CFUUIDCreate](<cfuuidcreate(__).md>) — Creates a Universally Unique Identifier (UUID) object.
- [CFUUIDCreateFromUUIDBytes](<cfuuidcreatefromuuidbytes(____).md>) — Creates a CFUUID object from raw UUID bytes.
- [CFUUIDCreateWithBytes](<cfuuidcreatewithbytes(__________________________________).md>) — Creates a CFUUID object from raw UUID bytes.
