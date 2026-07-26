---
title: tlsMaximumSupportedProtocolVersion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/tlsmaximumsupportedprotocolversion
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/tlsmaximumsupportedprotocolversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/tlsmaximumsupportedprotocolversion.json'
content_hash: 'sha256:87e3b1ca63e9cf52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# tlsMaximumSupportedProtocolVersion

<sub>Instance Property</sub>

The maximum TLS protocol version that the client should request when making connections in this session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tlsMaximumSupportedProtocolVersion: tls_protocol_version_t { get set }
```

## See Also

### Setting security policies

- [TLSMinimumSupportedProtocolVersion](tlsminimumsupportedprotocolversion.md) — The minimum TLS protocol version that the client should accept when making connections in this session.
- [URLCredentialStorage](urlcredentialstorage.md) — A credential store that provides credentials for authentication.
- [TLSMinimumSupportedProtocol](tlsminimumsupportedprotocol.md) — The minimum TLS protocol to accept during protocol negotiation. _(deprecated)_
- [TLSMaximumSupportedProtocol](tlsmaximumsupportedprotocol.md) — The maximum TLS protocol version that the client should request when making connections in this session. _(deprecated)_
- [requiresDNSSECValidation](requiresdnssecvalidation.md)
