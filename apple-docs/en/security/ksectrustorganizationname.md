---
title: kSecTrustOrganizationName
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustorganizationname
source_url: 'https://developer.apple.com/documentation/security/ksectrustorganizationname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustorganizationname.json'
content_hash: 'sha256:637567369b34d912'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustOrganizationName

<sub>Global Variable</sub>

A key whose value is the organization name field of the subject of the leaf certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustOrganizationName: CFString
```

## Discussion

The value is a [CFString](../corefoundation/cfstring.md) that is meant to be displayed to the user as the validated name of the company or entity that owns the certificate, but only if the [kSecTrustExtendedValidation](ksectrustextendedvalidation.md) key is present.
