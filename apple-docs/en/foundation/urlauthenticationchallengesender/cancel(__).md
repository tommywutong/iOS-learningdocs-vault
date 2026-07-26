---
title: 'cancel(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlauthenticationchallengesender/cancel(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/cancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallengesender/cancel%28_%3A%29.json'
content_hash: 'sha256:47e2cca8fc8d42c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md)

# cancel(_:)

<sub>Instance Method</sub>

Cancels a given authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel(_ challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge` — The authentication challenge to cancel.

## See Also

### Related Documentation

- [URL Loading System](../url-loading-system.md) — Interact with URLs and communicate with servers using standard Internet protocols.

### Protocol Methods

- [- continueWithoutCredentialForAuthenticationChallenge:](<continuewithoutcredential(for_).md>) — Attempt to continue downloading a request without providing a credential for a given challenge.
- [- useCredential:forAuthenticationChallenge:](<use(__for_).md>) — Attempt to use a given credential for a given authentication challenge.
- [- performDefaultHandlingForAuthenticationChallenge:](<performdefaulthandling(for_).md>) — Causes the system-provided default behavior to be used.
- [- rejectProtectionSpaceAndContinueWithChallenge:](<rejectprotectionspaceandcontinue(with_).md>) — Rejects the currently supplied protection space.
