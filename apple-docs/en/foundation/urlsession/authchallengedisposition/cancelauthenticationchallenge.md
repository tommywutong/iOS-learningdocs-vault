---
title: URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/authchallengedisposition/cancelauthenticationchallenge
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/cancelauthenticationchallenge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/authchallengedisposition/cancelauthenticationchallenge.json'
content_hash: 'sha256:1103002550c871ac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSession](../../urlsession.md) · [AuthChallengeDisposition](../authchallengedisposition.md)

# URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge

<sub>Case</sub>

Cancel the entire request. The provided credential parameter is ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancelAuthenticationChallenge
```

## See Also

### Constants

- [NSURLSessionAuthChallengeUseCredential](usecredential.md) — Use the specified credential, which may be `nil`.
- [NSURLSessionAuthChallengePerformDefaultHandling](performdefaulthandling.md) — Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [NSURLSessionAuthChallengeRejectProtectionSpace](rejectprotectionspace.md) — Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.
