---
title: kSecCodeInfoStatus
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfostatus
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfostatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfostatus.json'
content_hash: 'sha256:d0b87f9b103416b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoStatus

<sub>Global Variable</sub>

A key whose value is the set of code status flags for the running code.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoStatus: CFString
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md) object. This is a snapshot taken at the time the function is executed and may be out of date by the time you examine it. Note, however, that some flag values cannot be changed and are therefore permanently reliable. See [SecCodeStatus](seccodestatus.md) for a list of possible values.

Specify the [kSecCSDynamicInformation](kseccsdynamicinformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
