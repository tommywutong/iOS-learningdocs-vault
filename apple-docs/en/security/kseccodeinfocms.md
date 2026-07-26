---
title: kSecCodeInfoCMS
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfocms
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfocms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfocms.json'
content_hash: 'sha256:c17485a84d134ec4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoCMS

<sub>Global Variable</sub>

A key whose value is the CMS cryptographic object that secures the code signature.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoCMS: CFString
```

## Discussion

The value is a [CFData](../corefoundation/cfdata.md) object. Empty for ad-hoc signed code.

Specify the [kSecCSSigningInformation](kseccssigninginformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
