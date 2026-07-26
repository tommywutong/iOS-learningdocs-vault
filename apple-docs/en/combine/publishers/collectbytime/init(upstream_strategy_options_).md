---
title: 'init(upstream:strategy:options:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/collectbytime/init(upstream:strategy:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbytime/init(upstream:strategy:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbytime/init%28upstream%3Astrategy%3Aoptions%3A%29.json'
content_hash: 'sha256:4448dd874c12d645'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CollectByTime](../collectbytime.md)

# init(upstream:strategy:options:)

<sub>Initializer</sub>

Creates a publisher that buffers and periodically publishes its items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, strategy: Publishers.TimeGroupingStrategy<Context>, options: Context.SchedulerOptions?)
```

## Parameters

- `upstream` — The publisher that this publisher receives elements from.

- `strategy` — The strategy with which to collect and publish elements.

- `options` — `Scheduler` options to use for the strategy.
