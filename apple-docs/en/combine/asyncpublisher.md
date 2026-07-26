---
title: AsyncPublisher
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/asyncpublisher
source_url: 'https://developer.apple.com/documentation/combine/asyncpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncpublisher.json'
content_hash: 'sha256:2730b391f62732b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# AsyncPublisher

<sub>Structure</sub>

A publisher that exposes its elements as an asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncPublisher<P> where P : Publisher, P.Failure == Never
```

## Overview

`AsyncPublisher` conforms to [AsyncSequence](../swift/asyncsequence.md), which allows callers to receive values with the `for`-`await`-`in` syntax, rather than attaching a [Subscriber](subscriber.md).

Use the [values](publisher/values-1dm9r.md) property of the [Publisher](publisher.md) protocol to wrap an existing publisher with an instance of this type.

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md)

## Topics

### Creating an asynchronous publisher

- [init(_:)](<asyncpublisher/init(__).md>) — Creates a publisher that exposes elements received from an upstream publisher as an asynchronous sequence.

### Creating an iterator

- [makeAsyncIterator()](<asyncpublisher/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [Iterator](asyncpublisher/iterator.md) — The iterator that produces elements of the asynchronous publisher sequence.

### Supporting types

- [Element](asyncpublisher/element.md) — The type of element produced by this asynchronous sequence.

## See Also

### Asynchronous Publishers

- [AsyncThrowingPublisher](asyncthrowingpublisher.md) — A publisher that exposes its elements as a throwing asynchronous sequence.
