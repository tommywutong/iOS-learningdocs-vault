---
title: 'init(upstream:isIncluded:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/tryfilter/init(upstream:isincluded:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryfilter/init(upstream:isincluded:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryfilter/init%28upstream%3Aisincluded%3A%29.json'
content_hash: 'sha256:6018e6f61f93a65a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryFilter](../tryfilter.md)

# init(upstream:isIncluded:)

<sub>Initializer</sub>

Creates a publisher that republishes all elements that match a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, isIncluded: @escaping (Upstream.Output) throws -> Bool)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `isIncluded` — An error-throwing closure that indicates whether this filter should republish an element.
