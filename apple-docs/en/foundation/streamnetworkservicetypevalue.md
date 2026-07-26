---
title: StreamNetworkServiceTypeValue
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/streamnetworkservicetypevalue
source_url: 'https://developer.apple.com/documentation/foundation/streamnetworkservicetypevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/streamnetworkservicetypevalue.json'
content_hash: 'sha256:c866ff2d6045221f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# StreamNetworkServiceTypeValue

<sub>Structure</sub>

`NSStream` defines these string constants for specifying the service type of a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StreamNetworkServiceTypeValue
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSStreamNetworkServiceTypeBackground](streamnetworkservicetypevalue/background.md) — Specifies that the stream is providing a background service.
- [NSStreamNetworkServiceTypeVideo](streamnetworkservicetypevalue/video.md) — Specifies that the stream is providing video service.
- [NSStreamNetworkServiceTypeVoice](streamnetworkservicetypevalue/voice.md) — Specifies that the stream is providing voice service.
- [NSStreamNetworkServiceTypeVoIP](streamnetworkservicetypevalue/voip.md) — Specifies that the stream is providing VoIP service. _(deprecated)_
- [NSStreamNetworkServiceTypeCallSignaling](streamnetworkservicetypevalue/callsignaling.md)

### Initializers

- [init(rawValue:)](<streamnetworkservicetypevalue/init(rawvalue_).md>)

## See Also

### Constants

- [Status](stream/status.md) — The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](stream_status_constants.md) — These constants indicate the current status of a stream. They are returned by [streamStatus](stream/streamstatus.md).
- [Event](stream/event.md) — Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) to specify the kind of stream event.
- [StreamSOCKSProxyConfiguration](streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [PropertyKey](stream/propertykey.md) — `NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<stream/property(forkey_).md>) and setting properties with [- setProperty:forKey:](<stream/setproperty(__forkey_).md>):
- [NSStreamSocketSSLErrorDomain](nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
