---
title: 'init(upstream:dueTime:scheduler:options:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/debounce/init(upstream:duetime:scheduler:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/debounce/init(upstream:duetime:scheduler:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/debounce/init%28upstream%3Aduetime%3Ascheduler%3Aoptions%3A%29.json'
content_hash: 'sha256:ecc980afb963141a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Debounce](../debounce.md)

# init(upstream:dueTime:scheduler:options:)

<sub>Initializer</sub>

Creates a publisher that publishes elements only after a specified time interval elapses between events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, dueTime: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions?)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `dueTime` — The amount of time the publisher should wait before publishing an element.

- `scheduler` — The scheduler on which this publisher delivers elements.

- `options` — Scheduler options that customize this publisher’s delivery of elements.
