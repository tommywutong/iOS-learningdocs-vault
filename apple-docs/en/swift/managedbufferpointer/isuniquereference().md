---
title: isUniqueReference()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managedbufferpointer/isuniquereference()
source_url: 'https://developer.apple.com/documentation/swift/managedbufferpointer/isuniquereference()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managedbufferpointer/isuniquereference%28%29.json'
content_hash: 'sha256:1a14ea26d5364a44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ManagedBufferPointer](../managedbufferpointer.md)

# isUniqueReference()

<sub>Instance Method</sub>

Returns `true` if `self` holds the only strong reference to its buffer; otherwise, returns `false`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func isUniqueReference() -> Bool
```

## Discussion

See `isKnownUniquelyReferenced` for details.

## See Also

### Inspecting a Buffer

- [capacity](capacity.md) — The actual number of elements that can be stored in this object.
- [header](header.md) — The stored `Header` instance.
- [buffer](buffer.md) — Returns the object instance being used for storage.
