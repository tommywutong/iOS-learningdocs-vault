---
title: 'requireEncryptedNameResolution(_:fallbackResolver:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparameters/privacycontext/requireencryptednameresolution(_:fallbackresolver:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/requireencryptednameresolution(_:fallbackresolver:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/requireencryptednameresolution%28_%3Afallbackresolver%3A%29.json'
content_hash: 'sha256:06b9ac93f56b54b9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [PrivacyContext](../privacycontext.md)

# requireEncryptedNameResolution(_:fallbackResolver:)

<sub>Instance Method</sub>

Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func requireEncryptedNameResolution(_ requireEncryption: Bool, fallbackResolver: NWParameters.PrivacyContext.ResolverConfiguration?)
```

## Parameters

- `requireEncryption` — A Boolean that indicates whether your connections prohibits unencrypted name resolution.

- `fallbackResolver` — An encrypted DNS resolver configuration that your connections use if the system doesn’t have a preferred encrypted resolver.

## Discussion

Connections that use iCloud Private Relay automatically use encrypted name resolution. When active, name resolution uses iCloud Private Relay instead of the `fallbackResolver`.

## See Also

### Requiring Encrypted DNS

- [ResolverConfiguration](resolverconfiguration.md) — A DNS server configuration that uses TLS or HTTPS.
