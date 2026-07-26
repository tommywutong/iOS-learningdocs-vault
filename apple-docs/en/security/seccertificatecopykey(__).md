---
title: 'SecCertificateCopyKey(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopykey(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopykey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopykey%28_%3A%29.json'
content_hash: 'sha256:3558a83690d9515c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyKey(_:)

<sub>Function</sub>

Retrieves the public key for a given certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyKey(_ certificate: SecCertificate) -> SecKey?
```

## Parameters

- `certificate` — The certificate from which to copy the key.

## Return Value

The public key. In Objective-C, free this key with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.

## Discussion

The return reference is `NULL` if the public key has an encoding issue or uses an unsupported algorithm.
