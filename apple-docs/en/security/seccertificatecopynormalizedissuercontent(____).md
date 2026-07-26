---
title: 'SecCertificateCopyNormalizedIssuerContent(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.12.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seccertificatecopynormalizedissuercontent(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopynormalizedissuercontent(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopynormalizedissuercontent%28_%3A_%3A%29.json'
content_hash: 'sha256:294b7ad81d64e963'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyNormalizedIssuerContent(_:_:)

<sub>Function</sub>

Returns a normalized copy of the distinguished name (DN) of the issuer of a certificate.

> [!warning] Deprecated
> SecCertificateCopyNormalizedIssuerContent is deprecated. Use SecCertificateCopyNormalizedIssuerSequence instead.

<sub>macOS</sub>

```swift
func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `certificate` — The certificate from which the issuer’s distinguished name should be copied.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

A data object containing a DER-encoded X.509 distinguished name suitable for use with [SecItemCopyMatching](<secitemcopymatching(____).md>). Returns `NULL` if an error occurred. In Objective-C, free the object with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.

## Discussion

To obtain a copy of the issuer’s distinguished name in a format suitable for display purposes, call [SecCertificateCopyValues](<seccertificatecopyvalues(______).md>) instead.
