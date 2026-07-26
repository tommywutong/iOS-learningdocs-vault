---
title: URLSession.AuthChallengeDisposition
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/authchallengedisposition
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/authchallengedisposition.json'
content_hash: 'sha256:d0768221913dccc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# URLSession.AuthChallengeDisposition

<sub>Enumeration</sub>

Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AuthChallengeDisposition
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSURLSessionAuthChallengeUseCredential](authchallengedisposition/usecredential.md) — Use the specified credential, which may be `nil`.
- [NSURLSessionAuthChallengePerformDefaultHandling](authchallengedisposition/performdefaulthandling.md) — Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [NSURLSessionAuthChallengeCancelAuthenticationChallenge](authchallengedisposition/cancelauthenticationchallenge.md) — Cancel the entire request. The provided credential parameter is ignored.
- [NSURLSessionAuthChallengeRejectProtectionSpace](authchallengedisposition/rejectprotectionspace.md) — Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.

### Initializers

- [init(rawValue:)](<authchallengedisposition/init(rawvalue_).md>)

## See Also

### Handling authentication challenges

- [- URLSession:didReceiveChallenge:completionHandler:](<../urlsessiondelegate/urlsession(__didreceive_completionhandler_).md>) — Requests credentials from the delegate in response to a session-level authentication request from the remote server.
