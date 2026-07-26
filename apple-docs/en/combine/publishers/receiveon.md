---
title: Publishers.ReceiveOn
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/receiveon
source_url: 'https://developer.apple.com/documentation/combine/publishers/receiveon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/receiveon.json'
content_hash: 'sha256:467b7ff2f7d2774b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.ReceiveOn

<sub>Structure</sub>

A publisher that delivers elements to its downstream subscriber on a specific scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReceiveOn<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a receive-on Publisher

- [init(upstream:scheduler:options:)](<receiveon/init(upstream_scheduler_options_).md>) — Creates a publisher that delivers elements to its downstream subscriber on a specific scheduler.

### Declaring supporting types

- [Output](receiveon/output.md) — The kind of values published by this publisher.
- [Failure](receiveon/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](receiveon/upstream.md) — The publisher from which this publisher receives elements.
- [scheduler](receiveon/scheduler.md) — The scheduler the publisher uses to deliver elements.
- [options](receiveon/options.md) — Scheduler options used to customize element delivery.

## See Also

### Working with subscribers

- [SubscribeOn](subscribeon.md) — A publisher that receives elements from an upstream publisher on a specific scheduler.
