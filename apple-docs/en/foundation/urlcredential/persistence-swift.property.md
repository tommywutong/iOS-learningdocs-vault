---
title: persistence
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/persistence-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/persistence-swift.property.json'
content_hash: 'sha256:3c5f6e5e59c67226'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# persistence

<sub>Instance Property</sub>

The credential’s persistence setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistence: URLCredential.Persistence { get }
```

## See Also

### Getting credential properties

- [user](user.md) — The credential’s user name.
- [certificates](certificates.md) — The intermediate certificates of the credential, if it is a client certificate credential.
- [hasPassword](haspassword.md) — A Boolean value that indicates whether the credential has a password.
- [password](password.md) — The credential’s password.
- [identity](identity.md) — The identity of this credential if it is a client certificate credential.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
