---
title: SecTrustCallback
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustcallback
source_url: 'https://developer.apple.com/documentation/security/sectrustcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcallback.json'
content_hash: 'sha256:c0d78005d501c134'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCallback

<sub>Type Alias</sub>

A block called with the results of an asynchronous trust evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SecTrustCallback = (SecTrust, SecTrustResultType) -> Void
```

## Parameters

- `trustRef` — The trust that was evaluated.

- `trustResult` — The result of the trust evaluation. See [SecTrustResultType](sectrustresulttype.md) for a list of possible values.

## Discussion

Use a block of this type when making a call to [SecTrustEvaluateAsync](<sectrustevaluateasync(______).md>) to receive the result of the trust evaluation.
