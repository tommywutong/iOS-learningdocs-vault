---
title: 'SecTrustSetAnchorCertificatesOnly(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetanchorcertificatesonly(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetanchorcertificatesonly(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetanchorcertificatesonly%28_%3A_%3A%29.json'
content_hash: 'sha256:a75124a03e992ac2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetAnchorCertificatesOnly(_:_:)

<sub>Function</sub>

Reenables trusting built-in anchor certificates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetAnchorCertificatesOnly(_ trust: SecTrust, _ anchorCertificatesOnly: Bool) -> OSStatus
```

## Parameters

- `trust` — The trust management object containing the certificate you want to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `anchorCertificatesOnly` — If `true`, disables trusting any anchors other than the ones passed in with the [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) function.  If `false`, the built-in anchor certificates are also trusted. If [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) is called and [SecTrustSetAnchorCertificatesOnly](<sectrustsetanchorcertificatesonly(____).md>) is not called, only the anchors explicitly passed in are trusted.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) — Retrieves the custom anchor certificates, if any, used by a given trust.
- [SecTrustCopyAnchorCertificates](<sectrustcopyanchorcertificates(__).md>) — Retrieves the anchor (root) certificates stored by macOS.
