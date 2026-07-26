---
title: Identifiable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/identifiable
source_url: 'https://developer.apple.com/documentation/swift/identifiable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/identifiable.json'
content_hash: 'sha256:5c19a78f444f492e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Identifiable

<sub>Protocol</sub>

A class of types whose instances hold the value of an entity with stable identity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Identifiable<ID>
```

## Overview

Use the `Identifiable` protocol to provide a stable notion of identity to a class or value type. For example, you could define a `User` type with an `id` property that is stable across your app and your app’s database storage. You could use the `id` property to identify a particular user even if other data fields change, such as the user’s name.

`Identifiable` leaves the duration and scope of the identity unspecified. Identities can have any of the following characteristics:

- Guaranteed always unique, like UUIDs.
- Persistently unique per environment, like database record keys.
- Unique for the lifetime of a process, like global incrementing integers.
- Unique for the lifetime of an object, like object identifiers.
- Unique within the current collection, like collection indices.

It’s up to both the conformer and the receiver of the protocol to document the nature of the identity.

## Conforming to the Identifiable Protocol

`Identifiable` provides a default implementation for class types (using `ObjectIdentifier`), which is only guaranteed to remain unique for the lifetime of an object. If an object has a stronger notion of identity, it may be appropriate to provide a custom implementation.

## Relationships

- **Inherited By**: [DistributedActor](../distributed/distributedactor.md)

- **Conforming Types**: [Never](never.md)

## Topics

### Specifying the Associated Type

- [ID](identifiable/id-swift.associatedtype.md) — A type representing the stable identity of the entity associated with an instance.

### Specifying the Identified Item

- [id](identifiable/id-8t2ws.md) — The stable identity of the entity associated with this instance.

## See Also

### Equality and Ordering

- [Equatable](equatable.md) — A type that can be compared for value equality.
- [Comparable](comparable.md) — A type that can be compared using the relational operators `<`, `<=`, `>=`, and `>`.
