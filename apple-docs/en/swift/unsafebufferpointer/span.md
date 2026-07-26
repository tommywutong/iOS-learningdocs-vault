---
title: span
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafebufferpointer/span
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/span.json'
content_hash: 'sha256:211ccaeca496efac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# span

<sub>Instance Property</sub>

A span over the elements of this buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var span: Span<Element> { get }
```

## Return Value

A `Span` over the elements of this buffer.

## Discussion

The lifetime of the returned span matches the lifetime of the binding which returns it. This lifetime is a convenience, as there can be no enforcement that there is no concurrent write to the underlying memory. The programmer must ensure that the memory remains allocated, initialized and immutable for the lifetime of the returned span.

> [!note] Note
> This property is unsafe because it cannot guarantee that the underlying memory remains valid and immutable for the lifetime of the returned span.

> [!abstract] Complexity
> O(1)
