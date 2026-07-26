---
title: 'resolve(id:using:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactor/resolve(id:using:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/resolve(id:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/resolve%28id%3Ausing%3A%29.json'
content_hash: 'sha256:6e6859dd821b369b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# resolve(id:using:)

<sub>Type Method</sub>

Resolves the passed in `id` against the `system`, returning either a local or remote actor reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func resolve(id: Self.ID, using system: Self.ActorSystem) throws -> Self
```

## Parameters

- `id` — Identity uniquely identifying a, potentially remote, actor in the system

- `system` — `system` which should be used to resolve the `identity`, and be associated with the returned actor

## Discussion

The system will be asked to `resolve` the identity and return either a local instance or request a proxy to be created for this identity.

A remote distributed actor reference will forward all invocations through the system, allowing it to take over the remote messaging with the remote actor instance.

> [!info] Postcondition
> Upon successful return, the returned actor’s [id](id.md) and [actorSystem](actorsystem-swift.property.md) properties will be equal to the values passed as parameters to this method.
