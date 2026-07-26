---
title: kSecCodeInfoEntitlements
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoentitlements
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoentitlements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoentitlements.json'
content_hash: 'sha256:ca285d997a198189'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoEntitlements

<sub>Global Variable</sub>

A key whose value represents the embedded entitlement blob of the code, if any.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoEntitlements: CFString
```

## Discussion

The value is a [CFData](../corefoundation/cfdata.md) object.

Specify the [kSecCSRequirementInformation](kseccsrequirementinformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) to get this information.
