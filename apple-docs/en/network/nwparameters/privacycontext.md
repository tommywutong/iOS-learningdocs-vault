---
title: NWParameters.PrivacyContext
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/privacycontext
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext.json'
content_hash: 'sha256:00c513cf8ec327e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# NWParameters.PrivacyContext

<sub>Class</sub>

An object that defines the privacy requirements for a set of connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class PrivacyContext
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Configuring Custom Privacy Settings

- [init(description:)](<privacycontext/init(description_).md>) — Initializes a privacy context with a description string.
- [default](privacycontext/default.md) — The privacy context that applies to all connections that do not use a custom context.
- [disableLogging()](<privacycontext/disablelogging().md>) — Disables system logging of connection activity.
- [flushCache()](<privacycontext/flushcache().md>) — Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.

### Requiring Encrypted DNS

- [requireEncryptedNameResolution(_:fallbackResolver:)](<privacycontext/requireencryptednameresolution(__fallbackresolver_).md>) — Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [ResolverConfiguration](privacycontext/resolverconfiguration.md) — A DNS server configuration that uses TLS or HTTPS.

### Configuring Proxies

- [proxyConfigurations](privacycontext/proxyconfigurations.md) — Applies proxy configurations for all connections associated with this context.
- [ProxyConfiguration](../proxyconfiguration.md) — A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

## See Also

### Configuring Privacy Settings

- [setPrivacyContext(_:)](<setprivacycontext(__).md>) — Associates a privacy context with any connections or listeners that use the parameters.
