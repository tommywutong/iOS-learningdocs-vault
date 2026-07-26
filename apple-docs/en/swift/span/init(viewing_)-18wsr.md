---
title: 'init(viewing:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/span/init(viewing:)-18wsr'
source_url: 'https://developer.apple.com/documentation/swift/span/init(viewing:)-18wsr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/init%28viewing%3A%29-18wsr.json'
content_hash: 'sha256:60513625742a667c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# init(viewing:)

<sub>Initializer</sub>

View initialized raw memory as a typed span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(viewing bytes: RawSpan) where Element : ConvertibleFromBytes
```

## Parameters

- `bytes` — An existing `RawSpan`, which will define both this `Span`’s lifetime and the memory it represents.

## Discussion

The `byteCount` of `bytes` must be a multiple of `Element`’s stride, and the starting address of `bytes` must be well-aligned for the type of `Element`. If either of these requirements is not met, this initializer will trap at runtime.
