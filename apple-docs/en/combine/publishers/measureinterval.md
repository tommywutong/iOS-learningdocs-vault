---
title: Publishers.MeasureInterval
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/measureinterval
source_url: 'https://developer.apple.com/documentation/combine/publishers/measureinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/measureinterval.json'
content_hash: 'sha256:90fb9fd194b625a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.MeasureInterval

<sub>Structure</sub>

A publisher that measures and emits the time interval between events received from an upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MeasureInterval<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a measure interval publisher

- [init(upstream:scheduler:)](<measureinterval/init(upstream_scheduler_).md>) — Creates a publisher that measures and emits the time interval between events received from an upstream publisher.

### Declaring supporting types

- [Output](measureinterval/output.md) — The kind of values published by this publisher.
- [Failure](measureinterval/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](measureinterval/upstream.md) — The publisher from which this publisher receives elements.
- [scheduler](measureinterval/scheduler.md) — The scheduler used for tracking the timing of events.

## See Also

### Controlling timing

- [Debounce](debounce.md) — A publisher that publishes elements only after a specified time interval elapses between events.
- [Delay](delay.md) — A publisher that delays delivery of elements and completion to the downstream receiver.
- [Throttle](throttle.md) — A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Timeout](timeout.md) — A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.
