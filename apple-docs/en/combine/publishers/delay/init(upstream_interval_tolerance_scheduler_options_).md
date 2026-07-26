---
title: 'init(upstream:interval:tolerance:scheduler:options:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/delay/init(upstream:interval:tolerance:scheduler:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/delay/init(upstream:interval:tolerance:scheduler:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/delay/init%28upstream%3Ainterval%3Atolerance%3Ascheduler%3Aoptions%3A%29.json'
content_hash: 'sha256:19b50909d1f74247'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Delay](../delay.md)

# init(upstream:interval:tolerance:scheduler:options:)

<sub>Initializer</sub>

Creates a publisher that delays delivery of elements and completion to the downstream receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, tolerance: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions? = nil)
```

## Parameters

- `upstream` — The publisher from which this publisher receives its elements.

- `interval` — The amount of time to delay.

- `tolerance` — The allowed tolerance in delivering delayed events. The `Delay` publisher may deliver elements this much sooner or later than the interval specifies.

- `scheduler` — The scheduler to deliver the delayed events.

- `options` — Options relevant to the scheduler’s behavior.
