---
title: CustomCombineIdentifierConvertible
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/customcombineidentifierconvertible
source_url: 'https://developer.apple.com/documentation/combine/customcombineidentifierconvertible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/customcombineidentifierconvertible.json'
content_hash: 'sha256:c5353d68076ef5cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# CustomCombineIdentifierConvertible

<sub>Protocol</sub>

A protocol for uniquely identifying publisher streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomCombineIdentifierConvertible
```

## Overview

If you create a custom [Subscription](subscription.md) or [Subscriber](subscriber.md) type, implement this protocol so that development tools can uniquely identify publisher chains in your app. If your type is a class, Combine provides an implementation of [combineIdentifier](customcombineidentifierconvertible/combineidentifier.md) for you. If your type is a structure, set up the identifier as follows:

```swift
let combineIdentifier = CombineIdentifier()
```

## Relationships

- **Inherited By**: [Subscriber](subscriber.md), [Subscription](subscription.md)

- **Conforming Types**: [AnySubscriber](anysubscriber.md), [Assign](subscribers/assign.md), [Sink](subscribers/sink.md)

## Topics

### Identifying publisher streams

- [combineIdentifier](customcombineidentifierconvertible/combineidentifier.md) — A unique identifier for identifying publisher streams.

## See Also

### Debugging Identifiers

- [CombineIdentifier](combineidentifier.md) — A unique identifier for identifying publisher streams.
