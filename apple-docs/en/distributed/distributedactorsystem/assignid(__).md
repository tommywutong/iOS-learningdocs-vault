---
title: 'assignID(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactorsystem/assignid(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/assignid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/assignid%28_%3A%29.json'
content_hash: 'sha256:a9aab50ea1641568'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# assignID(_:)

<sub>Instance Method</sub>

Assign an [ActorID](actorid.md) for the passed actor type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assignID<Act>(_ actorType: Act.Type) -> Self.ActorID where Act : DistributedActor, Self.ActorID == Act.ID
```

## Discussion

This function is invoked by a distributed actor during its initialization, and the returned address value is stored along with it for the time of its lifetime.

The address MUST uniquely identify the actor, and allow resolving it. E.g. if an actor is created under address `addr1` then immediately invoking `system.resolve(id: addr1, as: Greeter.self)` MUST return a reference to the same actor.
