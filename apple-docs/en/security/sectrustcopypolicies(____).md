---
title: 'SecTrustCopyPolicies(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustcopypolicies(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopypolicies(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopypolicies%28_%3A_%3A%29.json'
content_hash: 'sha256:c1bcb3bc833efb62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyPolicies(_:_:)

<sub>Function</sub>

Retrieves the policies used by a given trust management object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCopyPolicies(_ trust: SecTrust, _ policies: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `trust` — The trust management object whose policies you wish to retrieve.

- `policies` — On return, an array of [SecPolicy](secpolicy.md) objects for the policies used by this trust management object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [SecTrustSetPolicies](<sectrustsetpolicies(____).md>) function for the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustSetPolicies](<sectrustsetpolicies(____).md>) — Sets the policies to use in an evaluation.
