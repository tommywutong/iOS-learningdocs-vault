---
title: SecTrustWithErrorCallback
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustwitherrorcallback
source_url: 'https://developer.apple.com/documentation/security/sectrustwitherrorcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustwitherrorcallback.json'
content_hash: 'sha256:5a3c2d9002a6e974'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustWithErrorCallback

<sub>Type Alias</sub>

A block called with the results of an asynchronous trust evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SecTrustWithErrorCallback = (SecTrust, Bool, CFError?) -> Void
```

## Parameters

- `trustRef` — The trust that was evaluated.

- `result` — A Boolean that’s `true` if the certificate is trusted, or `false` if not.

- `error` — An error that indicates the reason for trust failure, if applicable.

## Discussion

Provide a block of this type as the final argument to the [SecTrustEvaluateAsyncWithError](<sectrustevaluateasyncwitherror(______).md>) method to receive the result of the trust evaluation.

The block provides a pass or fail indicator and an error describing the reason for any failure. In the case of multiple certificate failures, the error contains a code representing the most serious. The localized description indicates the certificate with the most serious problem and the type of error. The underlying error contains a localized description of each certificate in the chain that had an error and all errors found with that certificate.
