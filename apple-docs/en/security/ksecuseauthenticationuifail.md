---
title: kSecUseAuthenticationUIFail
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（14.0 起废弃）, iPadOS 9.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.11+（11.0 起废弃）, tvOS 9.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecuseauthenticationuifail
source_url: 'https://developer.apple.com/documentation/security/ksecuseauthenticationuifail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseauthenticationuifail.json'
content_hash: 'sha256:81e9bc747e2437e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseAuthenticationUIFail

<sub>Global Variable</sub>

A value that indicates user authentication is disallowed.

> [!warning] Deprecated
> Instead of kSecUseAuthenticationUI, use kSecUseAuthenticationContext and set LAContext.interactionNotAllowed property

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseAuthenticationUIFail: CFString
```

## Discussion

When you specify this value, if user authentication is needed, the function returns the [errSecInteractionNotAllowed](errsecinteractionnotallowed.md) error.
