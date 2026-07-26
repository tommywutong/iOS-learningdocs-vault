---
title: receivesCredentialSecurely
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotectionspace/receivescredentialsecurely
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace/receivescredentialsecurely'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace/receivescredentialsecurely.json'
content_hash: 'sha256:e793f33d98df5e6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# receivesCredentialSecurely

<sub>Instance Property</sub>

A Boolean value that indicates whether the credentials for the protection space can be sent securely.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var receivesCredentialSecurely: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) if the credentials for the protection space represented by the receiver can be sent securely, [false](../../swift/false.md) otherwise.

## See Also

### Getting protection space properties

- [authenticationMethod](authenticationmethod.md) — The authentication method used by the receiver.
- [distinguishedNames](distinguishednames.md) — The acceptable certificate-issuing authorities for client certificate authentication.
- [host](host.md) — The receiver’s host.
- [port](port.md) — The receiver’s port.
- [protocol](protocol.md) — The receiver’s protocol.
- [proxyType](proxytype.md) — The receiver’s proxy type.
- [realm](realm.md) — The receiver’s authentication realm
- [serverTrust](servertrust.md) — A representation of the server’s SSL transaction state.
