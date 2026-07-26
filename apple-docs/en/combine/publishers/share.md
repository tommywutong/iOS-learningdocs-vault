---
title: Publishers.Share
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/share
source_url: 'https://developer.apple.com/documentation/combine/publishers/share'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/share.json'
content_hash: 'sha256:6e589d940e6fe518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Share

<sub>Class</sub>

A publisher that shares the output of an upstream publisher with multiple subscribers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Share<Upstream> where Upstream : Publisher
```

## Overview

This publisher type supports multiple subscribers, all of whom receive unchanged elements and completion states from the upstream publisher.

> [!tip] Tip
> [Share](share.md) is effectively a combination of the [Multicast](multicast.md) and [PassthroughSubject](../passthroughsubject.md) publishers, with an implicit [autoconnect()](<../connectablepublisher/autoconnect().md>).

Be aware that [Share](share.md) is a class rather than a structure like most other publishers. Use this type when you need a publisher instance that uses reference semantics.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a share publisher

- [init(upstream:)](<share/init(upstream_).md>) — Creates a publisher that shares the output of an upstream publisher with multiple subscribers.

### Declaring supporting types

- [Output](share/output.md) — The kind of values published by this publisher.
- [Failure](share/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](share/upstream.md) — The publisher from which this publisher receives elements.

### Comparing publishers

- [==(_:_:)](<share/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

## See Also

### Working with multiple subscribers

- [Multicast](multicast.md) — A publisher that uses a subject to deliver elements to multiple subscribers.
