---
title: tlsMaximumSupportedProtocol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessionconfiguration/tlsmaximumsupportedprotocol
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/tlsmaximumsupportedprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/tlsmaximumsupportedprotocol.json'
content_hash: 'sha256:ae932c4b7d395bde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# tlsMaximumSupportedProtocol

<sub>Instance Property</sub>

The maximum TLS protocol version that the client should request when making connections in this session.

> [!warning] Deprecated
> Use [TLSMaximumSupportedProtocolVersion](tlsmaximumsupportedprotocolversion.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tlsMaximumSupportedProtocol: SSLProtocol { get set }
```

## Discussion

This property determines the maximum supported TLS protocol version for tasks within sessions based on this configuration.

## See Also

### Setting security policies

- [TLSMinimumSupportedProtocolVersion](tlsminimumsupportedprotocolversion.md) — The minimum TLS protocol version that the client should accept when making connections in this session.
- [TLSMaximumSupportedProtocolVersion](tlsmaximumsupportedprotocolversion.md) — The maximum TLS protocol version that the client should request when making connections in this session.
- [URLCredentialStorage](urlcredentialstorage.md) — A credential store that provides credentials for authentication.
- [TLSMinimumSupportedProtocol](tlsminimumsupportedprotocol.md) — The minimum TLS protocol to accept during protocol negotiation. _(deprecated)_
- [requiresDNSSECValidation](requiresdnssecvalidation.md)
