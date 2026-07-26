---
title: Stream Status Constants
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream_status_constants
source_url: 'https://developer.apple.com/documentation/foundation/stream_status_constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream_status_constants.json'
content_hash: 'sha256:95babd18140eb624'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Streams, Sockets, and Ports](streams-sockets-and-ports.md) · [Stream](stream.md)

# Stream Status Constants

<sub>API Collection</sub>

These constants indicate the current status of a stream. They are returned by [streamStatus](stream/streamstatus.md).

## Topics

### Constants

- [NSStreamStatusNotOpen](stream/status/notopen.md) — The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [NSStreamStatusOpening](stream/status/opening.md) — The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [NSStreamStatusOpen](stream/status/open.md) — The stream is open, but no reading or writing is occurring.
- [NSStreamStatusReading](stream/status/reading.md) — Data is being read from the stream. This status would be returned if code on another thread were to call [streamStatus](stream/streamstatus.md) on the stream while a [- read:maxLength:](<inputstream/read(__maxlength_).md>) call ([InputStream](inputstream.md)) was in progress.
- [NSStreamStatusWriting](stream/status/writing.md) — Data is being written to the stream. This status would be returned if code on another thread were to call [streamStatus](stream/streamstatus.md) on the stream while a [- write:maxLength:](<outputstream/write(__maxlength_).md>) call ([OutputStream](outputstream.md)) was in progress.
- [NSStreamStatusAtEnd](stream/status/atend.md) — There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [NSStreamStatusClosed](stream/status/closed.md) — The stream is closed ([- close](<stream/close().md>) has been called on it).
- [NSStreamStatusError](stream/status/error.md) — The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.

## See Also

### Constants

- [Status](stream/status.md) — The type declared for the constants listed in doc:stream/stream_status_constants.
- [Event](stream/event.md) — Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) to specify the kind of stream event.
- [StreamNetworkServiceTypeValue](streamnetworkservicetypevalue.md) — `NSStream` defines these string constants for specifying the service type of a stream.
- [StreamSOCKSProxyConfiguration](streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [PropertyKey](stream/propertykey.md) — `NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<stream/property(forkey_).md>) and setting properties with [- setProperty:forKey:](<stream/setproperty(__forkey_).md>):
- [NSStreamSocketSSLErrorDomain](nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
