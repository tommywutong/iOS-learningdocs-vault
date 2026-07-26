---
title: distinguishedNames
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotectionspace/distinguishednames
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace/distinguishednames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace/distinguishednames.json'
content_hash: 'sha256:33ab0322756b3552'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# distinguishedNames

<sub>Instance Property</sub>

The acceptable certificate-issuing authorities for client certificate authentication.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var distinguishedNames: [Data]? { get }
```

## Discussion

This value is `nil` if the authentication method of the protection space is not client certificate. The returned issuing authorities are encoded with Distinguished Encoding Rules (DER).

## See Also

### Getting protection space properties

- [authenticationMethod](authenticationmethod.md) — The authentication method used by the receiver.
- [host](host.md) — The receiver’s host.
- [port](port.md) — The receiver’s port.
- [protocol](protocol.md) — The receiver’s protocol.
- [proxyType](proxytype.md) — The receiver’s proxy type.
- [realm](realm.md) — The receiver’s authentication realm
- [receivesCredentialSecurely](receivescredentialsecurely.md) — A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [serverTrust](servertrust.md) — A representation of the server’s SSL transaction state.
