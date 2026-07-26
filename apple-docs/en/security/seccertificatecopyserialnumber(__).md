---
title: 'SecCertificateCopySerialNumber(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.3+（11.0 起废弃）, iPadOS 10.3+（11.0 起废弃）, macOS 10.7+（10.13 起废弃）, tvOS 10.2+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.2+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seccertificatecopyserialnumber(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopyserialnumber(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopyserialnumber%28_%3A%29.json'
content_hash: 'sha256:6163785b892b841f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopySerialNumber(_:)

<sub>Function</sub>

Returns a copy of a certificate’s serial number.

> [!warning] Deprecated
> Use [SecCertificateCopySerialNumberData](<seccertificatecopyserialnumberdata(____).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopySerialNumber(_ certificate: SecCertificate) -> CFData?
```

<sub>macOS</sub>

```swift
func SecCertificateCopySerialNumber(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `certificate` — The certificate from which the serial number should be copied.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

A data instance containing a DER-encoded integer for the certificate’s serial number (without the tag and length fields) or `nil` if an error occurred. In Objective-C, free this object with a call to [CFRelease](../corefoundation/cfrelease.md) when you are done with it.
