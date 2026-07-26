---
title: 'withUnsafeBytes(body:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/withunsafebytes(body:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/withunsafebytes(body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/withunsafebytes%28body%3A%29.json'
content_hash: 'sha256:258a0f4ae5078ec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# withUnsafeBytes(body:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result
```

## See Also

### Creating a Dispatch Data Structure

- [init(bytes:)](<init(bytes_)-9lrd.md>) — Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-vfoe.md>) — Creates a new dispatch data object using the specified memory buffer and deallocator.
- [Deallocator](deallocator.md) — Memory deallocators for dispatch data objects.
- [empty](empty.md) — A dispatch data object representing a zero-length memory region.
