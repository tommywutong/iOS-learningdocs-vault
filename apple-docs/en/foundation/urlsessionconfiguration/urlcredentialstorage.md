---
title: urlCredentialStorage
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/urlcredentialstorage
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/urlcredentialstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/urlcredentialstorage.json'
content_hash: 'sha256:f93b9365fa79bc6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# urlCredentialStorage

<sub>Instance Property</sub>

A credential store that provides credentials for authentication.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var urlCredentialStorage: URLCredentialStorage? { get set }
```

## Discussion

This property determines the credential storage object used by tasks within sessions based on this configuration.

If you don’t want to use a credential store, set this property to `nil`.

For default and background sessions, the default value is the [sharedCredentialStorage](../urlcredentialstorage/shared.md) credential store object.

For [ephemeralSessionConfiguration](ephemeral.md) sessions, the default value is a private credential store object that stores data in memory only, and is destroyed when you invalidate the session.

## See Also

### Setting security policies

- [TLSMinimumSupportedProtocolVersion](tlsminimumsupportedprotocolversion.md) — The minimum TLS protocol version that the client should accept when making connections in this session.
- [TLSMaximumSupportedProtocolVersion](tlsmaximumsupportedprotocolversion.md) — The maximum TLS protocol version that the client should request when making connections in this session.
- [TLSMinimumSupportedProtocol](tlsminimumsupportedprotocol.md) — The minimum TLS protocol to accept during protocol negotiation. _(deprecated)_
- [TLSMaximumSupportedProtocol](tlsmaximumsupportedprotocol.md) — The maximum TLS protocol version that the client should request when making connections in this session. _(deprecated)_
- [requiresDNSSECValidation](requiresdnssecvalidation.md)
