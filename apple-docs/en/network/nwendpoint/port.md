---
title: NWEndpoint.Port
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwendpoint/port
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/port.json'
content_hash: 'sha256:ca7fae5bf11859b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# NWEndpoint.Port

<sub>Structure</sub>

A port number you use along with a host to identify a network endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Port
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [ExpressibleByIntegerLiteral](../../swift/expressiblebyintegerliteral.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Ports

- [init(_:)](<port/init(__).md>) — Initializes a port with a string.

### Setting Well-Known Ports

- [any](port/any.md) — The unspecified port (port 0).
- [ssh](port/ssh.md) — The Secure Shell port (port 22).
- [smtp](port/smtp.md) — The Simple Mail Transfer Protocol port (port 25).
- [http](port/http.md) — The Hypertext Transfer Protocol port (port 80).
- [pop](port/pop.md) — The Post Office Protocol port (port 110).
- [imap](port/imap.md) — The Internet Message Access Protocol port (port 143).
- [https](port/https.md) — The Secure Hypertext Transfer Protocol port (port 443).
- [imaps](port/imaps.md) — The Secure Internet Message Access Protocol port (port 993).
- [socks](port/socks.md) — The SOCKS proxy protocol port (port 1080).

## See Also

### Host and Ports

- [Host](host.md) — A name or address that identifies a network endpoint.
