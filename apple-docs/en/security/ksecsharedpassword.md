---
title: kSecSharedPassword
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecsharedpassword
source_url: 'https://developer.apple.com/documentation/security/ksecsharedpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecsharedpassword.json'
content_hash: 'sha256:8aec4bb550613a90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecSharedPassword

<sub>Global Variable</sub>

A dictionary key whose value is the shared password.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let kSecSharedPassword: CFString
```

## Discussion

The dictionary returned by the [SecRequestSharedWebCredential](<secrequestsharedwebcredential(______).md>) function includes this key to provide you with the password.

You can also access the server’s URL and the user name from this dictionary. To access the server, use the [kSecAttrServer](ksecattrserver.md) constant. To access the user name, use the [kSecAttrAccount](ksecattraccount.md) constant. These constants are part of the [Keychain services](keychain-services.md) API, and in particular are listed among the [Item attribute keys and values](item-attribute-keys-and-values.md).
