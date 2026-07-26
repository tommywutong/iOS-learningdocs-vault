---
title: realm
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotectionspace/realm
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace/realm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace/realm.json'
content_hash: 'sha256:a47e19d84d8c60e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# realm

<sub>Instance Property</sub>

The receiver’s authentication realm

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var realm: String? { get }
```

## Discussion

This value is `nil` if no realm has been set. A realm is generally only specified for HTTP and HTTPS authentication.

## See Also

### Getting protection space properties

- [authenticationMethod](authenticationmethod.md) — The authentication method used by the receiver.
- [distinguishedNames](distinguishednames.md) — The acceptable certificate-issuing authorities for client certificate authentication.
- [host](host.md) — The receiver’s host.
- [port](port.md) — The receiver’s port.
- [protocol](protocol.md) — The receiver’s protocol.
- [proxyType](proxytype.md) — The receiver’s proxy type.
- [receivesCredentialSecurely](receivescredentialsecurely.md) — A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [serverTrust](servertrust.md) — A representation of the server’s SSL transaction state.
