---
title: 'SecTrustCopyCustomAnchorCertificates(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustcopycustomanchorcertificates(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopycustomanchorcertificates(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopycustomanchorcertificates%28_%3A_%3A%29.json'
content_hash: 'sha256:3c71965bd31f5751'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyCustomAnchorCertificates(_:_:)

<sub>Function</sub>

Retrieves the custom anchor certificates, if any, used by a given trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCopyCustomAnchorCertificates(_ trust: SecTrust, _ anchors: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `trust` — The trust management object from which you wish to retrieve the custom anchor certificates.

- `anchors` — On return, a reference to an array of `SecCertificateRef` objects representing the set of anchor certificates that are considered valid (trusted) anchors by the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function when verifying a certificate using the trust management object in the `trust` parameter. Returns `NULL` if no custom anchors have been specified. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

You can use the [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) function to set custom anchor certificates.

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) function for the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) — Sets the anchor certificates used when evaluating a trust management object.
