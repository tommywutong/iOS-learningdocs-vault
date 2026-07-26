---
title: Fail
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/fail
source_url: 'https://developer.apple.com/documentation/combine/fail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/fail.json'
content_hash: 'sha256:a913303a3299b1ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Fail

<sub>Structure</sub>

A publisher that immediately terminates with the specified error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Fail<Output, Failure> where Failure : Error
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Publisher](publisher.md)

## Topics

### Creating a fail publisher

- [init(error:)](<fail/init(error_).md>) — Creates a publisher that immediately terminates with the specified failure.
- [init(outputType:failure:)](<fail/init(outputtype_failure_).md>) — Creates publisher with the given output type, that immediately terminates with the specified failure.

### Inspecting publisher properties

- [error](fail/error.md) — The failure to send when terminating the publisher.

### Comparing publishers

- [==(_:_:)](<fail/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](fail/equatable-implementations.md)

## See Also

### Convenience Publishers

- [Future](future.md) — A publisher that eventually produces a single value and then finishes or fails.
- [Just](just.md) — A publisher that emits an output to each subscriber just once, and then finishes.
- [Deferred](deferred.md) — A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [Empty](empty.md) — A publisher that never publishes any values, and optionally finishes immediately.
- [Record](record.md) — A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.
