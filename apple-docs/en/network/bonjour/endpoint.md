---
title: Bonjour.Endpoint
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/bonjour/endpoint
source_url: 'https://developer.apple.com/documentation/network/bonjour/endpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/bonjour/endpoint.json'
content_hash: 'sha256:9ed6d7572f67f297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [Bonjour](../bonjour.md)

# Bonjour.Endpoint

<sub>Structure</sub>

An endpoint for a discovered Bonjour service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Endpoint
```

## Relationships

- **Conforms To**: [Connectable](../connectable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Identifiable](../../swift/identifiable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<endpoint/==(____).md>) — Compare two endpoints for equality.

### Instance Properties

- [description](endpoint/description.md) — A description of this endpoint to be used for logging and debugging purposes.
- [domain](endpoint/domain.md) — The Bonjour domain of the endpoint.
- [id](endpoint/id.md) — A unique identifer for the endpoint.
- [name](endpoint/name.md) — The Bonjour name of the endpoint.
- [nwEndpoint](endpoint/nwendpoint.md) — The NWEndpoint to use when connecting to this result.
- [result](endpoint/result.md) — A snapshot of the endpoint at some point in time on the network.
- [txtRecord](endpoint/txtrecord.md) — TXT records provide additional information about an endpoint during advertisement or discovery.
- [type](endpoint/type.md) — The Bonjour type of the endpoint.
