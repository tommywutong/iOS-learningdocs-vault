---
title: 'SecCertificateCopyNormalizedIssuerSequence(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopynormalizedissuersequence(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopynormalizedissuersequence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopynormalizedissuersequence%28_%3A%29.json'
content_hash: 'sha256:53acaee084fafc07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyNormalizedIssuerSequence(_:)

<sub>Function</sub>

Retrieves the normalized issuer sequence from a certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyNormalizedIssuerSequence(_ certificate: SecCertificate) -> CFData?
```

## Parameters

- `certificate` — The certificate from which to retrieve the data.

## Return Value

A data object containing the sequence or `NULL` on error. In Objective-C, free this object with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.
