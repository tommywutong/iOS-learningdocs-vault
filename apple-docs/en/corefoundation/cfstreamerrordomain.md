---
title: CFStreamErrorDomain
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamerrordomain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamerrordomain.json'
content_hash: 'sha256:72acdf1e1e4004c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamErrorDomain

<sub>Enumeration</sub>

Defines constants for values returned in the domain field of the `CFStreamError` structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFStreamErrorDomain
```

## Overview

These constants indicate how the error code in the `error` field in the [CFStreamError](cfstreamerror.md) structure should be interpreted.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFStreamErrorDomainCustom](cfstreamerrordomain/custom.md) — The error code is a custom error code. _(deprecated)_
- [kCFStreamErrorDomainPOSIX](cfstreamerrordomain/posix.md) — The error code is an error code defined in `errno.h`.
- [kCFStreamErrorDomainMacOSStatus](cfstreamerrordomain/macosstatus.md) — The error is an OSStatus value defined in `MacErrors.h`.

### Initializers

- [init(rawValue:)](<cfstreamerrordomain/init(rawvalue_).md>)

## See Also

### Constants

- [CFStreamStatus](cfstreamstatus.md) — Constants that describe the status of a stream.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md) — Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [CFStreamEventType](cfstreameventtype.md) — Defines constants for stream-related events.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md) — Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md) — Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.
