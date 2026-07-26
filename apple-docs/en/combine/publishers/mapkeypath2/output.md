---
title: Publishers.MapKeyPath2.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/mapkeypath2/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/mapkeypath2/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mapkeypath2/output.json'
content_hash: 'sha256:0196e4ffac360968'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MapKeyPath2](../mapkeypath2.md)

# Publishers.MapKeyPath2.Output

<sub>Type Alias</sub>

The kind of values published by this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Output = (Output0, Output1)
```

## Discussion

This publisher produces two-element tuples, where each menber’s type matches the type of the corresponding key path’s property.

## See Also

### Declaring supporting types

- [Failure](failure.md) — The kind of errors this publisher might publish.
