---
title: 'init(upstream:initialResult:nextPartialResult:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/scan/init(upstream:initialresult:nextpartialresult:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/scan/init(upstream:initialresult:nextpartialresult:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/scan/init%28upstream%3Ainitialresult%3Anextpartialresult%3A%29.json'
content_hash: 'sha256:4e4ae4d6eda2f8c1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Scan](../scan.md)

# init(upstream:initialResult:nextPartialResult:)

<sub>Initializer</sub>

Creates a publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, initialResult: Output, nextPartialResult: @escaping (Output, Upstream.Output) -> Output)
```

## Parameters

- `upstream` — The publisher that this publisher receives elements from.

- `initialResult` — The previous result returned by the `nextPartialResult` closure.

- `nextPartialResult` — A closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.
