---
title: 'SecCertificateCopyNormalizedSubjectSequence(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopynormalizedsubjectsequence(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopynormalizedsubjectsequence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopynormalizedsubjectsequence%28_%3A%29.json'
content_hash: 'sha256:6d298545b51cc28d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyNormalizedSubjectSequence(_:)

<sub>Function</sub>

Retrieves the normalized subject sequence from a certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyNormalizedSubjectSequence(_ certificate: SecCertificate) -> CFData?
```

## Parameters

- `certificate` — The certificate from which to retrieve the data.

## Return Value

A data object containing the sequence or `NULL` on error. In Objective-C, free this object with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.
