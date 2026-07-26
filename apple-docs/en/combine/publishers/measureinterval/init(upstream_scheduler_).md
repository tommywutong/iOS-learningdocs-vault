---
title: 'init(upstream:scheduler:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/measureinterval/init(upstream:scheduler:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/measureinterval/init(upstream:scheduler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/measureinterval/init%28upstream%3Ascheduler%3A%29.json'
content_hash: 'sha256:556fe8fa36fb8e63'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MeasureInterval](../measureinterval.md)

# init(upstream:scheduler:)

<sub>Initializer</sub>

Creates a publisher that measures and emits the time interval between events received from an upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, scheduler: Context)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `scheduler` — A scheduler to use for tracking the timing of events.
