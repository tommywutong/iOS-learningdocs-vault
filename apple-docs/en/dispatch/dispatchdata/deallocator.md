---
title: DispatchData.Deallocator
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchdata/deallocator
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/deallocator.json'
content_hash: 'sha256:c6e08329e385cb78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# DispatchData.Deallocator

<sub>Enumeration</sub>

Memory deallocators for dispatch data objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Deallocator
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Deallocators

- [DispatchData.Deallocator.free](deallocator/free.md) — Use `free` to deallocate memory.
- [DispatchData.Deallocator.unmap](deallocator/unmap.md) — Use `munmap` to deallocate memory.
- [DispatchData.Deallocator.custom(_:_:)](<deallocator/custom(____).md>) — Use a custom deallocator.

## See Also

### Creating a Dispatch Data Structure

- [init(bytes:)](<init(bytes_)-9lrd.md>) — Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-vfoe.md>) — Creates a new dispatch data object using the specified memory buffer and deallocator.
- [withUnsafeBytes(body:)](<withunsafebytes(body_).md>)
- [empty](empty.md) — A dispatch data object representing a zero-length memory region.
