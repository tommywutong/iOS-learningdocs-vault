---
title: 'init(upstream:scheduler:options:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/receiveon/init(upstream:scheduler:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/receiveon/init(upstream:scheduler:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/receiveon/init%28upstream%3Ascheduler%3Aoptions%3A%29.json'
content_hash: 'sha256:b3f94504c6c4e732'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [ReceiveOn](../receiveon.md)

# init(upstream:scheduler:options:)

<sub>Initializer</sub>

Creates a publisher that delivers elements to its downstream subscriber on a specific scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, scheduler: Context, options: Context.SchedulerOptions?)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `scheduler` — The scheduler the publisher uses to deliver elements.

- `options` — Scheduler options used to customize element delivery.
