---
title: 'init(upstream:output:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/replaceerror/init(upstream:output:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/replaceerror/init(upstream:output:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/replaceerror/init%28upstream%3Aoutput%3A%29.json'
content_hash: 'sha256:f2beb6f58e099932'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [ReplaceError](../replaceerror.md)

# init(upstream:output:)

<sub>Initializer</sub>

Creates a publisher that replaces any errors in the stream with a provided element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, output: Publishers.ReplaceError<Upstream>.Output)
```

## Parameters

- `upstream` — The element with which to replace errors from the upstream publisher.

- `output` — The publisher from which this publisher receives elements.
