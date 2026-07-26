---
title: Publishers.MergeMany.Failure
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/mergemany/failure
source_url: 'https://developer.apple.com/documentation/combine/publishers/mergemany/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mergemany/failure.json'
content_hash: 'sha256:4d4c29f7c51aa016'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MergeMany](../mergemany.md)

# Publishers.MergeMany.Failure

<sub>Type Alias</sub>

The kind of errors this publisher might publish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = Upstream.Failure
```

## Discussion

This publisher uses its upstream publishers’ common failure type.

## See Also

### Declaring supporting types

- [Output](output.md) — The kind of values published by this publisher.
