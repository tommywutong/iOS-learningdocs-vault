---
title: 'missingActorSystemUserInfo(_:)'
framework: Distributed
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/distributed/distributedactorcodingerror/missingactorsystemuserinfo(_:)'
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorcodingerror/missingactorsystemuserinfo(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorcodingerror/missingactorsystemuserinfo%28_%3A%29.json'
content_hash: 'sha256:0958c42cb5c6bd73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [DistributedActorCodingError](../distributedactorcodingerror.md)

# missingActorSystemUserInfo(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func missingActorSystemUserInfo<Act>(_ actorType: Act.Type) -> DistributedActorCodingError where Act : DistributedActor
```
