---
title: 'SecTrustSetPolicies(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetpolicies(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetpolicies(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetpolicies%28_%3A_%3A%29.json'
content_hash: 'sha256:9cee6e116c70409c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetPolicies(_:_:)

<sub>Function</sub>

Sets the policies to use in an evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetPolicies(_ trust: SecTrust, _ policies: CFTypeRef) -> OSStatus
```

## Parameters

- `trust` — The trust management object whose policy list you wish to set.

- `policies` — An array of one or more [SecPolicy](secpolicy.md) objects for the policies to be used by this trust management object. A single policy object of type `SecPolicyRef` may also be passed, representing an array of one policy.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The policies you set with this function replace any already in the trust management object.

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustCopyPolicies](<sectrustcopypolicies(____).md>) — Retrieves the policies used by a given trust management object.
