---
title: Publishers.CollectByTime
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/collectbytime
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbytime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbytime.json'
content_hash: 'sha256:60813539d21e04a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.CollectByTime

<sub>Structure</sub>

A publisher that buffers and periodically publishes its items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CollectByTime<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a collect by time Publisher

- [init(upstream:strategy:options:)](<collectbytime/init(upstream_strategy_options_).md>) — Creates a publisher that buffers and periodically publishes its items.

### Declaring supporting types

- [Output](collectbytime/output.md) — The kind of values published by this publisher.
- [Failure](collectbytime/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](collectbytime/upstream.md) — The publisher that this publisher receives elements from.
- [strategy](collectbytime/strategy.md) — The strategy with which to collect and publish elements.
- [options](collectbytime/options.md) — Scheduler options to use for the strategy.

## See Also

### Reducing elements

- [Collect](collect.md) — A publisher that buffers items.
- [CollectByCount](collectbycount.md) — A publisher that buffers a maximum number of items.
- [TimeGroupingStrategy](timegroupingstrategy.md) — A strategy for collecting received elements.
- [IgnoreOutput](ignoreoutput.md) — A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Reduce](reduce.md) — A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [TryReduce](tryreduce.md) — A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.
