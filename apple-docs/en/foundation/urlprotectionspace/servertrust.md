---
title: serverTrust
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotectionspace/servertrust
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace/servertrust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace/servertrust.json'
content_hash: 'sha256:d3baab4df5f56070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# serverTrust

<sub>Instance Property</sub>

A representation of the server’s SSL transaction state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var serverTrust: SecTrust? { get }
```

## Discussion

This value is `nil` if the authentication method of the protection space is not server trust.

## See Also

### Getting protection space properties

- [authenticationMethod](authenticationmethod.md) — The authentication method used by the receiver.
- [distinguishedNames](distinguishednames.md) — The acceptable certificate-issuing authorities for client certificate authentication.
- [host](host.md) — The receiver’s host.
- [port](port.md) — The receiver’s port.
- [protocol](protocol.md) — The receiver’s protocol.
- [proxyType](proxytype.md) — The receiver’s proxy type.
- [realm](realm.md) — The receiver’s authentication realm
- [receivesCredentialSecurely](receivescredentialsecurely.md) — A Boolean value that indicates whether the credentials for the protection space can be sent securely.
