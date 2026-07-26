---
title: Publishers.Autoconnect.Failure
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/autoconnect/failure
source_url: 'https://developer.apple.com/documentation/combine/publishers/autoconnect/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/autoconnect/failure.json'
content_hash: 'sha256:83e44a6c2c4650fa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Autoconnect](../autoconnect.md)

# Publishers.Autoconnect.Failure

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
