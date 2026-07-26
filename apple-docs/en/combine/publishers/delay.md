---
title: Publishers.Delay
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/delay
source_url: 'https://developer.apple.com/documentation/combine/publishers/delay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/delay.json'
content_hash: 'sha256:4db227e72833eabb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Delay

<sub>Structure</sub>

A publisher that delays delivery of elements and completion to the downstream receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Delay<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a delay publisher

- [init(upstream:interval:tolerance:scheduler:options:)](<delay/init(upstream_interval_tolerance_scheduler_options_).md>) — Creates a publisher that delays delivery of elements and completion to the downstream receiver.

### Declaring supporting types

- [Output](delay/output.md) — The kind of values published by this publisher.
- [Failure](delay/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](delay/upstream.md) — The publisher from which this publisher receives its elements.
- [interval](delay/interval.md) — The amount of time to delay.
- [tolerance](delay/tolerance.md) — The allowed tolerance in firing delayed events.
- [scheduler](delay/scheduler.md) — The scheduler to deliver the delayed events.
- [options](delay/options.md) — Options relevant to the scheduler’s behavior.

## See Also

### Controlling timing

- [MeasureInterval](measureinterval.md) — A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Debounce](debounce.md) — A publisher that publishes elements only after a specified time interval elapses between events.
- [Throttle](throttle.md) — A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Timeout](timeout.md) — A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.
