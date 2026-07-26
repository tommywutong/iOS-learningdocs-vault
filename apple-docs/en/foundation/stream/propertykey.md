---
title: Stream.PropertyKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/propertykey
source_url: 'https://developer.apple.com/documentation/foundation/stream/propertykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/propertykey.json'
content_hash: 'sha256:716221d93a6cf014'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# Stream.PropertyKey

<sub>Structure</sub>

`NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<property(forkey_).md>) and setting properties with [- setProperty:forKey:](<setproperty(__forkey_).md>):

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PropertyKey
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSStreamDataWrittenToMemoryStreamKey](propertykey/datawrittentomemorystreamkey.md) — Value is an `NSData` instance containing the data written to a memory stream.
- [NSStreamFileCurrentOffsetKey](propertykey/filecurrentoffsetkey.md) — Value is an `NSNumber` object containing the current absolute offset of the stream.
- [NSStreamNetworkServiceType](propertykey/networkservicetype.md) — The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [NSStreamSocketSecurityLevelKey](propertykey/socketsecuritylevelkey.md)
- [NSStreamSOCKSProxyConfigurationKey](propertykey/socksproxyconfigurationkey.md) — Value is an `NSDictionary` object containing SOCKS proxy configuration information.

### Initializers

- [init(_:)](<propertykey/init(__).md>)
- [init(rawValue:)](<propertykey/init(rawvalue_).md>)

## See Also

### Constants

- [Status](status.md) — The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](../stream_status_constants.md) — These constants indicate the current status of a stream. They are returned by [streamStatus](streamstatus.md).
- [Event](event.md) — Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<../streamdelegate/stream(__handle_).md>) to specify the kind of stream event.
- [StreamNetworkServiceTypeValue](../streamnetworkservicetypevalue.md) — `NSStream` defines these string constants for specifying the service type of a stream.
- [StreamSOCKSProxyConfiguration](../streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](../streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](../streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [NSStreamSocketSSLErrorDomain](../nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](../nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
