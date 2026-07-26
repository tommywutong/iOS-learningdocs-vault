---
title: kSecUseAuthenticationUIAllow
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（14.0 起废弃）, iPadOS 9.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.11+（11.0 起废弃）, tvOS 9.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecuseauthenticationuiallow
source_url: 'https://developer.apple.com/documentation/security/ksecuseauthenticationuiallow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseauthenticationuiallow.json'
content_hash: 'sha256:78b98ed4fd14da0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseAuthenticationUIAllow

<sub>Global Variable</sub>

A value that indicates user authentication is allowed.

> [!warning] Deprecated
> Instead of kSecUseAuthenticationUI, use kSecUseAuthenticationContext and set LAContext.interactionNotAllowed property

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseAuthenticationUIAllow: CFString
```

## Discussion

The user may be prompted for authentication. This is the default value.
