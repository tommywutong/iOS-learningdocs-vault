---
title: failureResponse
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge/failureresponse
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/failureresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/failureresponse.json'
content_hash: 'sha256:cfe4a3b941e35fcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# failureResponse

<sub>Instance Property</sub>

The URL response object representing the last authentication failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var failureResponse: URLResponse? { get }
```

## Discussion

This value is `nil` if the protocol doesn’t use responses to indicate an authentication failure.

## See Also

### Related Documentation

- [error](error.md) — The error object representing the last authentication failure.

### Getting properties of previous authentication attempts

- [previousFailureCount](previousfailurecount.md) — The receiver’s count of failed authentication attempts.
- [proposedCredential](proposedcredential.md) — The proposed credential for this challenge.
