---
title: kSecCodeInfoRequirementData
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinforequirementdata
source_url: 'https://developer.apple.com/documentation/security/kseccodeinforequirementdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinforequirementdata.json'
content_hash: 'sha256:7d3e422d308382e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoRequirementData

<sub>Global Variable</sub>

A key whose value is the internal requirements of the code as a binary blob.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoRequirementData: CFString
```

## Discussion

The value is a [CFData](../corefoundation/cfdata.md) object. If there is an explicit designated requirement, then it’s included in this data blob.

Specify the [kSecCSRequirementInformation](kseccsrequirementinformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
