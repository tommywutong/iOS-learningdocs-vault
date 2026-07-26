---
title: kSecAttrIsNegative
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrisnegative
source_url: 'https://developer.apple.com/documentation/security/ksecattrisnegative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrisnegative.json'
content_hash: 'sha256:8432125653613218'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrIsNegative

<sub>Global Variable</sub>

A key with a value that’s a Boolean indicating whether the item has a valid password.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrIsNegative: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether there is a valid password associated with this keychain item. This is useful if your application doesn’t want a password for some particular service to be stored in the keychain, but prefers that it always be entered by the user.
