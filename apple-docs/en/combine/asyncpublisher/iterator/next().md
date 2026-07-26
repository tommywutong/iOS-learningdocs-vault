---
title: next()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/asyncpublisher/iterator/next()
source_url: 'https://developer.apple.com/documentation/combine/asyncpublisher/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncpublisher/iterator/next%28%29.json'
content_hash: 'sha256:64cf165e30986833'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [AsyncPublisher](../../asyncpublisher.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the prefix sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async -> P.Output?
```

## Return Value

The next published element, or nil if the publisher finishes normally.
