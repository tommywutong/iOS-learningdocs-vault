---
title: 'SecTrustSetVerifyDate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetverifydate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetverifydate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetverifydate%28_%3A_%3A%29.json'
content_hash: 'sha256:102a8b9c350f6db4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetVerifyDate(_:_:)

<sub>Function</sub>

Sets the date and time against which the certificates in a trust management object are verified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetVerifyDate(_ trust: SecTrust, _ verifyDate: CFDate) -> OSStatus
```

## Parameters

- `trust` — The trust management object whose verification date you want to set. A trust management object includes one or more certificates plus the policy or policies to be used in evaluating trust. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `verifyDate` — The date and time to use when verifying the certificate.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

By default, the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function uses the current date and time when verifying a certificate. However, you can use `SecTrustSetVerifyDate` to set another date and time to use when verifying a certificate. For example, you can determine whether the certificate was valid when the document was signed rather than whether it’s valid at the present time.

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the evaluation function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustGetVerifyTime](<sectrustgetverifytime(__).md>) — Gets the absolute time against which the certificates in a trust management object are verified.
