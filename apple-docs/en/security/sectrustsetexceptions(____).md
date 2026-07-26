---
title: 'SecTrustSetExceptions(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetexceptions(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetexceptions(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetexceptions%28_%3A_%3A%29.json'
content_hash: 'sha256:409deaaa979a4dc7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetExceptions(_:_:)

<sub>Function</sub>

Sets a list of exceptions that should be ignored when the certificate is evaluated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetExceptions(_ trust: SecTrust, _ exceptions: CFData?) -> Bool
```

## Parameters

- `trust` — The trust management object whose exception list you wish to modify.

- `exceptions` — An opaque cookie returned by a prior call to [SecTrustCopyExceptions](<sectrustcopyexceptions(__).md>).

## Return Value

A Boolean that is [true](../swift/true.md) if the exceptions cookies was valid and matches the current leaf certificate, [false](../swift/false.md) otherwise.

## Discussion

> [!important] Important
> Even if this function returns true, you must still call [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) because the evaluation can still fail if something changes between the initial evaluation and the reevaluation.
