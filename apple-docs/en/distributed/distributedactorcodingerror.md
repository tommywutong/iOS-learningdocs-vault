---
title: DistributedActorCodingError
framework: Distributed
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorcodingerror
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorcodingerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorcodingerror.json'
content_hash: 'sha256:b51f40e33392c30d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# DistributedActorCodingError

<sub>Structure</sub>

Error thrown by distributed actor systems while encountering encoding/decoding issues.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DistributedActorCodingError
```

## Overview

Also thrown when an attempt to decode [DistributedActor](distributedactor.md) is made, but no [DistributedActorSystem](distributedactorsystem.md) is available in the `Decoder`’s `userInfo[.actorSystemKey]`, as it is required to perform the resolve call.

## Relationships

- **Conforms To**: [DistributedActorSystemError](distributedactorsystemerror.md), [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(message:)](<distributedactorcodingerror/init(message_).md>)

### Instance Properties

- [message](distributedactorcodingerror/message.md)

### Type Methods

- [missingActorSystemUserInfo(_:)](<distributedactorcodingerror/missingactorsystemuserinfo(__).md>)

## See Also

### Errors

- [DistributedActorSystemError](distributedactorsystemerror.md) — Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [ExecuteDistributedTargetError](executedistributedtargeterror.md) — Error thrown by [executeDistributedTarget(on:target:invocationDecoder:handler:)](<distributedactorsystem/executedistributedtarget(on_target_invocationdecoder_handler_).md>).
- [LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)
