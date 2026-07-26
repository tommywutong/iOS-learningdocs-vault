---
title: 'resignID(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactorsystem/resignid(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystem/resignid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystem/resignid%28_%3A%29.json'
content_hash: 'sha256:6162080970f7b5d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorSystem](../distributedactorsystem.md)

# resignID(_:)

<sub>Instance Method</sub>

Called during when a distributed actor is deinitialized, or fails to initialize completely (e.g. by throwing out of an `init` that did not completely initialize all of the actors stored properties yet).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resignID(_ id: Self.ActorID)
```

## Parameters

- `id` — The id of an actor managed by this system that has begun its `deinit`.

## Discussion

This method is guaranteed to be called at-most-once for a given id (assuming IDs are unique, and not re-cycled by the system), i.e. if it is called during a failure to initialize completely, the call from the actor’s deinitializer will not happen (as under these circumstances, `deinit` will be run).

If `resignID` gets called with some unknown ID, it should crash immediately as it signifies some very unexpected use of the system.
