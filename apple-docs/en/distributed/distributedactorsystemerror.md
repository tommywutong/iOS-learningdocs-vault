---
title: DistributedActorSystemError
framework: Distributed
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/distributedactorsystemerror
source_url: 'https://developer.apple.com/documentation/distributed/distributedactorsystemerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/distributedactorsystemerror.json'
content_hash: 'sha256:66a49a97f19f2124'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# DistributedActorSystemError

<sub>Protocol</sub>

Error protocol to which errors thrown by any `DistributedActorSystem` should conform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DistributedActorSystemError : Error
```

## Relationships

- **Inherits From**: [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DistributedActorCodingError](distributedactorcodingerror.md), [ExecuteDistributedTargetError](executedistributedtargeterror.md), [LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)

## See Also

### Errors

- [DistributedActorCodingError](distributedactorcodingerror.md) — Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [ExecuteDistributedTargetError](executedistributedtargeterror.md) — Error thrown by [executeDistributedTarget(on:target:invocationDecoder:handler:)](<distributedactorsystem/executedistributedtarget(on_target_invocationdecoder_handler_).md>).
- [LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)
