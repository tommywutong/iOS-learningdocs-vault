---
title: kSecTrustResultValue
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustresultvalue
source_url: 'https://developer.apple.com/documentation/security/ksectrustresultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustresultvalue.json'
content_hash: 'sha256:eac01294ef8cfd09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustResultValue

<sub>Global Variable</sub>

A key whose value represents the trust evaluation result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustResultValue: CFString
```

## Discussion

The key is present after trust evaluation completes. Its value is a [CFNumber](../corefoundation/cfnumber.md) that holds one of the values listed in [SecTrustResultType](sectrustresulttype.md), indicating the outcome of the trust evaluation.
