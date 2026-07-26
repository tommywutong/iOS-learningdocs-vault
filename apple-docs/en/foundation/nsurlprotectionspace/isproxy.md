---
title: isProxy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlprotectionspace/isproxy
source_url: 'https://developer.apple.com/documentation/foundation/nsurlprotectionspace/isproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlprotectionspace/isproxy.json'
content_hash: 'sha256:24dc65192425f5cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# isProxy

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver represents a proxy server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) BOOL isProxy;
```

## Discussion

[true](../../swift/true.md) if the receiver represents a proxy server, [false](../../swift/false.md) otherwise.

## See Also

### Getting protection space properties

- [authenticationMethod](../urlprotectionspace/authenticationmethod.md) — The authentication method used by the receiver.
- [distinguishedNames](../urlprotectionspace/distinguishednames.md) — The acceptable certificate-issuing authorities for client certificate authentication.
- [host](../urlprotectionspace/host.md) — The receiver’s host.
- [port](../urlprotectionspace/port.md) — The receiver’s port.
- [protocol](../urlprotectionspace/protocol.md) — The receiver’s protocol.
- [proxyType](../urlprotectionspace/proxytype.md) — The receiver’s proxy type.
- [realm](../urlprotectionspace/realm.md) — The receiver’s authentication realm
- [receivesCredentialSecurely](../urlprotectionspace/receivescredentialsecurely.md) — A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [serverTrust](../urlprotectionspace/servertrust.md) — A representation of the server’s SSL transaction state.
