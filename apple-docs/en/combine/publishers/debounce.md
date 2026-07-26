---
title: Publishers.Debounce
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/debounce
source_url: 'https://developer.apple.com/documentation/combine/publishers/debounce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/debounce.json'
content_hash: 'sha256:24729bc1b278af56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Debounce

<sub>Structure</sub>

A publisher that publishes elements only after a specified time interval elapses between events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Debounce<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a debounce publisher

- [init(upstream:dueTime:scheduler:options:)](<debounce/init(upstream_duetime_scheduler_options_).md>) — Creates a publisher that publishes elements only after a specified time interval elapses between events.

### Declaring supporting types

- [Output](debounce/output.md) — The kind of values published by this publisher.
- [Failure](debounce/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](debounce/upstream.md) — The publisher from which this publisher receives elements.
- [dueTime](debounce/duetime.md) — The amount of time the publisher should wait before publishing an element.
- [scheduler](debounce/scheduler.md) — The scheduler on which this publisher delivers elements.
- [options](debounce/options.md) — Scheduler options that customize this publisher’s delivery of elements.

## See Also

### Controlling timing

- [MeasureInterval](measureinterval.md) — A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Delay](delay.md) — A publisher that delays delivery of elements and completion to the downstream receiver.
- [Throttle](throttle.md) — A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Timeout](timeout.md) — A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.
