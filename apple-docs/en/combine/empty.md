---
title: Empty
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/empty
source_url: 'https://developer.apple.com/documentation/combine/empty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/empty.json'
content_hash: 'sha256:d7762ea08cd5b22b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Empty

<sub>Structure</sub>

A publisher that never publishes any values, and optionally finishes immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Empty<Output, Failure> where Failure : Error
```

## Overview

You can create a ”Never” publisher — one which never sends values and never finishes or fails — with the initializer `Empty(completeImmediately: false)`.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Publisher](publisher.md)

## Topics

### Creating an empty publisher

- [init(completeImmediately:)](<empty/init(completeimmediately_).md>) — Creates an empty publisher.
- [init(completeImmediately:outputType:failureType:)](<empty/init(completeimmediately_outputtype_failuretype_).md>) — Creates an empty publisher with the given completion behavior and output and failure types.

### Inspecting publisher properties

- [completeImmediately](empty/completeimmediately.md) — A Boolean value that indicates whether the publisher immediately sends a completion.

### Comparing publishers

- [==(_:_:)](<empty/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

## See Also

### Convenience Publishers

- [Future](future.md) — A publisher that eventually produces a single value and then finishes or fails.
- [Just](just.md) — A publisher that emits an output to each subscriber just once, and then finishes.
- [Deferred](deferred.md) — A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [Fail](fail.md) — A publisher that immediately terminates with the specified error.
- [Record](record.md) — A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.
