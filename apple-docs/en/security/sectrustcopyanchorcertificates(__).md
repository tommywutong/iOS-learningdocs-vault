---
title: 'SecTrustCopyAnchorCertificates(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustcopyanchorcertificates(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopyanchorcertificates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopyanchorcertificates%28_%3A%29.json'
content_hash: 'sha256:d3686719feabf896'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyAnchorCertificates(_:)

<sub>Function</sub>

Retrieves the anchor (root) certificates stored by macOS.

<sub>macOS</sub>

```swift
func SecTrustCopyAnchorCertificates(_ anchors: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `anchors` — On return, points to an array of certificate objects for trusted anchor (root) certificates, which is the default set of anchors for the caller. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release the [CFArray](../corefoundation/cfarray.md) object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function retrieves the certificates in the system’s store of anchor certificates (see [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>)). You can use the [SecCertificate](seccertificate.md) objects retrieved by this function as input to other functions of this API, such as [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>).

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) function for the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) — Sets the anchor certificates used when evaluating a trust management object.
