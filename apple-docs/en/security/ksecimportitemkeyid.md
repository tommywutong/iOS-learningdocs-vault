---
title: kSecImportItemKeyID
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecimportitemkeyid
source_url: 'https://developer.apple.com/documentation/security/ksecimportitemkeyid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecimportitemkeyid.json'
content_hash: 'sha256:42154e3b1bc0818b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecImportItemKeyID

<sub>Global Variable</sub>

Key ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecImportItemKeyID: CFString
```

## Discussion

The corresponding value is of type `CFDataRef`. This unique ID is often the SHA-1 digest of the public encryption key.
