---
title: 'SecTrustGetCertificateAtIndex(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.7+（12.0 起废弃）, tvOS 9.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustgetcertificateatindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustgetcertificateatindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgetcertificateatindex%28_%3A_%3A%29.json'
content_hash: 'sha256:1687289db9d273ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetCertificateAtIndex(_:_:)

<sub>Function</sub>

Returns a specific certificate from the certificate chain used to evaluate trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustGetCertificateAtIndex(_ trust: SecTrust, _ ix: CFIndex) -> SecCertificate?
```

## Parameters

- `trust` — The trust management object for the certificate that has been evaluated.  Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object and the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function to evaluate the certificate chain.

- `ix` — The index number of the requested certificate. Index numbers start at 0 for the leaf certificate and end at the anchor (or the last certificate if no anchor was found). Use the [SecTrustGetCertificateCount](<sectrustgetcertificatecount(__).md>) function to get the total number of certificates in the chain.

## Return Value

A certificate object for the requested certificate.

## Discussion

Call the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function before calling this function.
