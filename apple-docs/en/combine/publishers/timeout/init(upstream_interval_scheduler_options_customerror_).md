---
title: 'init(upstream:interval:scheduler:options:customError:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/timeout/init(upstream:interval:scheduler:options:customerror:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/timeout/init(upstream:interval:scheduler:options:customerror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/timeout/init%28upstream%3Ainterval%3Ascheduler%3Aoptions%3Acustomerror%3A%29.json'
content_hash: 'sha256:3b47253cad48169f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Timeout](../timeout.md)

# init(upstream:interval:scheduler:options:customError:)

<sub>Initializer</sub>

Creates a publisher that terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, interval: Context.SchedulerTimeType.Stride, scheduler: Context, options: Context.SchedulerOptions?, customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `interval` — The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.

- `scheduler` — The scheduler on which to deliver events.

- `options` — Scheduler options that customize the delivery of elements.

- `customError` — A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.
