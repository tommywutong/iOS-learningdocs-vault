---
title: Publishers.Throttle
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/throttle
source_url: 'https://developer.apple.com/documentation/combine/publishers/throttle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/throttle.json'
content_hash: 'sha256:0dc2579fd3e9132a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Throttle

<sub>Structure</sub>

A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Throttle<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a throttle publisher

- [init(upstream:interval:scheduler:latest:)](<throttle/init(upstream_interval_scheduler_latest_).md>) — Creates a publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.

### Declaring supporting types

- [Output](throttle/output.md) — The kind of values published by this publisher.
- [Failure](throttle/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](throttle/upstream.md) — The publisher from which this publisher receives elements.
- [interval](throttle/interval.md) — The interval in which to find and emit the most recent element.
- [scheduler](throttle/scheduler.md) — The scheduler on which to publish elements.
- [latest](throttle/latest.md) — A Boolean value indicating whether to publish the most recent element.

## See Also

### Controlling timing

- [MeasureInterval](measureinterval.md) — A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Debounce](debounce.md) — A publisher that publishes elements only after a specified time interval elapses between events.
- [Delay](delay.md) — A publisher that delays delivery of elements and completion to the downstream receiver.
- [Timeout](timeout.md) — A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.
