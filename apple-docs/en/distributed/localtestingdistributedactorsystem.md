---
title: LocalTestingDistributedActorSystem
framework: Distributed
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/localtestingdistributedactorsystem
source_url: 'https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/localtestingdistributedactorsystem.json'
content_hash: 'sha256:918b849232343edf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# LocalTestingDistributedActorSystem

<sub>Class</sub>

A `DistributedActorSystem` designed for local only testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class LocalTestingDistributedActorSystem
```

## Overview

It will crash on any attempt of remote communication, but can be useful for learning about `distributed actor` isolation, as well as early prototyping stages of development where a real system is not necessary yet.

## Relationships

- **Conforms To**: [DistributedActorSystem](distributedactorsystem.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<localtestingdistributedactorsystem/init().md>)

## See Also

### Local Testing

- [LocalTestingActorID](localtestingactorid.md)
- [LocalTestingActorAddress](localtestingactoraddress.md) _(deprecated)_
- [LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)
