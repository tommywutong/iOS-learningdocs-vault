---
title: 'init(upstream:initial:nextPartialResult:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/tryreduce/init(upstream:initial:nextpartialresult:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryreduce/init(upstream:initial:nextpartialresult:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryreduce/init%28upstream%3Ainitial%3Anextpartialresult%3A%29.json'
content_hash: 'sha256:11b12931cfaa3bf9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryReduce](../tryreduce.md)

# init(upstream:initial:nextPartialResult:)

<sub>Initializer</sub>

Creates a publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, initial: Output, nextPartialResult: @escaping (Output, Upstream.Output) throws -> Output)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `initial` — The initial value provided on the first-use of the closure.

- `nextPartialResult` — An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value. If this closure throws an error, the publisher fails and passes the error to its subscriber.
