---
title: 'SecTrustGetCertificateCount(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustgetcertificatecount(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustgetcertificatecount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgetcertificatecount%28_%3A%29.json'
content_hash: 'sha256:76a8567a83a893ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetCertificateCount(_:)

<sub>Function</sub>

Returns the number of certificates in an evaluated certificate chain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustGetCertificateCount(_ trust: SecTrust) -> CFIndex
```

## Parameters

- `trust` — The trust management object for the certificate that has been evaluated.  Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object and the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function to evaluate the certificate chain.

## Return Value

The number of certificates in the certificate chain.

## Discussion

Call the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function before calling this function.
