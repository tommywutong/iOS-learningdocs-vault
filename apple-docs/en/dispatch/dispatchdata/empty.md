---
title: empty
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchdata/empty
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/empty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/empty.json'
content_hash: 'sha256:e118a3f547c83769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# empty

<sub>Type Property</sub>

A dispatch data object representing a zero-length memory region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let empty: DispatchData
```

## See Also

### Creating a Dispatch Data Structure

- [init(bytes:)](<init(bytes_)-9lrd.md>) — Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-vfoe.md>) — Creates a new dispatch data object using the specified memory buffer and deallocator.
- [withUnsafeBytes(body:)](<withunsafebytes(body_).md>)
- [Deallocator](deallocator.md) — Memory deallocators for dispatch data objects.
