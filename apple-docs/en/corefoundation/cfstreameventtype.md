---
title: CFStreamEventType
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreameventtype
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreameventtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreameventtype.json'
content_hash: 'sha256:b2c3946a39c8d7cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamEventType

<sub>Structure</sub>

Defines constants for stream-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStreamEventType
```

## Overview

This enumeration defines constants for stream-related events.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFStreamEventOpenCompleted](cfstreameventtype/opencompleted.md) — The open has completed successfully.
- [kCFStreamEventHasBytesAvailable](cfstreameventtype/hasbytesavailable.md) — The stream has bytes to be read.
- [kCFStreamEventCanAcceptBytes](cfstreameventtype/canacceptbytes.md) — The stream can accept bytes for writing.
- [kCFStreamEventErrorOccurred](cfstreameventtype/erroroccurred.md) — An error has occurred on the stream.
- [kCFStreamEventEndEncountered](cfstreameventtype/endencountered.md) — The end of the stream has been reached.

### Initializers

- [init(rawValue:)](<cfstreameventtype/init(rawvalue_).md>)

## See Also

### Constants

- [CFStreamStatus](cfstreamstatus.md) — Constants that describe the status of a stream.
- [CFStreamErrorDomain](cfstreamerrordomain.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md) — Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md) — Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md) — Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.
