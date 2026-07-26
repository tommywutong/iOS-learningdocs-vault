---
title: Publishers.MapKeyPath3.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/mapkeypath3/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/mapkeypath3/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mapkeypath3/output.json'
content_hash: 'sha256:bdf5de97961c4273'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MapKeyPath3](../mapkeypath3.md)

# Publishers.MapKeyPath3.Output

<sub>Type Alias</sub>

The kind of values published by this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Output = (Output0, Output1, Output2)
```

## Discussion

This publisher produces three-element tuples, where each menber’s type matches the type of the corresponding key path’s property.

## See Also

### Declaring supporting types

- [Failure](failure.md) — The kind of errors this publisher might publish.
