---
title: 'SecTrustGetVerifyTime(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustgetverifytime(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustgetverifytime(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgetverifytime%28_%3A%29.json'
content_hash: 'sha256:b4c18b05f8b31023'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetVerifyTime(_:)

<sub>Function</sub>

Gets the absolute time against which the certificates in a trust management object are verified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustGetVerifyTime(_ trust: SecTrust) -> CFAbsoluteTime
```

## Parameters

- `trust` — The trust management object whose verification time you want to get. A trust management object includes one or more certificates plus the policy or policies to be used in evaluating trust. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

## Return Value

The absolute time at which the certificates should be checked for validity.

## Discussion

This function returns the absolute time returned by:

1. the [CFDateGetAbsoluteTime(_:)](<../corefoundation/cfdategetabsolutetime(__).md>) function for the date passed in to the [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) function, if that was called, or
2. the last value returned by the [SecTrustGetVerifyTime](<sectrustgetverifytime(__).md>) function, if it was called before, or
3. the value returned by the [CFAbsoluteTimeGetCurrent()](<../corefoundation/cfabsolutetimegetcurrent().md>) function if neither [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) nor [SecTrustGetVerifyTime](<sectrustgetverifytime(__).md>) were ever called.

It is safe to call this function concurrently on two or more threads as long as it is not used to get a value from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) function for the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) — Sets the date and time against which the certificates in a trust management object are verified.
