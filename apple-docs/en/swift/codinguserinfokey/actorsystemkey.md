---
title: actorSystemKey
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/codinguserinfokey/actorsystemkey
source_url: 'https://developer.apple.com/documentation/swift/codinguserinfokey/actorsystemkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codinguserinfokey/actorsystemkey.json'
content_hash: 'sha256:35d971805bdec791'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CodingUserInfoKey](../codinguserinfokey.md)

# actorSystemKey

<sub>Type Property</sub>

Key which is required to be set on a `Decoder`’s `userInfo` while attempting to `init(from:)` a `DistributedActor`. The stored value under this key must conform to `DistributedActorSystem`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let actorSystemKey: CodingUserInfoKey
```

## Discussion

Forgetting to set this key will result in that initializer throwing, because an actor system is required in order to call `DistributedActor/resolve(id:using:)` using it.
