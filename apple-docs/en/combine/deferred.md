---
title: Deferred
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/deferred
source_url: 'https://developer.apple.com/documentation/combine/deferred'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/deferred.json'
content_hash: 'sha256:bd8990d178754722'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Deferred

<sub>Structure</sub>

A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Deferred<DeferredPublisher> where DeferredPublisher : Publisher
```

## Relationships

- **Conforms To**: [Publisher](publisher.md)

## Topics

### Creating a deferred publisher

- [init(createPublisher:)](<deferred/init(createpublisher_).md>) — Creates a deferred publisher.

### Declaring supporting types

- [Output](deferred/output.md) — The kind of values published by this publisher.
- [Failure](deferred/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [createPublisher](deferred/createpublisher.md) — The closure to execute when this deferred publisher receives a subscription.

## See Also

### Convenience Publishers

- [Future](future.md) — A publisher that eventually produces a single value and then finishes or fails.
- [Just](just.md) — A publisher that emits an output to each subscriber just once, and then finishes.
- [Empty](empty.md) — A publisher that never publishes any values, and optionally finishes immediately.
- [Fail](fail.md) — A publisher that immediately terminates with the specified error.
- [Record](record.md) — A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.
