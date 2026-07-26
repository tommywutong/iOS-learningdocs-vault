---
title: LocalTestingDistributedActorSystemError
framework: Distributed
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/localtestingdistributedactorsystemerror
source_url: 'https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystemerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/localtestingdistributedactorsystemerror.json'
content_hash: 'sha256:9b7303e1c5578f4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# LocalTestingDistributedActorSystemError

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LocalTestingDistributedActorSystemError
```

## Relationships

- **Conforms To**: [DistributedActorSystemError](distributedactorsystemerror.md), [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(message:)](<localtestingdistributedactorsystemerror/init(message_).md>)

### Instance Properties

- [message](localtestingdistributedactorsystemerror/message.md)

## See Also

### Errors

- [DistributedActorCodingError](distributedactorcodingerror.md) — Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [DistributedActorSystemError](distributedactorsystemerror.md) — Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [ExecuteDistributedTargetError](executedistributedtargeterror.md) — Error thrown by [executeDistributedTarget(on:target:invocationDecoder:handler:)](<distributedactorsystem/executedistributedtarget(on_target_invocationdecoder_handler_).md>).
