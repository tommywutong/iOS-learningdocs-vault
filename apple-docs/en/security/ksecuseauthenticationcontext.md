---
title: kSecUseAuthenticationContext
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecuseauthenticationcontext
source_url: 'https://developer.apple.com/documentation/security/ksecuseauthenticationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseauthenticationcontext.json'
content_hash: 'sha256:14ae7267d7049044'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseAuthenticationContext

<sub>Global Variable</sub>

A key whose value indicates a local authentication context to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseAuthenticationContext: CFString
```

## Discussion

The corresponding value is of type [LAContext](../localauthentication/lacontext.md), and represents a reusable local authentication context that should be used for keychain item authentication, according to the following rules:

- If this key is not specified, and if the item requires authentication, a new context will be created, used once, and discarded.
- If this key is specified with a context that has been previously authenticated, the operation will succeed without asking user for authentication.
- If this key is specified with a context that has not been previously authenticated, the system attempts authentication on the context. If successful, the context may be reused in subsequent keychain operations.
