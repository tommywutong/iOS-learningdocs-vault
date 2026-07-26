---
title: previousFailureCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge/previousfailurecount
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/previousfailurecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/previousfailurecount.json'
content_hash: 'sha256:1e220bbf0e194fcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# previousFailureCount

<sub>Instance Property</sub>

The receiver’s count of failed authentication attempts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var previousFailureCount: Int { get }
```

## Discussion

The previous failure count includes failures from _all_ protection spaces, not just the current one.

## See Also

### Getting properties of previous authentication attempts

- [failureResponse](failureresponse.md) — The URL response object representing the last authentication failure.
- [proposedCredential](proposedcredential.md) — The proposed credential for this challenge.
