---
title: URLSession.AuthChallengeDisposition.rejectProtectionSpace
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/authchallengedisposition/rejectprotectionspace
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/rejectprotectionspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/authchallengedisposition/rejectprotectionspace.json'
content_hash: 'sha256:e1830b93feca68b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSession](../../urlsession.md) · [AuthChallengeDisposition](../authchallengedisposition.md)

# URLSession.AuthChallengeDisposition.rejectProtectionSpace

<sub>Case</sub>

Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case rejectProtectionSpace
```

## Discussion

The [NSURLSessionAuthChallengeRejectProtectionSpace](rejectprotectionspace.md) disposition is only appropriate in fairly unusual situations. For example, a Windows server might use both [NSURLAuthenticationMethodNegotiate](../../nsurlauthenticationmethodnegotiate.md) and [NSURLAuthenticationMethodNTLM](../../nsurlauthenticationmethodntlm.md). If your app can only handle NTLM, you would want to reject the Negotiate challenge, in order to then receive the queued NTLM challenge.

However, most apps won’t face this scenario, and if you cannot provide a credential for a certain authentication method, you should usually fall back to the [NSURLSessionAuthChallengePerformDefaultHandling](performdefaulthandling.md) disposition instead.

## See Also

### Constants

- [NSURLSessionAuthChallengeUseCredential](usecredential.md) — Use the specified credential, which may be `nil`.
- [NSURLSessionAuthChallengePerformDefaultHandling](performdefaulthandling.md) — Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [NSURLSessionAuthChallengeCancelAuthenticationChallenge](cancelauthenticationchallenge.md) — Cancel the entire request. The provided credential parameter is ignored.
