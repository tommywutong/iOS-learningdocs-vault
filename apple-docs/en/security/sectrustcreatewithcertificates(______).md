---
title: 'SecTrustCreateWithCertificates(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustcreatewithcertificates(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcreatewithcertificates(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcreatewithcertificates%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a1f6eb6df09975b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCreateWithCertificates(_:_:_:)

<sub>Function</sub>

Creates a trust management object based on certificates and policies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCreateWithCertificates(_ certificates: CFTypeRef, _ policies: CFTypeRef?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus
```

## Parameters

- `certificates` — The certificate to be verified, plus any other certificates you think might be useful for verifying the certificate. The certificate to be verified must be the first in the array. If you want to specify only one certificate, you can pass a [SecCertificate](seccertificate.md) object; otherwise, pass an array of [SecCertificate](seccertificate.md) objects.

- `policies` — References to one or more policies to be evaluated. You can pass a single [SecPolicy](secpolicy.md) object, or an array of one or more [SecPolicy](secpolicy.md) objects. If you pass in multiple policies, all policies must verify for the certificate chain to be considered valid. You typically use one of the standard policies, like the one returned by [SecPolicyCreateBasicX509](<secpolicycreatebasicx509().md>).

- `trust` — On return, points to the newly created trust management object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The trust management object includes a reference to the certificate to be verified, plus pointers to the policies to be evaluated for those certificates. You can optionally include references to other certificates, including anchor certificates, that you think might be in the certificate chain needed to verify the first (leaf) certificate. Any input certificates that turn out to be irrelevant are harmlessly ignored. Call the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function to evaluate the trust management object.

If you omit needed intermediate certificates from the `certificates` parameter, [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) searches for certificates in the user’s keychain and in the system’s store of anchor certificates (see [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>)). You gain a significant performance benefit by passing in the entire certificate chain, in order, in the `certificates` parameter.
