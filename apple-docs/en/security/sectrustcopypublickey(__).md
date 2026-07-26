---
title: 'SecTrustCopyPublicKey(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（14.0 起废弃）, iPadOS 2.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.7+（11.0 起废弃）, tvOS 9.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustcopypublickey(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopypublickey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopypublickey%28_%3A%29.json'
content_hash: 'sha256:a8c867993c913544'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyPublicKey(_:)

<sub>Function</sub>

Returns the public key for a leaf certificate after it has been evaluated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCopyPublicKey(_ trust: SecTrust) -> SecKey?
```

## Parameters

- `trust` — The trust management object for the certificate that has been evaluated.  Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

## Return Value

The leaf certificate’s public key, or `NULL` if it the public key could not be extracted (this can happen with DSA certificate chains if the parameters in the chain cannot be found). In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Discussion

Call the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function before calling this function.

When you call this function, it attempts to return the public key of the leaf certificate, even if the trust evaluation was unsuccessful. Even if the trust evaluation was successful, this function might still return `NULL`—for example, if the leaf certificate’s key can’t be extracted for some reason.
