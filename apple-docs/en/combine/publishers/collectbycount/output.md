---
title: Publishers.CollectByCount.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/collectbycount/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbycount/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbycount/output.json'
content_hash: 'sha256:05e32f5d38440c8e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CollectByCount](../collectbycount.md)

# Publishers.CollectByCount.Output

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
