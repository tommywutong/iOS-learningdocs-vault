---
title: kSecCodeInfoTrust
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfotrust
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfotrust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfotrust.json'
content_hash: 'sha256:bfdae79ee218d7dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoTrust

<sub>Global Variable</sub>

A key whose value is the trust object the system uses to evaluate the validity of the code’s signature.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoTrust: CFString
```

## Discussion

The value is a retained [SecTrust](sectrust.md) object. You may use [SecTrust](sectrust.md) functions (see [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) to extract detailed information, for example the reasons why certificate validation may have failed. Because this object may continue to be used for further evaluations of the code signature, if you make any changes to it, the behavior of the [SecTrust](sectrust.md) functions is undefined.

Specify the [kSecCSSigningInformation](kseccssigninginformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
