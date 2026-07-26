---
title: LocalTestingActorID
framework: Distributed
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/localtestingactorid
source_url: 'https://developer.apple.com/documentation/distributed/localtestingactorid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/localtestingactorid.json'
content_hash: 'sha256:694850124b6cfefb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Distributed](../distributed.md)

# LocalTestingActorID

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LocalTestingActorID
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(id:)](<localtestingactorid/init(id_).md>)
- [init(parse:)](<localtestingactorid/init(parse_).md>) _(deprecated)_

### Instance Properties

- [address](localtestingactorid/address.md) _(deprecated)_
- [id](localtestingactorid/id.md)

## See Also

### Local Testing

- [LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md) — A `DistributedActorSystem` designed for local only testing.
- [LocalTestingActorAddress](localtestingactoraddress.md) _(deprecated)_
- [LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)
