---
title: Just
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/just
source_url: 'https://developer.apple.com/documentation/combine/just'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just.json'
content_hash: 'sha256:0062af6ce2400782'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Just

<sub>Structure</sub>

A publisher that emits an output to each subscriber just once, and then finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Just<Output>
```

## Overview

You can use a [Just](just.md) publisher to start a chain of publishers. A [Just](just.md) publisher is also useful when replacing a value with [Catch](publishers/catch.md).

In contrast with [Result.Publisher](../swift/result/publisher-swift.struct.md), a [Just](just.md) publisher can’t fail with an error. And unlike [Optional.Publisher](../swift/optional/publisher-swift.struct.md), a [Just](just.md) publisher always produces a value.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Publisher](publisher.md)

## Topics

### Creating a just ublisher

- [init(_:)](<just/init(__).md>) — Initializes a publisher that emits the specified output just once.

### Inspecting publisher properties

- [output](just/output.md) — The one element that the publisher emits.

### Comparing publishers

- [==(_:_:)](<just/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Applying operators

- [Publisher Operators](just-publisher-operators.md) — Methods that create downstream publishers or subscribers to act on the elements they receive.

### Default Implementations

- [Equatable Implementations](just/equatable-implementations.md)

## See Also

### Convenience Publishers

- [Future](future.md) — A publisher that eventually produces a single value and then finishes or fails.
- [Deferred](deferred.md) — A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [Empty](empty.md) — A publisher that never publishes any values, and optionally finishes immediately.
- [Fail](fail.md) — A publisher that immediately terminates with the specified error.
- [Record](record.md) — A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.
