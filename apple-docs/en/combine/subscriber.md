---
title: Subscriber
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscriber
source_url: 'https://developer.apple.com/documentation/combine/subscriber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriber.json'
content_hash: 'sha256:076cf0bb87df2a4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Subscriber

<sub>Protocol</sub>

A protocol that declares a type that can receive input from a publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Subscriber<Input, Failure> : CustomCombineIdentifierConvertible
```

## Overview

A [Subscriber](subscriber.md) instance receives a stream of elements from a [Publisher](publisher.md), along with life cycle events describing changes to their relationship. A given subscriber’s [Input](subscriber/input.md) and [Failure](subscriber/failure.md) associated types must match the [Output](publisher/output.md) and [Failure](publisher/failure.md) of its corresponding publisher.

You connect a subscriber to a publisher by calling the publisher’s [subscribe(_:)](<publisher/subscribe(__)-4u8kn.md>) method.  After making this call, the publisher invokes the subscriber’s [receive(subscription:)](<subscriber/receive(subscription_).md>) method. This gives the subscriber a [Subscription](subscription.md) instance, which it uses to demand elements from the publisher, and to optionally cancel the subscription. After the subscriber makes an initial demand, the publisher calls [receive(_:)](<subscriber/receive(__).md>), possibly asynchronously, to deliver newly-published elements. If the publisher stops publishing, it calls [receive(completion:)](<subscriber/receive(completion_).md>), using a parameter of type [Completion](subscribers/completion.md) to indicate whether publishing completes normally or with an error.

Combine provides the following subscribers as operators on the [Publisher](publisher.md) type:

- [sink(receiveCompletion:receiveValue:)](<publisher/sink(receivecompletion_receivevalue_).md>) executes arbitrary closures when it receives a completion signal and each time it receives a new element.
- [assign(to:on:)](<publisher/assign(to_on_).md>) writes each newly-received value to a property identified by a key path on a given instance.

## Relationships

- **Inherits From**: [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)

- **Conforming Types**: [AnySubscriber](anysubscriber.md), [Assign](subscribers/assign.md), [Sink](subscribers/sink.md)

## Topics

### Declaring supporting types

- [Input](subscriber/input.md) — The kind of values this subscriber receives.
- [Failure](subscriber/failure.md) — The kind of errors this subscriber might receive.

### Receiving elements

- [receive(_:)](<subscriber/receive(__).md>) — Tells the subscriber that the publisher has produced an element.
- [receive()](<subscriber/receive().md>) — Tells the subscriber that a publisher of void elements is ready to receive further requests.

### Receiving life cycle events

- [receive(subscription:)](<subscriber/receive(subscription_).md>) — Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [receive(completion:)](<subscriber/receive(completion_).md>) — Tells the subscriber that the publisher has completed publishing, either normally or with an error.
- [Completion](subscribers/completion.md) — A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.

## See Also

### Subscribers

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md) — Apply back pressure to precisely control when publishers produce elements.
- [Subscribers](subscribers.md) — A namespace for types that serve as subscribers.
- [AnySubscriber](anysubscriber.md) — A type-erasing subscriber.
- [Subscription](subscription.md) — A protocol representing the connection of a subscriber to a publisher.
- [Subscriptions](subscriptions.md) — A namespace for symbols related to subscriptions.
