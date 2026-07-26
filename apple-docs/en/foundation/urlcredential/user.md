---
title: user
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/user
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/user'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/user.json'
content_hash: 'sha256:fb8b0f361c27d448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# user

<sub>Instance Property</sub>

The credential’s user name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var user: String? { get }
```

## See Also

### Getting credential properties

- [certificates](certificates.md) — The intermediate certificates of the credential, if it is a client certificate credential.
- [hasPassword](haspassword.md) — A Boolean value that indicates whether the credential has a password.
- [password](password.md) — The credential’s password.
- [identity](identity.md) — The identity of this credential if it is a client certificate credential.
- [persistence](persistence-swift.property.md) — The credential’s persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
