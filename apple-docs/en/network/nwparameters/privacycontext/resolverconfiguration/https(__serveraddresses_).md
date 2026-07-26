---
title: 'NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparameters/privacycontext/resolverconfiguration/https(_:serveraddresses:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/resolverconfiguration/https(_:serveraddresses:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/resolverconfiguration/https%28_%3Aserveraddresses%3A%29.json'
content_hash: 'sha256:77fb10eabc5e923e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWParameters](../../../nwparameters.md) · [PrivacyContext](../../privacycontext.md) · [ResolverConfiguration](../resolverconfiguration.md)

# NWParameters.PrivacyContext.ResolverConfiguration.https(_:serverAddresses:)

<sub>Case</sub>

A DNS-over-HTTPS resolver configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case https(URL, serverAddresses: [NWEndpoint])
```

## Discussion

The URL describes the location of the DNS server, such as “https://dnsserver.example.net/dns-query”. See [RFC 8484](https://tools.ietf.org/html/rfc8484) for more details. The associated server addresses you provide are hints for which well-known DNS server addresses to use.

## See Also

### Resolver Types

- [NWParameters.PrivacyContext.ResolverConfiguration.tls(_:serverAddresses:)](<tls(__serveraddresses_).md>) — A DNS-over-TLS resolver configuration.
