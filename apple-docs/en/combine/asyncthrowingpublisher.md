---
title: AsyncThrowingPublisher
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/asyncthrowingpublisher
source_url: 'https://developer.apple.com/documentation/combine/asyncthrowingpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncthrowingpublisher.json'
content_hash: 'sha256:53ce11c59b563fb3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# AsyncThrowingPublisher

<sub>Structure</sub>

A publisher that exposes its elements as a throwing asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncThrowingPublisher<P> where P : Publisher
```

## Overview

`AsyncThrowingPublisher` conforms to [AsyncSequence](../swift/asyncsequence.md), which allows callers to receive values with the `for`-`await`-`in` syntax, rather than attaching a [Subscriber](subscriber.md). If the upstream publisher terminates with an error, `AsyncThrowingPublisher` throws the error to the awaiting caller.

Use the [values](publisher/values-v7nz.md) property of the [Publisher](publisher.md) protocol to wrap an existing publisher with an instance of this type.

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md)

## Topics

### Creating an asynchronous publisher

- [init(_:)](<asyncthrowingpublisher/init(__).md>) — Creates a publisher that exposes elements received from an upstream publisher as a throwing asynchronous sequence.

### Creating an iterator

- [makeAsyncIterator()](<asyncthrowingpublisher/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [Iterator](asyncthrowingpublisher/iterator.md) — The iterator that produces elements of the asynchronous publisher sequence.

### Supporting types

- [Element](asyncthrowingpublisher/element.md) — The type of element produced by this asynchronous sequence.

## See Also

### Asynchronous Publishers

- [AsyncPublisher](asyncpublisher.md) — A publisher that exposes its elements as an asynchronous sequence.
