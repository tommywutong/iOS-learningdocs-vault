---
title: Subscription
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscription
source_url: 'https://developer.apple.com/documentation/combine/subscription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscription.json'
content_hash: 'sha256:1a3112dc40e708c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Subscription

<sub>Protocol</sub>

A protocol representing the connection of a subscriber to a publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Subscription : Cancellable, CustomCombineIdentifierConvertible
```

## Overview

Subscriptions are class constrained because a [Subscription](subscription.md) has identity, defined by the moment in time a particular subscriber attached to a publisher. Canceling a [Subscription](subscription.md) must be thread-safe.

You can only cancel a [Subscription](subscription.md) once.

Canceling a subscription frees up any resources previously allocated by attaching the [Subscriber](subscriber.md).

## Relationships

- **Inherits From**: [Cancellable](cancellable.md), [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)

## Topics

### Requesting elements

- [request(_:)](<subscription/request(__).md>) — Tells a publisher that it may send more values to the subscriber.
- [Demand](subscribers/demand.md) — A requested number of items, sent to a publisher from a subscriber through the subscription.

## See Also

### Subscribers

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md) — Apply back pressure to precisely control when publishers produce elements.
- [Subscriber](subscriber.md) — A protocol that declares a type that can receive input from a publisher.
- [Subscribers](subscribers.md) — A namespace for types that serve as subscribers.
- [AnySubscriber](anysubscriber.md) — A type-erasing subscriber.
- [Subscriptions](subscriptions.md) — A namespace for symbols related to subscriptions.
