---
title: 'SecTrustCopyExceptions(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustcopyexceptions(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopyexceptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopyexceptions%28_%3A%29.json'
content_hash: 'sha256:8648c9b52214cbb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyExceptions(_:)

<sub>Function</sub>

Returns an opaque cookie containing exceptions to trust policies that will allow future evaluations of the current certificate to succeed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCopyExceptions(_ trust: SecTrust) -> CFData?
```

## Parameters

- `trust` — The evaluated trust management object whose policies you wish to retrieve.

## Return Value

An opaque cookie. If you pass this cookie to [SecTrustSetExceptions](<sectrustsetexceptions(____).md>), that function sets a list of exceptions for future processing of the certificate. Once this list of exceptions are set, a subsequent call to [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) for that certificate will return `true`.

## Discussion

Note: If a new error occurs that did not occur when this function was called originally, the subsequent call to [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) can still fail. For example, if the certificate expires between calling `SecTrustCopyExceptions` and [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>), evaluation will fail.

## Discussion

Normally this API should only be called after asking the user how to proceed, and even then, only if the user explicitly tells your application to trust the current certificate chain in spite of the errors presented.

## See Also

### Related Documentation

- [SecTrustSetPolicies](<sectrustsetpolicies(____).md>) — Sets the policies to use in an evaluation.
