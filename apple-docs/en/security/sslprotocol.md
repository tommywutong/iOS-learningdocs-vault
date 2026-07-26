---
title: SSLProtocol
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslprotocol
source_url: 'https://developer.apple.com/documentation/security/sslprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslprotocol.json'
content_hash: 'sha256:819761da4e23cb8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLProtocol

<sub>Enumeration</sub>

An enumeration of valid SSL protocol versions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SSLProtocol
```

## Overview

The descriptions given here apply to the functions [SSLSetProtocolVersion](sslsetprotocolversion.md) and [SSLGetProtocolVersion](sslgetprotocolversion.md). For the functions [SSLSetProtocolVersionEnabled](sslsetprotocolversionenabled.md) and [SSLGetProtocolVersionEnabled](sslgetprotocolversionenabled.md), only the following values are used. For these functions, each constant except [kSSLProtocolAll](sslprotocol/sslprotocolall.md) specifies a single protocol version.

- [kSSLProtocol2](sslprotocol/sslprotocol2.md)
- [kSSLProtocol3](sslprotocol/sslprotocol3.md)
- [kTLSProtocol1](sslprotocol/tlsprotocol1.md)
- [kSSLProtocolAll](sslprotocol/sslprotocolall.md)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### SSL Protocols

- [kSSLProtocolUnknown](sslprotocol/sslprotocolunknown.md) — Specifies that no protocol has been or should be negotiated or specified; use default. _(deprecated)_
- [kSSLProtocol2](sslprotocol/sslprotocol2.md) — Specifies that only the SSL 2.0 protocol may be negotiated. Deprecated in iOS. _(deprecated)_
- [kSSLProtocol3](sslprotocol/sslprotocol3.md) — Specifies that the SSL 3.0 protocol is preferred; the SSL 2.0 protocol may be negotiated if the peer cannot use the SSL 3.0 protocol. _(deprecated)_
- [kSSLProtocol3Only](sslprotocol/sslprotocol3only.md) — Specifies that only the SSL 3.0 protocol may be negotiated; fails if the peer tries to negotiate the SSL 2.0 protocol. Deprecated in iOS. _(deprecated)_
- [kSSLProtocolAll](sslprotocol/sslprotocolall.md) — Specifies all supported versions. Deprecated in iOS. _(deprecated)_

### TLS Protocols

- [kTLSProtocol1](sslprotocol/tlsprotocol1.md) — Specifies that the TLS 1.0 protocol is preferred but lower versions may be negotiated. _(deprecated)_
- [kTLSProtocol1Only](sslprotocol/tlsprotocol1only.md) — Specifies that only the TLS 1.0 protocol may be negotiated. Deprecated in iOS. _(deprecated)_
- [kTLSProtocol11](sslprotocol/tlsprotocol11.md) — Specifies that the TLS 1.1 protocol is preferred but lower versions may be negotiated. _(deprecated)_
- [kTLSProtocol12](sslprotocol/tlsprotocol12.md) — Specifies that the TLS 1.2 protocol is preferred but lower versions may be negotiated. _(deprecated)_
- [kTLSProtocol13](sslprotocol/tlsprotocol13.md) — Specifies that the TLS 1.3 protocol is preferred but lower versions may be negotiated. _(deprecated)_
- [kTLSProtocolMaxSupported](sslprotocol/tlsprotocolmaxsupported.md) — The maximum system supported version. _(deprecated)_

### DTLS Protocols

- [kDTLSProtocol1](sslprotocol/dtlsprotocol1.md) — Specifies the DTLS 1.0 protocol. _(deprecated)_
- [kDTLSProtocol12](sslprotocol/dtlsprotocol12.md) — Specifies the DTLS 1.2 protocol. _(deprecated)_

### Initializers

- [init(rawValue:)](<sslprotocol/init(rawvalue_).md>)
