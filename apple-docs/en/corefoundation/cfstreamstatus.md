---
title: CFStreamStatus
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamstatus
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamstatus.json'
content_hash: 'sha256:b7bebb65c465148a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamStatus

<sub>Enumeration</sub>

Constants that describe the status of a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFStreamStatus
```

## Overview

The `CFStreamStatus` enumeration defines constants that describe the status of a stream. These values are returned by [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) and [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFStreamStatusNotOpen](cfstreamstatus/notopen.md) — The stream is not open for reading or writing.
- [kCFStreamStatusOpening](cfstreamstatus/opening.md) — The stream is being opened for reading or for writing.
- [kCFStreamStatusOpen](cfstreamstatus/open.md) — The stream is open.
- [kCFStreamStatusReading](cfstreamstatus/reading.md) — The stream is being read from.
- [kCFStreamStatusWriting](cfstreamstatus/writing.md) — The stream is being written to.
- [kCFStreamStatusAtEnd](cfstreamstatus/atend.md) — There is no more data to read, or no more data can be written.
- [kCFStreamStatusClosed](cfstreamstatus/closed.md) — The stream is closed.
- [kCFStreamStatusError](cfstreamstatus/error.md) — An error occurred on the stream.

### Initializers

- [init(rawValue:)](<cfstreamstatus/init(rawvalue_).md>)

## See Also

### Constants

- [CFStreamErrorDomain](cfstreamerrordomain.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md) — Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [CFStreamEventType](cfstreameventtype.md) — Defines constants for stream-related events.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md) — Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md) — Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.
