---
title: kSecAttrAccessibleWhenUnlocked
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccessiblewhenunlocked
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessiblewhenunlocked.json'
content_hash: 'sha256:ed9be4649f98ebe9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessibleWhenUnlocked

<sub>Global Variable</sub>

The data in the keychain item can be accessed only while the device is unlocked by the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessibleWhenUnlocked: CFString
```

## Discussion

This is recommended for items that need to be accessible only while the application is in the foreground. Items with this attribute migrate to a new device when using encrypted backups.

This is the default value for keychain items added without explicitly setting an accessibility constant.
