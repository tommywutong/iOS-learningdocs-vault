---
title: 'SecTrustGetTrustResult(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustgettrustresult(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustgettrustresult(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgettrustresult%28_%3A_%3A%29.json'
content_hash: 'sha256:6180ff418faa16ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetTrustResult(_:_:)

<sub>Function</sub>

Returns the result code from the most recent trust evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustGetTrustResult(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus
```

## Parameters

- `trust` — The trust object from which results should be obtained

- `result` — A pointer that the function sets to point at a value that is the result type. See [SecTrustResultType](sectrustresulttype.md) for possible values.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If the trust object has not yet been evaluated, the result type is [kSecTrustResultInvalid](sectrustresulttype/invalid.md).
