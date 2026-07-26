---
title: 'init(upstream:retries:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/retry/init(upstream:retries:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/retry/init(upstream:retries:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/retry/init%28upstream%3Aretries%3A%29.json'
content_hash: 'sha256:eeb25cf33483b177'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Retry](../retry.md)

# init(upstream:retries:)

<sub>Initializer</sub>

Creates a publisher that attempts to recreate its subscription to a failed upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, retries: Int?)
```

## Parameters

- `upstream` — The publisher from which this publisher receives its elements.

- `retries` — The maximum number of retry attempts to perform. If `nil`, this publisher attempts to reconnect with the upstream publisher an unlimited number of times.
