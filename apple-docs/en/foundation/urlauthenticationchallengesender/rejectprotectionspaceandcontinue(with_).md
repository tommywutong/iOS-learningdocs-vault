---
title: 'rejectProtectionSpaceAndContinue(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallengesender/rejectprotectionspaceandcontinue%28with%3A%29.json'
content_hash: 'sha256:1652e1a061dbd28a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md)

# rejectProtectionSpaceAndContinue(with:)

<sub>Instance Method</sub>

Rejects the currently supplied protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func rejectProtectionSpaceAndContinue(with challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge` — The challenge that should be rejected.

## See Also

### Protocol Methods

- [- cancelAuthenticationChallenge:](<cancel(__).md>) — Cancels a given authentication challenge.
- [- continueWithoutCredentialForAuthenticationChallenge:](<continuewithoutcredential(for_).md>) — Attempt to continue downloading a request without providing a credential for a given challenge.
- [- useCredential:forAuthenticationChallenge:](<use(__for_).md>) — Attempt to use a given credential for a given authentication challenge.
- [- performDefaultHandlingForAuthenticationChallenge:](<performdefaulthandling(for_).md>) — Causes the system-provided default behavior to be used.
