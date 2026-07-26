---
title: 'NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparameters/privacycontext/resolverconfiguration/tls(_:serveraddresses:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/resolverconfiguration/tls(_:serveraddresses:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/resolverconfiguration/tls%28_%3Aserveraddresses%3A%29.json'
content_hash: 'sha256:07ab824c9388c7d7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWParameters](../../../nwparameters.md) · [PrivacyContext](../../privacycontext.md) · [ResolverConfiguration](../resolverconfiguration.md)

# NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)

<sub>Case</sub>

A DNS-over-TLS resolver configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case tls(NWEndpoint, serverAddresses: [NWEndpoint])
```

## Discussion

The hostname of the provided endpoint will be used to validate the TLS certificate of the server. See [RFC 7858](https://tools.ietf.org/html/rfc7858) for more details. The associated server addresses you provide are hints for which well-known DNS server addresses to use.

## See Also

### Resolver Types

- [NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)](<https(__serveraddresses_).md>) — A DNS-over-HTTPS resolver configuration.
