---
title: kSecTrustRevocationValidUntilDate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustrevocationvaliduntildate
source_url: 'https://developer.apple.com/documentation/security/ksectrustrevocationvaliduntildate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustrevocationvaliduntildate.json'
content_hash: 'sha256:bffc6c3b9a7cf932'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustRevocationValidUntilDate

<sub>Global Variable</sub>

A key whose value indicates the earliest date at which revocation information becomes stale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustRevocationValidUntilDate: CFString
```

## Discussion

This key is only present if the [kSecTrustRevocationChecked](ksectrustrevocationchecked.md) key has a value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md). The value is a [CFDate](../corefoundation/cfdate.md) representing the earliest date at which the revocation information for one of the certificates in this chain might change.
