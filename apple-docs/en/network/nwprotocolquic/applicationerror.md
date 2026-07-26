---
title: NWProtocolQUIC.ApplicationError
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/applicationerror
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/applicationerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/applicationerror.json'
content_hash: 'sha256:c9cc12d4da64e9c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolQUIC](../nwprotocolquic.md)

# NWProtocolQUIC.ApplicationError

<sub>Structure</sub>

A QUIC application error code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ApplicationError
```

## Relationships

- **Conforms To**: [ExpressibleByIntegerLiteral](../../swift/expressiblebyintegerliteral.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Configuring Application Errors

- [init(code:reason:)](<applicationerror/init(code_reason_).md>) — Initializes a QUIC application error with an error code and an optional reason.

### Inspecting Application Errors

- [code](applicationerror/code.md) — The QUIC application error code.
- [reason](applicationerror/reason.md) — The QUIC application error reason.

## See Also

### Handling Errors

- [applicationError](metadata/applicationerror.md) — The QUIC application error code to send for the connection, or received from the peer.
- [streamApplicationErrorCode](metadata/streamapplicationerrorcode.md) — The QUIC application error code to send for the stream, or received from the peer.
