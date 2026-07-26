---
title: 'CFUUIDCreateString(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfuuidcreatestring(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuidcreatestring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuidcreatestring%28_%3A_%3A%29.json'
content_hash: 'sha256:38de673b1e5d0727'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUIDCreateString(_:_:)

<sub>Function</sub>

Returns the string representation of a specified CFUUID object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFUUIDCreateString(_ alloc: CFAllocator!, _ uuid: CFUUID!) -> CFString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `uuid` — The CFUUID object whose string representation to obtain.

## Return Value

The string representation of `uuid`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting Information About CFUUID Objects

- [CFUUIDGetConstantUUIDWithBytes](<cfuuidgetconstantuuidwithbytes(__________________________________).md>) — Returns a CFUUID object from raw UUID bytes.
- [CFUUIDGetUUIDBytes](<cfuuidgetuuidbytes(__).md>) — Returns the value of a UUID object as raw bytes.
