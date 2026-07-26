---
title: StreamSOCKSProxyVersion
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/streamsocksproxyversion
source_url: 'https://developer.apple.com/documentation/foundation/streamsocksproxyversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/streamsocksproxyversion.json'
content_hash: 'sha256:4b5f524c6df7275d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# StreamSOCKSProxyVersion

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StreamSOCKSProxyVersion
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSStreamSOCKSProxyVersion4](streamsocksproxyversion/version4.md) — Possible value for `NSStreamSOCKSProxyVersionKey`.
- [NSStreamSOCKSProxyVersion5](streamsocksproxyversion/version5.md) — Possible value for `NSStreamSOCKSProxyVersionKey`.

### Initializers

- [init(rawValue:)](<streamsocksproxyversion/init(rawvalue_).md>)

## See Also

### Constants

- [Status](stream/status.md) — The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](stream_status_constants.md) — These constants indicate the current status of a stream. They are returned by [streamStatus](stream/streamstatus.md).
- [Event](stream/event.md) — Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) to specify the kind of stream event.
- [StreamNetworkServiceTypeValue](streamnetworkservicetypevalue.md) — `NSStream` defines these string constants for specifying the service type of a stream.
- [StreamSOCKSProxyConfiguration](streamsocksproxyconfiguration.md)
- [StreamSocketSecurityLevel](streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [PropertyKey](stream/propertykey.md) — `NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<stream/property(forkey_).md>) and setting properties with [- setProperty:forKey:](<stream/setproperty(__forkey_).md>):
- [NSStreamSocketSSLErrorDomain](nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
