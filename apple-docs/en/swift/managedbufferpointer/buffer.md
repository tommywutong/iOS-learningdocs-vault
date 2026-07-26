---
title: buffer
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managedbufferpointer/buffer
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/buffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/buffer.json'
content_hash: 'sha256:e323b75003725d22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# buffer

<sub>Instance Property</sub>

Returns the object instance being used for storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var buffer: AnyObject { get }
```

## See Also

### Inspecting a Buffer

- [capacity](capacity.md) — The actual number of elements that can be stored in this object.
- [header](header.md) — The stored `Header` instance.
- [isUniqueReference()](<isuniquereference().md>) — Returns `true` if `self` holds the only strong reference to its buffer; otherwise, returns `false`.
