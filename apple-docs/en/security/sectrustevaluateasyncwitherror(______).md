---
title: 'SecTrustEvaluateAsyncWithError(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustevaluateasyncwitherror(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustevaluateasyncwitherror(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustevaluateasyncwitherror%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8611a69ad303ef27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustEvaluateAsyncWithError(_:_:_:)

<sub>Function</sub>

Evaluates a trust object asynchronously on the specified dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustEvaluateAsyncWithError(_ trust: SecTrust, _ queue: dispatch_queue_t, _ result: @escaping SecTrustWithErrorCallback) -> OSStatus
```

## Parameters

- `trust` — The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `queue` — The dispatch queue on which the result block should execute. You must call the method from the same queue.

- `result` — A closure that the method calls to report the result of trust evaluation. The method calls the closure exactly once if the method returns [errSecSuccess](errsecsuccess.md), and not at all otherwise. The method might call the closure synchronously in some cases, before returning.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This method behaves like [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>), except that it provides an evaluation by calling the given closure. The method might do this synchronously before returning if the trust instance already contains a result. Otherwise, the method returns immediately, performs the evaluation asynchronously, and calls the closure with the result later.

> [!important] Important
> You must call this method from the same dispatch queue that you specify as the `queue` parameter.
