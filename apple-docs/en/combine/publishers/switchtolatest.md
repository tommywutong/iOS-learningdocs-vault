---
title: Publishers.SwitchToLatest
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/switchtolatest
source_url: 'https://developer.apple.com/documentation/combine/publishers/switchtolatest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/switchtolatest.json'
content_hash: 'sha256:f50c54bbf21edf61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.SwitchToLatest

<sub>Structure</sub>

A publisher that flattens nested publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SwitchToLatest<P, Upstream> where P : Publisher, P == Upstream.Output, Upstream : Publisher, P.Failure == Upstream.Failure
```

## Overview

Given a publisher that publishes [Publisher](../publisher.md) instances, the [SwitchToLatest](switchtolatest.md) publisher produces a sequence of events from only the most recent one. For example, given the type `AnyPublisher<URLSession.DataTaskPublisher,NSError>`, calling `switchToLatest()` results in the type `SwitchToLatest<(Data, URLResponse), URLError>`. The downstream subscriber sees a continuous stream of `(Data, URLResponse)` elements from what looks like a single [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md) even though the elements are coming from different upstream publishers.

When [SwitchToLatest](switchtolatest.md) receives a new publisher from the upstream publisher, it cancels its previous subscription. Use this feature to prevent earlier publishers from performing unnecessary work, such as creating network request publishers from frequently-updating user interface publishers.

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a switch-to-latest Publisher

- [init(upstream:)](<switchtolatest/init(upstream_).md>) — Creates a publisher that “flattens” nested publishers.

### Declaring supporting types

- [Output](switchtolatest/output.md) — The kind of values published by this publisher.
- [Failure](switchtolatest/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](switchtolatest/upstream.md) — The publisher from which this publisher receives elements.

## See Also

### Republishing elements by subscribing to new publishers

- [FlatMap](flatmap.md) — A publisher that transforms elements from an upstream publisher into a new publisher.
