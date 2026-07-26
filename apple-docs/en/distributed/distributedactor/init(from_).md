---
title: 'init(from:)'
framework: Distributed
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactor/init(from:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactor/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactor/init%28from%3A%29.json'
content_hash: 'sha256:29090faf9ab690ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActor](../distributedactor.md)

# init(from:)

<sub>Initializer</sub>

Initializes an instance of this distributed actor by decoding its [id](id.md), and passing it to the [DistributedActorSystem](../distributedactorsystem.md) obtained from `decoder.userInfo[actorSystemKey]`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — Used to decode the `ID` of this distributed actor.

## Requires: The decoder must have the ``CodingUserInfoKey/actorSystemKey`` set to

the [ActorSystem](actorsystem-swift.associatedtype.md) that this actor expects, as it will be used to call [resolve(id:using:)](<resolve(id_using_).md>) on, in order to obtain the instance this initializer should return.

> [!danger] Throws
> If the actor system value in `decoder.userInfo` is missing or mistyped; the `ID` fails to decode from the passed `decoder`;
