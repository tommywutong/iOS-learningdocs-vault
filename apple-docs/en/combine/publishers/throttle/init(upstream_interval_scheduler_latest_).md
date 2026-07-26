---
title: 'init(upstream:interval:scheduler:latest:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/throttle/init(upstream:interval:scheduler:latest:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/throttle/init(upstream:interval:scheduler:latest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/throttle/init%28upstream%3Ainterval%3Ascheduler%3Alatest%3A%29.json'
content_hash: 'sha256:44fa7bea828cf98e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Throttle](../throttle.md)

# init(upstream:interval:scheduler:latest:)

<sub>Initializer</sub>

Creates a publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, scheduler: Context, latest: Bool)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `interval` — The interval in which to find and emit the most recent element.

- `scheduler` — The scheduler on which to publish elements.

- `latest` — A Boolean value indicating whether to publish the most recent element. If `false`, the publisher emits the first element received during the interval.
