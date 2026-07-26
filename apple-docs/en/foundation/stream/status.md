---
title: Stream.Status
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/status
source_url: 'https://developer.apple.com/documentation/foundation/stream/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/status.json'
content_hash: 'sha256:c93231a7989f96f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# Stream.Status

<sub>Enumeration</sub>

The type declared for the constants listed in doc:stream/stream_status_constants.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NSStreamStatusAtEnd](status/atend.md) — There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [NSStreamStatusClosed](status/closed.md) — The stream is closed ([- close](<close().md>) has been called on it).
- [NSStreamStatusError](status/error.md) — The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [NSStreamStatusNotOpen](status/notopen.md) — The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [NSStreamStatusOpen](status/open.md) — The stream is open, but no reading or writing is occurring.
- [NSStreamStatusOpening](status/opening.md) — The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [NSStreamStatusReading](status/reading.md) — Data is being read from the stream. This status would be returned if code on another thread were to call [streamStatus](streamstatus.md) on the stream while a [- read:maxLength:](<../inputstream/read(__maxlength_).md>) call ([InputStream](../inputstream.md)) was in progress.
- [NSStreamStatusWriting](status/writing.md) — Data is being written to the stream. This status would be returned if code on another thread were to call [streamStatus](streamstatus.md) on the stream while a [- write:maxLength:](<../outputstream/write(__maxlength_).md>) call ([OutputStream](../outputstream.md)) was in progress.

### Initializers

- [init(rawValue:)](<status/init(rawvalue_).md>)

## See Also

### Constants

- [Stream Status Constants](../stream_status_constants.md) — These constants indicate the current status of a stream. They are returned by [streamStatus](streamstatus.md).
- [Event](event.md) — Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<../streamdelegate/stream(__handle_).md>) to specify the kind of stream event.
- [StreamNetworkServiceTypeValue](../streamnetworkservicetypevalue.md) — `NSStream` defines these string constants for specifying the service type of a stream.
- [StreamSOCKSProxyConfiguration](../streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](../streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](../streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [PropertyKey](propertykey.md) — `NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<property(forkey_).md>) and setting properties with [- setProperty:forKey:](<setproperty(__forkey_).md>):
- [NSStreamSocketSSLErrorDomain](../nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](../nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
