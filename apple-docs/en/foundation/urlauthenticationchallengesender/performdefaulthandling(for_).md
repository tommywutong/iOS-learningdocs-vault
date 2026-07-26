---
title: 'performDefaultHandling(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlauthenticationchallengesender/performdefaulthandling(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/performdefaulthandling(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallengesender/performdefaulthandling%28for%3A%29.json'
content_hash: 'sha256:cce1cf080fe10aef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md)

# performDefaultHandling(for:)

<sub>Instance Method</sub>

Causes the system-provided default behavior to be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func performDefaultHandling(for challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge` — The challenge for which the default behavior should be used.

## See Also

### Protocol Methods

- [- cancelAuthenticationChallenge:](<cancel(__).md>) — Cancels a given authentication challenge.
- [- continueWithoutCredentialForAuthenticationChallenge:](<continuewithoutcredential(for_).md>) — Attempt to continue downloading a request without providing a credential for a given challenge.
- [- useCredential:forAuthenticationChallenge:](<use(__for_).md>) — Attempt to use a given credential for a given authentication challenge.
- [- rejectProtectionSpaceAndContinueWithChallenge:](<rejectprotectionspaceandcontinue(with_).md>) — Rejects the currently supplied protection space.
