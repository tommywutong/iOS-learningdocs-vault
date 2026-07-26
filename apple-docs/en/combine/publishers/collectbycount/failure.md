---
title: Publishers.CollectByCount.Failure
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/collectbycount/failure
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbycount/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbycount/failure.json'
content_hash: 'sha256:0e7326ebca3661d7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CollectByCount](../collectbycount.md)

# Publishers.CollectByCount.Failure

<sub>Type Alias</sub>

The kind of errors this publisher might publish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = Upstream.Failure
```

## Discussion

This publisher uses its upstream publisher’s failure type.

## See Also

### Declaring supporting types

- [Output](output.md) — The kind of values published by this publisher.
