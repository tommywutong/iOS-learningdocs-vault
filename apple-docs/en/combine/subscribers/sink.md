---
title: Subscribers.Sink
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/sink
source_url: 'https://developer.apple.com/documentation/combine/subscribers/sink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/sink.json'
content_hash: 'sha256:0556c75608068b39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscribers](../subscribers.md)

# Subscribers.Sink

<sub>Class</sub>

A simple subscriber that requests an unlimited number of values upon subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Sink<Input, Failure> where Failure : Error
```

## Relationships

- **Conforms To**: [Cancellable](../cancellable.md), [CustomCombineIdentifierConvertible](../customcombineidentifierconvertible.md), [CustomPlaygroundDisplayConvertible](../../swift/customplaygrounddisplayconvertible.md), [CustomReflectable](../../swift/customreflectable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Subscriber](../subscriber.md)

## Topics

### Creating a sink subscriber

- [init(receiveCompletion:receiveValue:)](<sink/init(receivecompletion_receivevalue_).md>) — Initializes a sink with the provided closures.

### Inspecting subscriber properties

- [receiveValue](sink/receivevalue.md) — The closure to execute on receipt of a value.
- [receiveCompletion](sink/receivecompletion.md) — The closure to execute on completion.

## See Also

### Using convenience subscribers

- [Assign](assign.md) — A simple subscriber that assigns received elements to a property indicated by a key path.
