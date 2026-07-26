---
title: Publishers.FirstWhere.Failure
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/firstwhere/failure
source_url: 'https://developer.apple.com/documentation/combine/publishers/firstwhere/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/firstwhere/failure.json'
content_hash: 'sha256:a3f4f132229a37cc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [FirstWhere](../firstwhere.md)

# Publishers.FirstWhere.Failure

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
