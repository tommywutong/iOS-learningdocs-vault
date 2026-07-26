---
title: URLSession.AuthChallengeDisposition.useCredential
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/authchallengedisposition/usecredential
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/usecredential'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/authchallengedisposition/usecredential.json'
content_hash: 'sha256:ae2faa1559ca7b50'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSession](../../urlsession.md) · [AuthChallengeDisposition](../authchallengedisposition.md)

# URLSession.AuthChallengeDisposition.useCredential

<sub>Case</sub>

Use the specified credential, which may be `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case useCredential
```

## See Also

### Constants

- [NSURLSessionAuthChallengePerformDefaultHandling](performdefaulthandling.md) — Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [NSURLSessionAuthChallengeCancelAuthenticationChallenge](cancelauthenticationchallenge.md) — Cancel the entire request. The provided credential parameter is ignored.
- [NSURLSessionAuthChallengeRejectProtectionSpace](rejectprotectionspace.md) — Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.
