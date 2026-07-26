---
title: Publishers.SubscribeOn
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/subscribeon
source_url: 'https://developer.apple.com/documentation/combine/publishers/subscribeon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/subscribeon.json'
content_hash: 'sha256:96e52951e7723734'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.SubscribeOn

<sub>Structure</sub>

A publisher that receives elements from an upstream publisher on a specific scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscribeOn<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a subscribe-on publisher

- [init(upstream:scheduler:options:)](<subscribeon/init(upstream_scheduler_options_).md>) — Creates a publisher that receives elements from an upstream publisher on a specific scheduler.

### Declaring supporting types

- [Output](subscribeon/output.md) — The kind of values published by this publisher.
- [Failure](subscribeon/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](subscribeon/upstream.md) — The publisher from which this publisher receives elements.
- [scheduler](subscribeon/scheduler.md) — The scheduler the publisher should use to receive elements.
- [options](subscribeon/options.md) — Scheduler options that customize the delivery of elements.

## See Also

### Working with subscribers

- [ReceiveOn](receiveon.md) — A publisher that delivers elements to its downstream subscriber on a specific scheduler.
