---
title: 'SecCertificateCopyData(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopydata(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopydata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopydata%28_%3A%29.json'
content_hash: 'sha256:3778264ad22b583e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyData(_:)

<sub>Function</sub>

Returns a DER representation of a certificate given a certificate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyData(_ certificate: SecCertificate) -> CFData
```

## Parameters

- `certificate` — The certificate object for which you wish to return the DER (Distinguished Encoding Rules) representation of the X.509 certificate.

## Return Value

The DER representation of the certificate. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it. Returns `nil` if the data passed in the `certificate` parameter is not a valid certificate object.
