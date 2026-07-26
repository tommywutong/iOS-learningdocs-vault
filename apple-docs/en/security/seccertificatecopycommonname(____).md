---
title: 'SecCertificateCopyCommonName(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopycommonname(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopycommonname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopycommonname%28_%3A_%3A%29.json'
content_hash: 'sha256:2ba7be33d217c0e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyCommonName(_:_:)

<sub>Function</sub>

Retrieves the common name of the subject of a certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyCommonName(_ certificate: SecCertificate, _ commonName: UnsafeMutablePointer<CFString?>) -> OSStatus
```

## Parameters

- `certificate` — The certificate object from which to retrieve the common name.

- `commonName` — On return, points to the common name. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
