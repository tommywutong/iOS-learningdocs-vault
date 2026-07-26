---
title: asLocalActor
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactor/aslocalactor
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/aslocalactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/aslocalactor.json'
content_hash: 'sha256:3f2334e83a9b81a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# asLocalActor

<sub>Instance Property</sub>

Produces an erased `any Actor` reference to this known to be local distributed actor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
var asLocalActor: any Actor { get }
```

## Discussion

Since this method is not distributed, it can only be invoked when the underlying distributed actor is known to be local, e.g. from a context that is isolated to this actor.

Such reference can be used to work with APIs accepting `isolated any Actor`, as only a local distributed actor can be isolated on and may be automatically erased to such `any Actor` when calling methods implicitly accepting the caller’s actor isolation, e.g. by using the `#isolation` macro.
