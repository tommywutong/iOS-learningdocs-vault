---
title: NWParameters.PrivacyContext.ResolverConfiguration
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/privacycontext/resolverconfiguration
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/resolverconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/resolverconfiguration.json'
content_hash: 'sha256:608862c03f7d6b1e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [PrivacyContext](../privacycontext.md)

# NWParameters.PrivacyContext.ResolverConfiguration

<sub>Enumeration</sub>

A DNS server configuration that uses TLS or HTTPS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ResolverConfiguration
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Resolver Types

- [NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)](<resolverconfiguration/https(__serveraddresses_).md>) — A DNS-over-HTTPS resolver configuration.
- [NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)](<resolverconfiguration/tls(__serveraddresses_).md>) — A DNS-over-TLS resolver configuration.

## See Also

### Requiring Encrypted DNS

- [requireEncryptedNameResolution(_:fallbackResolver:)](<requireencryptednameresolution(__fallbackresolver_).md>) — Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
