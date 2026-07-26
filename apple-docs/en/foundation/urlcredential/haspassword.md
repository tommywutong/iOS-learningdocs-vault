---
title: hasPassword
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/haspassword
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/haspassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/haspassword.json'
content_hash: 'sha256:b37fdb74b6bc5914'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# hasPassword

<sub>Instance Property</sub>

A Boolean value that indicates whether the credential has a password.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasPassword: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) if the receiver has a password, [false](../../swift/false.md) otherwise.

This method does not attempt to retrieve the password.

If this credential’s password is stored in the user’s keychain, [password](password.md) may return `nil` even if this method returns [true](../../swift/true.md)—getting the password may fail, or the user may refuse access.

## See Also

### Getting credential properties

- [user](user.md) — The credential’s user name.
- [certificates](certificates.md) — The intermediate certificates of the credential, if it is a client certificate credential.
- [password](password.md) — The credential’s password.
- [identity](identity.md) — The identity of this credential if it is a client certificate credential.
- [persistence](persistence-swift.property.md) — The credential’s persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
