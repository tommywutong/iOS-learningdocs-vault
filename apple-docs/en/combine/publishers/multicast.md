---
title: Publishers.Multicast
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/multicast
source_url: 'https://developer.apple.com/documentation/combine/publishers/multicast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/multicast.json'
content_hash: 'sha256:e8768a7bf9f829f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Multicast

<sub>Class</sub>

A publisher that uses a subject to deliver elements to multiple subscribers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Multicast<Upstream, SubjectType> where Upstream : Publisher, SubjectType : Subject, Upstream.Failure == SubjectType.Failure, Upstream.Output == SubjectType.Output
```

## Overview

Use a multicast publisher when you have multiple downstream subscribers, but you want upstream publishers to only process one [receive(_:)](<../subscriber/receive(__).md>) call per event.

## Relationships

- **Conforms To**: [ConnectablePublisher](../connectablepublisher.md), [Publisher](../publisher.md)

## Topics

### Creating a multicast publisher

- [init(upstream:createSubject:)](<multicast/init(upstream_createsubject_).md>) — Creates a multicast publisher that applies a closure to create a subject that delivers elements to subscribers.

### Declaring supporting types

- [Output](multicast/output.md) — The kind of values published by this publisher.
- [Failure](multicast/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](multicast/upstream.md) — The publisher from which this publisher receives its elements.
- [createSubject](multicast/createsubject.md) — A closure that returns a subject each time a subscriber attaches to the multicast publisher.

## See Also

### Working with multiple subscribers

- [Share](share.md) — A publisher that shares the output of an upstream publisher with multiple subscribers.
