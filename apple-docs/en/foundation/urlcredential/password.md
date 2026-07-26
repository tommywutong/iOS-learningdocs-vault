---
title: password
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/password
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/password'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/password.json'
content_hash: 'sha256:f86385a1442fe242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# password

<sub>Instance Property</sub>

The credential’s password.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var password: String? { get }
```

## Discussion

You should only access this property if you need the actual password value. If you only need to know if there is a password, use [hasPassword](haspassword.md). Accessing this property may result in prompting the user for access—for example, if the password is stored in the user’s keychain.

## See Also

### Getting credential properties

- [user](user.md) — The credential’s user name.
- [certificates](certificates.md) — The intermediate certificates of the credential, if it is a client certificate credential.
- [hasPassword](haspassword.md) — A Boolean value that indicates whether the credential has a password.
- [identity](identity.md) — The identity of this credential if it is a client certificate credential.
- [persistence](persistence-swift.property.md) — The credential’s persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
