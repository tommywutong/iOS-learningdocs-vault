---
title: 'SecCertificateCopySerialNumberData(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopyserialnumberdata(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopyserialnumberdata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopyserialnumberdata%28_%3A_%3A%29.json'
content_hash: 'sha256:a27685e1fe603234'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopySerialNumberData(_:_:)

<sub>Function</sub>

Returns the certificate’s serial number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopySerialNumberData(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `certificate` — The certificate from which to copy the serial number.

- `error` — A [CFError](../corefoundation/cferror.md) pointer the function uses to return an error instance on failure. Set to `nil` to ignore any error.

## Return Value

The content of a DER-encoded integer (without the tag and length fields) for this certificate’s serial number.

## Discussion

In Objective-C, if the function returns an error free it with a call to [CFRelease](../corefoundation/cfrelease.md) when you are done with it. If it returns data, you must free that as well.
