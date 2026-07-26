---
title: kSecTrustRevocationChecked
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustrevocationchecked
source_url: 'https://developer.apple.com/documentation/security/ksectrustrevocationchecked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustrevocationchecked.json'
content_hash: 'sha256:6adf6973ac768fbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustRevocationChecked

<sub>Global Variable</sub>

A key whose value indicates the outcome of revocation checking during trust evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustRevocationChecked: CFString
```

## Discussion

This key is only present if the evaluation process conducted revocation checking on the chain. The value is a Boolean set to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) if revocation checking was successful and none of the certificates in the chain were revoked. The value is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) if no current revocation status could be obtained for one or more certificates in the chain due to connection problems or timeouts. You can take this outcome as a hint to retry revocation checking again at a later time.
