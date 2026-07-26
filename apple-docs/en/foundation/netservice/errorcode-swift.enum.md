---
title: NetService.ErrorCode
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/netservice/errorcode-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/netservice/errorcode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/errorcode-swift.enum.json'
content_hash: 'sha256:9ea056f54fcda2f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# NetService.ErrorCode

<sub>Enumeration</sub>

These constants identify errors that can occur when accessing net services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum ErrorCode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSNetServicesUnknownError](errorcode-swift.enum/unknownerror.md) — An unknown error occurred.
- [NSNetServicesCollisionError](errorcode-swift.enum/collisionerror.md) — The service could not be published because the name is already in use. The name could be in use locally or on another system.
- [NSNetServicesNotFoundError](errorcode-swift.enum/notfounderror.md) — The service could not be found on the network.
- [NSNetServicesActivityInProgress](errorcode-swift.enum/activityinprogress.md) — The net service cannot process the request at this time. No additional information about the network state is known.
- [NSNetServicesBadArgumentError](errorcode-swift.enum/badargumenterror.md) — An invalid argument was used when creating the `NSNetService` object.
- [NSNetServicesCancelledError](errorcode-swift.enum/cancellederror.md) — The client canceled the action.
- [NSNetServicesInvalidError](errorcode-swift.enum/invaliderror.md) — The net service was improperly configured.
- [NSNetServicesTimeoutError](errorcode-swift.enum/timeouterror.md) — The net service has timed out.

### Enumeration Cases

- [NSNetServicesMissingRequiredConfigurationError](errorcode-swift.enum/missingrequiredconfigurationerror.md) — Missing required configuration for local network access.

### Initializers

- [init(rawValue:)](<errorcode-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [NSNetServices Errors](../nsnetservices-errors.md) — If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [Options](options.md) — These constants specify options for a network service.
