---
title: kSecUseAuthenticationUI
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecuseauthenticationui
source_url: 'https://developer.apple.com/documentation/security/ksecuseauthenticationui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseauthenticationui.json'
content_hash: 'sha256:4675c23e7b12c4aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseAuthenticationUI

<sub>Global Variable</sub>

A key whose value indicates whether the user is prompted for authentication.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseAuthenticationUI: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and contains one of the values listed in [UI authentication values](search-attribute-keys-and-values.md#UI-authentication-values). The value specifies whether or not the user is prompted for authentication, if needed. A default value of [kSecUseAuthenticationUIAllow](ksecuseauthenticationuiallow.md) is assumed when this key is not present.
