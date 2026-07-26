---
title: SecAuthenticationType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secauthenticationtype
source_url: 'https://developer.apple.com/documentation/security/secauthenticationtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secauthenticationtype.json'
content_hash: 'sha256:4e0d2b0fca2e7db5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAuthenticationType

<sub>Enumeration</sub>

The authentication type to use for an Internet password.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecAuthenticationType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecAuthenticationTypeNTLM](secauthenticationtype/ntlm.md) — Specifies Windows NT LAN Manager authentication.
- [kSecAuthenticationTypeMSN](secauthenticationtype/msn.md) — Specifies Microsoft Network default authentication.
- [kSecAuthenticationTypeDPA](secauthenticationtype/dpa.md) — Specifies Distributed Password authentication.
- [kSecAuthenticationTypeRPA](secauthenticationtype/rpa.md) — Specifies Remote Password authentication.
- [kSecAuthenticationTypeHTTPBasic](secauthenticationtype/httpbasic.md) — Specifies HTTP Basic authentication.
- [kSecAuthenticationTypeHTTPDigest](secauthenticationtype/httpdigest.md) — Specifies HTTP Digest Access authentication.
- [kSecAuthenticationTypeHTMLForm](secauthenticationtype/htmlform.md) — Specifies HTML form based authentication.
- [kSecAuthenticationTypeDefault](secauthenticationtype/default.md) — Specifies the default authentication type.
- [kSecAuthenticationTypeAny](secauthenticationtype/any.md) — Specifies that any authentication type is acceptable.

### Initializers

- [init(rawValue:)](<secauthenticationtype/init(rawvalue_).md>)
