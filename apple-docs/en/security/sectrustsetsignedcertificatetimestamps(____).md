---
title: 'SecTrustSetSignedCertificateTimestamps(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.1.1+, iPadOS 12.1.1+, Mac Catalyst 13.1+, macOS 10.14.2+, tvOS 12.1.1+, visionOS 1.0+, watchOS 5.1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetsignedcertificatetimestamps(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetsignedcertificatetimestamps(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetsignedcertificatetimestamps%28_%3A_%3A%29.json'
content_hash: 'sha256:07d873a5def3852a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetSignedCertificateTimestamps(_:_:)

<sub>Function</sub>

Attaches signed certificate timestamp data to a trust object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetSignedCertificateTimestamps(_ trust: SecTrust, _ sctArray: CFArray?) -> OSStatus
```

## Parameters

- `trust` — The trust object to which the timestamp data should be attached.

- `sctArray` — An array of [CFData](../corefoundation/cfdata.md) instances, each of which contains a signed certificate timestamp.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Use this function to provide secure certificate timestamps, which might be obtained during a TLS/SSL handshake, as input to a trust evaluation. For more information, see [RFC 6962](https://tools.ietf.org/html/rfc6962).
