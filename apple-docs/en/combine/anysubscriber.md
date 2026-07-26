---
title: AnySubscriber
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/anysubscriber
source_url: 'https://developer.apple.com/documentation/combine/anysubscriber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anysubscriber.json'
content_hash: 'sha256:275c92a6d54917aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# AnySubscriber

<sub>Structure</sub>

A type-erasing subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnySubscriber<Input, Failure> where Failure : Error
```

## Overview

Use an [AnySubscriber](anysubscriber.md) to wrap an existing subscriber whose details you don’t want to expose. You can also use [AnySubscriber](anysubscriber.md) to create a custom subscriber by providing closures for the methods defined in [Subscriber](subscriber.md), rather than implementing [Subscriber](subscriber.md) directly.

## Relationships

- **Conforms To**: [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md), [CustomPlaygroundDisplayConvertible](../swift/customplaygrounddisplayconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Subscriber](subscriber.md)

## Topics

### Creating a type-erased subscriber

- [init(_:)](<anysubscriber/init(__)-2dbfs.md>) — Creates a type-erasing subscriber to wrap an existing subscriber.
- [init(_:)](<anysubscriber/init(__)-3t3eh.md>) — Creates a type-erasing subscriber to wrap an existing subscriber.
- [init(receiveSubscription:receiveValue:receiveCompletion:)](<anysubscriber/init(receivesubscription_receivevalue_receivecompletion_).md>) — Creates a type-erasing subscriber that executes the provided closures.

## See Also

### Subscribers

- [Processing Published Elements with Subscribers](processing-published-elements-with-subscribers.md) — Apply back pressure to precisely control when publishers produce elements.
- [Subscriber](subscriber.md) — A protocol that declares a type that can receive input from a publisher.
- [Subscribers](subscribers.md) — A namespace for types that serve as subscribers.
- [Subscription](subscription.md) — A protocol representing the connection of a subscriber to a publisher.
- [Subscriptions](subscriptions.md) — A namespace for symbols related to subscriptions.
