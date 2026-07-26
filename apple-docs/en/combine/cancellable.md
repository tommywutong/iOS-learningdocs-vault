---
title: Cancellable
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/cancellable
source_url: 'https://developer.apple.com/documentation/combine/cancellable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/cancellable.json'
content_hash: 'sha256:3fdbb83a48b332b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Cancellable

<sub>Protocol</sub>

A protocol indicating that an activity or action supports cancellation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Cancellable
```

## Overview

Calling [cancel()](<cancellable/cancel().md>) frees up any allocated resources. It also stops side effects such as timers, network access, or disk I/O.

## Relationships

- **Inherited By**: [Subscription](subscription.md)

- **Conforming Types**: [AnyCancellable](anycancellable.md), [Assign](subscribers/assign.md), [Sink](subscribers/sink.md)

## Topics

### Canceling actions

- [cancel()](<cancellable/cancel().md>) — Cancel the activity.

### Storing instances

- [store(in:)](<cancellable/store(in_)-35vnt.md>) — Stores this cancellable instance in the specified collection.
- [store(in:)](<cancellable/store(in_)-95sfl.md>) — Stores this cancellable instance in the specified set.

### Instance Methods

- [storeWhileEntityActive(_:)](<cancellable/storewhileentityactive(__).md>) — Retains the `Cancellable` as long as the entity is active (see `Entity.isActive`). If the entity is deactivated, the `Cancellable` is released.

## See Also

### Publishers

- [Publisher](publisher.md) — Declares that a type can transmit a sequence of values over time.
- [Publishers](publishers.md) — A namespace for types that serve as publishers.
- [AnyPublisher](anypublisher.md) — A publisher that performs type erasure by wrapping another publisher.
- [Published](published.md) — A type that publishes a property marked with an attribute.
- [AnyCancellable](anycancellable.md) — A type-erasing cancellable object that executes a provided closure when canceled.
