---
title: identity
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/identity
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/identity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/identity.json'
content_hash: 'sha256:ae2995569bf1dd54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# identity

<sub>Instance Property</sub>

The identity of this credential if it is a client certificate credential.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identity: SecIdentity? { get }
```

## Discussion

This value is `nil` if the credential is not a client certificate credential.

## See Also

### Getting credential properties

- [user](user.md) — The credential’s user name.
- [certificates](certificates.md) — The intermediate certificates of the credential, if it is a client certificate credential.
- [hasPassword](haspassword.md) — A Boolean value that indicates whether the credential has a password.
- [password](password.md) — The credential’s password.
- [persistence](persistence-swift.property.md) — The credential’s persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
