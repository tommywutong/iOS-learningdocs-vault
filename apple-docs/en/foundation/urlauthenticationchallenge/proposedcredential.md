---
title: proposedCredential
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge/proposedcredential
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/proposedcredential'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/proposedcredential.json'
content_hash: 'sha256:6ae44b4bf9e762bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# proposedCredential

<sub>Instance Property</sub>

The proposed credential for this challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var proposedCredential: URLCredential? { get }
```

## Discussion

This method returns `nil` if there is no default credential for this challenge.

If you have previously attempted to authenticate and failed, this method returns the most recent failed credential.

If the proposed credential is not `nil` and returns [true](../../swift/true.md) when you call its [hasPassword](../urlcredential/haspassword.md) method, then the credential is ready to use as-is. If the proposed credential’s [hasPassword](../urlcredential/haspassword.md) method returns [false](../../swift/false.md), then the credential provides a default user name, and the client must prompt the user for a corresponding password.

## See Also

### Getting properties of previous authentication attempts

- [failureResponse](failureresponse.md) — The URL response object representing the last authentication failure.
- [previousFailureCount](previousfailurecount.md) — The receiver’s count of failed authentication attempts.
