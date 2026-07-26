---
title: SecCreateSharedWebCredentialPassword()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccreatesharedwebcredentialpassword()
source_url: 'https://developer.apple.com/documentation/security/seccreatesharedwebcredentialpassword()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccreatesharedwebcredentialpassword%28%29.json'
content_hash: 'sha256:0cd12dd4c72a5628'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCreateSharedWebCredentialPassword()

<sub>Function</sub>

Returns a randomly generated password.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func SecCreateSharedWebCredentialPassword() -> CFString?
```

## Return Value

A password in the form `xxx-xxx-xxx-xxx`, where `x` is taken from the sets `abcdefghkmnopqrstuvwxy`, `ABCDEFGHJKLMNPQRSTUVWXYZ`, and `3456789`, with at least one character from each set being present.
