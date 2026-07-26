---
title: 'continueWithoutCredential(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlauthenticationchallengesender/continuewithoutcredential(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/continuewithoutcredential(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallengesender/continuewithoutcredential%28for%3A%29.json'
content_hash: 'sha256:d7ebc25fbe6a1cdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md)

# continueWithoutCredential(for:)

<sub>Instance Method</sub>

Attempt to continue downloading a request without providing a credential for a given challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func continueWithoutCredential(for challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge` — A challenge without authentication credentials.

## Discussion

This method has no effect if it is called with an authentication challenge that has already been handled.

## See Also

### Protocol Methods

- [- cancelAuthenticationChallenge:](<cancel(__).md>) — Cancels a given authentication challenge.
- [- useCredential:forAuthenticationChallenge:](<use(__for_).md>) — Attempt to use a given credential for a given authentication challenge.
- [- performDefaultHandlingForAuthenticationChallenge:](<performdefaulthandling(for_).md>) — Causes the system-provided default behavior to be used.
- [- rejectProtectionSpaceAndContinueWithChallenge:](<rejectprotectionspaceandcontinue(with_).md>) — Rejects the currently supplied protection space.
