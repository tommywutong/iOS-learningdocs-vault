---
title: kSecCodeInfoTime
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfotime
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfotime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfotime.json'
content_hash: 'sha256:00623fd9ad0714ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoTime

<sub>Global Variable</sub>

A key whose value is the signing date embedded in the code signature.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoTime: CFString
```

## Discussion

The value is a [CFDate](../corefoundation/cfdate.md) object. Note that a signer is able to omit this date or pre-date it. Therefore, this is not necessarily the date the code was actually signed. However, you do know that this is the date the signer wanted you to see. Ad-hoc signatures never have secured signing dates.

Specify the [kSecCSSigningInformation](kseccssigninginformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
