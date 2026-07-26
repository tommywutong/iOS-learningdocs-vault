---
title: 'SecTrustCopyResult(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustcopyresult(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustcopyresult(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustcopyresult%28_%3A%29.json'
content_hash: 'sha256:ae388a6829d9b47b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustCopyResult(_:)

<sub>Function</sub>

Returns a dictionary containing information about an evaluated trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustCopyResult(_ trust: SecTrust) -> CFDictionary?
```

## Parameters

- `trust` — The evaluated trust.

## Return Value

A dictionary containing keys with values that describe the result of the trust evaluation, or `NULL` when no information is available or if the trust has not been evaluated. See [Trust Result Dictionary Keys](trust-result-dictionary-keys.md) for the list of possible keys. In Objective-C, use [CFRelease](../corefoundation/cfrelease.md) to free the dictionary’s memory when you are done with it.

## Discussion

Call one of the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) or [SecTrustEvaluateAsyncWithError](<sectrustevaluateasyncwitherror(______).md>) methods before calling [SecTrustCopyResult](<sectrustcopyresult(__).md>).
