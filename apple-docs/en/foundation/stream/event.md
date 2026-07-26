---
title: Stream.Event
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/event
source_url: 'https://developer.apple.com/documentation/foundation/stream/event'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/event.json'
content_hash: 'sha256:f666b54f6ab97cef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# Stream.Event

<sub>Structure</sub>

Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<../streamdelegate/stream(__handle_).md>) to specify the kind of stream event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Event
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSStreamEventOpenCompleted](event/opencompleted.md) — The open has completed successfully.
- [NSStreamEventHasBytesAvailable](event/hasbytesavailable.md) — The stream has bytes to be read.
- [NSStreamEventHasSpaceAvailable](event/hasspaceavailable.md) — The stream can accept bytes for writing.
- [NSStreamEventErrorOccurred](event/erroroccurred.md) — An error has occurred on the stream.
- [NSStreamEventEndEncountered](event/endencountered.md) — The end of the stream has been reached.

### Initializers

- [init(rawValue:)](<event/init(rawvalue_).md>)

## See Also

### Constants

- [Status](status.md) — The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](../stream_status_constants.md) — These constants indicate the current status of a stream. They are returned by [streamStatus](streamstatus.md).
- [StreamNetworkServiceTypeValue](../streamnetworkservicetypevalue.md) — `NSStream` defines these string constants for specifying the service type of a stream.
- [StreamSOCKSProxyConfiguration](../streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](../streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](../streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [PropertyKey](propertykey.md) — `NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<property(forkey_).md>) and setting properties with [- setProperty:forKey:](<setproperty(__forkey_).md>):
- [NSStreamSocketSSLErrorDomain](../nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](../nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
