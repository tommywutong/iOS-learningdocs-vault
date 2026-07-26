---
title: Subscribers
framework: Combine
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers
source_url: 'https://developer.apple.com/documentation/combine/subscribers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers.json'
content_hash: 'sha256:330c47d969947601'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Subscribers

<sub>Enumeration</sub>

A namespace for types that serve as subscribers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Subscribers
```

## Topics

### Requesting elements

- [Demand](subscribers/demand.md) — A requested number of items, sent to a publisher from a subscriber through the subscription.

### Receiving life cycle events

- [Completion](subscribers/completion.md) — A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.

### Using convenience subscribers

- [Sink](subscribers/sink.md) — A simple subscriber that requests an unlimited number of values upon subscription.
- [Assign](subscribers/assign.md) — A simple subscriber that assigns received elements to a property indicated by a key path.

## See Also

### Subscribers

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md) — Apply back pressure to precisely control when publishers produce elements.
- [Subscriber](subscriber.md) — A protocol that declares a type that can receive input from a publisher.
- [AnySubscriber](anysubscriber.md) — A type-erasing subscriber.
- [Subscription](subscription.md) — A protocol representing the connection of a subscriber to a publisher.
- [Subscriptions](subscriptions.md) — A namespace for symbols related to subscriptions.
