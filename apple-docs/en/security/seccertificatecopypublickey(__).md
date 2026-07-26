---
title: 'SecCertificateCopyPublicKey(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.3+（12.0 起废弃）, iPadOS 10.3+（12.0 起废弃）, macOS 10.3+（10.14 起废弃）, tvOS 10.2+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.2+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seccertificatecopypublickey(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopypublickey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopypublickey%28_%3A%29.json'
content_hash: 'sha256:e030666fcea7bb3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyPublicKey(_:)

<sub>Function</sub>

Retrieves the public key from a certificate.

> [!warning] Deprecated
> Use [SecCertificateCopyKey](<seccertificatecopykey(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyPublicKey(_ certificate: SecCertificate) -> SecKey?
```

<sub>macOS</sub>

```swift
func SecCertificateCopyPublicKey(_ certificate: SecCertificate, _ key: UnsafeMutablePointer<SecKey?>) -> OSStatus
```

## Parameters

- `certificate` — The certificate object from which to retrieve the public key.

- `key` — In macOS, points to the public key for the specified certificate. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

In iOS, the certificate’s public key.

## Discussion

In macOS, a result code. See [Security Framework Result Codes](security-framework-result-codes.md).
