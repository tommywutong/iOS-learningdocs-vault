---
title: protocol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotectionspace/protocol
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace/protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace/protocol.json'
content_hash: 'sha256:15f3ec8603440730'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# protocol

<sub>Instance Property</sub>

The receiver’s protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var `protocol`: String? { get }
```

## Discussion

This value is `nil` if the receiver represents a proxy protection space.

## See Also

### Getting protection space properties

- [authenticationMethod](authenticationmethod.md) — The authentication method used by the receiver.
- [distinguishedNames](distinguishednames.md) — The acceptable certificate-issuing authorities for client certificate authentication.
- [host](host.md) — The receiver’s host.
- [port](port.md) — The receiver’s port.
- [proxyType](proxytype.md) — The receiver’s proxy type.
- [realm](realm.md) — The receiver’s authentication realm
- [receivesCredentialSecurely](receivescredentialsecurely.md) — A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [serverTrust](servertrust.md) — A representation of the server’s SSL transaction state.
