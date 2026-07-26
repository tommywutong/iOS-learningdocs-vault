---
title: 'init(bytes:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/init(bytes:)-9lrd'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytes:)-9lrd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/init%28bytes%3A%29-9lrd.json'
content_hash: 'sha256:42235179a424aa34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# init(bytes:)

<sub>Initializer</sub>

Creates a new dispatch data object from the specified memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytes buffer: UnsafeRawBufferPointer)
```

## Parameters

- `buffer` — A contiguous buffer of memory containing the initial data.

## See Also

### Creating a Dispatch Data Structure

- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-vfoe.md>) — Creates a new dispatch data object using the specified memory buffer and deallocator.
- [withUnsafeBytes(body:)](<withunsafebytes(body_).md>)
- [Deallocator](deallocator.md) — Memory deallocators for dispatch data objects.
- [empty](empty.md) — A dispatch data object representing a zero-length memory region.
