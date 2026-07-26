---
title: Publishers.CollectByTime.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/collectbytime/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbytime/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbytime/output.json'
content_hash: 'sha256:3e597a50654fcbd6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CollectByTime](../collectbytime.md)

# Publishers.CollectByTime.Output

<sub>Type Alias</sub>

The kind of values published by this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Output = [Upstream.Output]
```

## Discussion

This publisher publishes arrays of its upstream publisher’s output type.

## See Also

### Declaring supporting types

- [Failure](failure.md) — The kind of errors this publisher might publish.
