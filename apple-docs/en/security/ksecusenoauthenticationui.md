---
title: kSecUseNoAuthenticationUI
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+（9.0 起废弃）, iPadOS 8.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecusenoauthenticationui
source_url: 'https://developer.apple.com/documentation/security/ksecusenoauthenticationui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecusenoauthenticationui.json'
content_hash: 'sha256:7cad31506dde395b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseNoAuthenticationUI

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether to disallow UI authentication.

> [!warning] Deprecated
> Use the key [kSecUseAuthenticationUI](ksecuseauthenticationui.md) with value [kSecUseAuthenticationUIFail](ksecuseauthenticationuifail.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseNoAuthenticationUI: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). If provided with a value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), the error [errSecInteractionNotAllowed](errsecinteractionnotallowed.md) is returned when the item is attempting to authenticate with UI.
