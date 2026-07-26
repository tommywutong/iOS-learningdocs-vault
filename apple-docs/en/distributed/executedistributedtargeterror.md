---
title: ExecuteDistributedTargetError
framework: Distributed
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/executedistributedtargeterror
source_url: 'https://developer.apple.com/documentation/distributed/executedistributedtargeterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/executedistributedtargeterror.json'
content_hash: 'sha256:163f2d6ed0d94f7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# ExecuteDistributedTargetError

<sub>Structure</sub>

Error thrown by [executeDistributedTarget(on:target:invocationDecoder:handler:)](<distributedactorsystem/executedistributedtarget(on_target_invocationdecoder_handler_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ExecuteDistributedTargetError
```

## Overview

Inspect the [errorCode](executedistributedtargeterror/errorcode-swift.property.md) for details about the underlying reason this error was thrown.

## Relationships

- **Conforms To**: [DistributedActorSystemError](distributedactorsystemerror.md), [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(message:)](<executedistributedtargeterror/init(message_).md>)
- [init(message:errorCode:)](<executedistributedtargeterror/init(message_errorcode_).md>)

### Instance Properties

- [errorCode](executedistributedtargeterror/errorcode-swift.property.md)
- [message](executedistributedtargeterror/message.md)

### Enumerations

- [ErrorCode](executedistributedtargeterror/errorcode-swift.enum.md)

## See Also

### Errors

- [DistributedActorCodingError](distributedactorcodingerror.md) — Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [DistributedActorSystemError](distributedactorsystemerror.md) — Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)
