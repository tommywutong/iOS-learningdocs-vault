---
title: NetService.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/netservice/options
source_url: 'https://developer.apple.com/documentation/foundation/netservice/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/options.json'
content_hash: 'sha256:149b3da7e4f05374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# NetService.Options

<sub>Structure</sub>

These constants specify options for a network service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSNetServiceNoAutoRename](options/noautorename.md) — Specifies that the network service should not rename itself in the event of a name collision.
- [NSNetServiceListenForConnections](options/listenforconnections.md)

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

## See Also

### Constants

- [NSNetServices Errors](../nsnetservices-errors.md) — If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [ErrorCode](errorcode-swift.enum.md) — These constants identify errors that can occur when accessing net services.
