---
title: capacity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managedbufferpointer/capacity
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/capacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/capacity.json'
content_hash: 'sha256:66eae225e1948d62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# capacity

<sub>Instance Property</sub>

The actual number of elements that can be stored in this object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var capacity: Int { get }
```

## Discussion

This value may be nontrivial to compute; it is usually a good idea to store this information in the “header” area when an instance is created.

## See Also

### Inspecting a Buffer

- [header](header.md) — The stored `Header` instance.
- [buffer](buffer.md) — Returns the object instance being used for storage.
- [isUniqueReference()](<isuniquereference().md>) — Returns `true` if `self` holds the only strong reference to its buffer; otherwise, returns `false`.
