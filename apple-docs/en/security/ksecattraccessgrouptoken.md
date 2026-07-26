---
title: kSecAttrAccessGroupToken
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccessgrouptoken
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessgrouptoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessgrouptoken.json'
content_hash: 'sha256:dfb599ff2a9a4366'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessGroupToken

<sub>Global Variable</sub>

The access group containing items provided by external tokens.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessGroupToken: CFString
```

## Discussion

Use this access group identifier as the value for the [kSecAttrAccessGroup](ksecattraccessgroup.md) attribute in a keychain query to access external tokens such as smart cards. Access to this group is granted by default and does not require an explicit entry in your app’s [Keychain Access Groups Entitlement](../bundleresources/entitlements/keychain-access-groups.md).
