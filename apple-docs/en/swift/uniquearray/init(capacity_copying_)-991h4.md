---
title: 'init(capacity:copying:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/init(capacity:copying:)-991h4'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/init(capacity:copying:)-991h4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/init%28capacity%3Acopying%3A%29-991h4.json'
content_hash: 'sha256:d83abdc3378f6fec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# init(capacity:copying:)

<sub>Initializer</sub>

Creates a new array with the specified capacity, holding a copy of the contents of the given span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity: Int? = nil, copying span: Span<Element>)
```

## Parameters

- `capacity` — The storage capacity of the new array, or nil to allocate just enough capacity to store the contents of the span.

- `span` — The span whose contents to copy into the new array. The span must not contain more than `capacity` elements.
