---
title: AnyCancellable
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/anycancellable
source_url: 'https://developer.apple.com/documentation/combine/anycancellable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anycancellable.json'
content_hash: 'sha256:53f2efbf02671a96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# AnyCancellable

<sub>Class</sub>

A type-erasing cancellable object that executes a provided closure when canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class AnyCancellable
```

## Overview

Subscriber implementations can use this type to provide a “cancellation token” that makes it possible for a caller to cancel a publisher, but not to use the [Subscription](subscription.md) object to request items.

An [AnyCancellable](anycancellable.md) instance automatically calls [cancel()](<cancellable/cancel().md>) when deinitialized.

## Relationships

- **Conforms To**: [Cancellable](cancellable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a type-erased cancellable

- [init(_:)](<anycancellable/init(__)-3icn3.md>) — Initializes the cancellable object with the given cancel-time closure.
- [init(_:)](<anycancellable/init(__)-48fh3.md>)

### Storing instances

- [store(in:)](<anycancellable/store(in_)-6cr9i.md>) — Stores this type-erasing cancellable instance in the specified collection.
- [store(in:)](<anycancellable/store(in_)-3hyxs.md>) — Stores this type-erasing cancellable instance in the specified set.

### Operators

- [==(_:_:)](<anycancellable/==(____).md>) — Returns a Boolean value that indicates whether two instances are equal, as determined by comparing whether their references point to the same instance.

## See Also

### Publishers

- [Publisher](publisher.md) — Declares that a type can transmit a sequence of values over time.
- [Publishers](publishers.md) — A namespace for types that serve as publishers.
- [AnyPublisher](anypublisher.md) — A publisher that performs type erasure by wrapping another publisher.
- [Published](published.md) — A type that publishes a property marked with an attribute.
- [Cancellable](cancellable.md) — A protocol indicating that an activity or action supports cancellation.
