---
title: 'init(bytesNoCopy:deallocator:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/init(bytesnocopy:deallocator:)-vfoe'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytesnocopy:deallocator:)-vfoe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/init%28bytesnocopy%3Adeallocator%3A%29-vfoe.json'
content_hash: 'sha256:a949cec4016854e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# init(bytesNoCopy:deallocator:)

<sub>Initializer</sub>

Creates a new dispatch data object using the specified memory buffer and deallocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytesNoCopy bytes: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator = .free)
```

## Parameters

- `bytes` — A contiguous buffer of memory containing the initial data.

- `deallocator` — The deallocator responsible for releasing the memory associated with the data object. For a list of possible options, see [Deallocator](deallocator.md).

## See Also

### Creating a Dispatch Data Structure

- [init(bytes:)](<init(bytes_)-9lrd.md>) — Creates a new dispatch data object from the specified memory buffer.
- [withUnsafeBytes(body:)](<withunsafebytes(body_).md>)
- [Deallocator](deallocator.md) — Memory deallocators for dispatch data objects.
- [empty](empty.md) — A dispatch data object representing a zero-length memory region.
