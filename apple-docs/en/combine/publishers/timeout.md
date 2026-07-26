---
title: Publishers.Timeout
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/timeout
source_url: 'https://developer.apple.com/documentation/combine/publishers/timeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/timeout.json'
content_hash: 'sha256:39eda428c66146aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Timeout

<sub>Structure</sub>

A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Timeout<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a timeout publisher

- [init(upstream:interval:scheduler:options:customError:)](<timeout/init(upstream_interval_scheduler_options_customerror_).md>) — Creates a publisher that terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.

### Declaring supporting types

- [Output](timeout/output.md) — The kind of values published by this publisher.
- [Failure](timeout/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](timeout/upstream.md) — The publisher from which this publisher receives elements.
- [interval](timeout/interval.md) — The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.
- [scheduler](timeout/scheduler.md) — The scheduler on which to deliver events.
- [options](timeout/options.md) — Scheduler options that customize the delivery of elements.
- [customError](timeout/customerror.md) — A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.

## See Also

### Controlling timing

- [MeasureInterval](measureinterval.md) — A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Debounce](debounce.md) — A publisher that publishes elements only after a specified time interval elapses between events.
- [Delay](delay.md) — A publisher that delays delivery of elements and completion to the downstream receiver.
- [Throttle](throttle.md) — A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
