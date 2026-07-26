---
title: AnyPublisher
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/anypublisher
source_url: 'https://developer.apple.com/documentation/combine/anypublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anypublisher.json'
content_hash: 'sha256:4ba4a52e68192ee5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# AnyPublisher

<sub>Structure</sub>

A publisher that performs type erasure by wrapping another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyPublisher<Output, Failure> where Failure : Error
```

## Overview

[AnyPublisher](anypublisher.md) is a concrete implementation of [Publisher](publisher.md) that has no significant properties of its own, and passes through elements and completion values from its upstream publisher.

Use [AnyPublisher](anypublisher.md) to wrap a publisher whose type has details you don’t want to expose across API boundaries, such as different modules. Wrapping a [Subject](subject.md) with [AnyPublisher](anypublisher.md) also prevents callers from accessing its [send(_:)](<subject/send(__).md>) method. When you use type erasure this way, you can change the underlying publisher implementation over time without affecting existing clients.

You can use Combine’s [eraseToAnyPublisher()](<publisher/erasetoanypublisher().md>) operator to wrap a publisher with [AnyPublisher](anypublisher.md).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomPlaygroundDisplayConvertible](../swift/customplaygrounddisplayconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Escapable](../swift/escapable.md), [Publisher](publisher.md)

## Topics

### Creating a type-erased publisher

- [init(_:)](<anypublisher/init(__).md>) — Creates a type-erasing publisher to wrap the provided publisher.

## See Also

### Publishers

- [Publisher](publisher.md) — Declares that a type can transmit a sequence of values over time.
- [Publishers](publishers.md) — A namespace for types that serve as publishers.
- [Published](published.md) — A type that publishes a property marked with an attribute.
- [Cancellable](cancellable.md) — A protocol indicating that an activity or action supports cancellation.
- [AnyCancellable](anycancellable.md) — A type-erasing cancellable object that executes a provided closure when canceled.
