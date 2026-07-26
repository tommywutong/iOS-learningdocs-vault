---
title: certificates
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/certificates
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/certificates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/certificates.json'
content_hash: 'sha256:0dced0cbe33dbdec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# certificates

<sub>Instance Property</sub>

The intermediate certificates of the credential, if it is a client certificate credential.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var certificates: [Any] { get }
```

## Discussion

The certificates are [SecCertificate](../../security/seccertificate.md) objects representing the intermediate certificates of the credential. This value is `nil` if this is not a client certificate credential or if the credential was created with no intermediate certificates.

## See Also

### Getting credential properties

- [user](user.md) — The credential’s user name.
- [hasPassword](haspassword.md) — A Boolean value that indicates whether the credential has a password.
- [password](password.md) — The credential’s password.
- [identity](identity.md) — The identity of this credential if it is a client certificate credential.
- [persistence](persistence-swift.property.md) — The credential’s persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
