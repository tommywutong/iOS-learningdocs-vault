---
title: kSecCodeInfoRequirements
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinforequirements
source_url: 'https://developer.apple.com/documentation/security/kseccodeinforequirements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinforequirements.json'
content_hash: 'sha256:7e622f49d1c3a75d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoRequirements

<sub>Global Variable</sub>

A key whose value is the internal requirements of the code as a text string in canonical syntax.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoRequirements: CFString
```

## Discussion

The value is a [CFString](../corefoundation/cfstring.md) object. If there is an explicit designated requirement, then it’s included in this text string.

Specify the [kSecCSRequirementInformation](kseccsrequirementinformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
