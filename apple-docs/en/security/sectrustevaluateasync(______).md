---
title: 'SecTrustEvaluateAsync(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）, tvOS 7.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustevaluateasync(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustevaluateasync(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustevaluateasync%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:07fa1e9e156d8f10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustEvaluateAsync(_:_:_:)

<sub>Function</sub>

Evaluates a trust object asynchronously on the specified dispatch queue.

> [!warning] Deprecated
> Use [SecTrustEvaluateAsyncWithError](<sectrustevaluateasyncwitherror(______).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustEvaluateAsync(_ trust: SecTrust, _ queue: dispatch_queue_t?, _ result: @escaping SecTrustCallback) -> OSStatus
```

## Parameters

- `trust` — The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `queue` — The dispatch queue on which the result block should execute.

- `result` — A block called with the result of evaluation. See [SecTrustResultType](sectrustresulttype.md) for descriptions of possible values.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function is functionally equivalent to [SecTrustEvaluate](<sectrustevaluate(____).md>) except that it performs evaluation asynchronously and calls a block when evaluation completes. For a detailed discussion of the evaluation process, see [SecTrustEvaluate](<sectrustevaluate(____).md>).
