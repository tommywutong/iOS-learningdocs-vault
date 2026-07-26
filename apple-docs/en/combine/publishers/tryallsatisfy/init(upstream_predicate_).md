---
title: 'init(upstream:predicate:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/tryallsatisfy/init(upstream:predicate:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryallsatisfy/init(upstream:predicate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryallsatisfy/init%28upstream%3Apredicate%3A%29.json'
content_hash: 'sha256:c094c3ed6d18657a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryAllSatisfy](../tryallsatisfy.md)

# init(upstream:predicate:)

<sub>Initializer</sub>

Returns a publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, predicate: @escaping (Upstream.Output) throws -> Bool)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `predicate` — A closure that evaluates each received element.
