---
title: 'connection(_:willSendRequestFor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondelegate/connection(_:willsendrequestfor:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:willsendrequestfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate/connection%28_%3Awillsendrequestfor%3A%29.json'
content_hash: 'sha256:b872955953ff77fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDelegate](../nsurlconnectiondelegate.md)

# connection(_:willSendRequestFor:)

<sub>Instance Method</sub>

Tells the delegate that the connection will send a request for an authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, willSendRequestFor challenge: URLAuthenticationChallenge)
```

## Parameters

- `connection` — The connection sending the message.

- `challenge` — The authentication challenge for which a request is being sent.

## Discussion

This method allows the delegate to make an informed decision about connection authentication at once. If the delegate implements this method, it has no need to implement [- connection:canAuthenticateAgainstProtectionSpace:](<connection(__canauthenticateagainstprotectionspace_).md>) or [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>). In fact, those other methods are not invoked (except on older operating systems, where applicable).

In this method,you _must_ invoke one of the challenge-responder methods ([URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md) protocol):

- [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>)
- [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>)
- [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>)
- [- performDefaultHandlingForAuthenticationChallenge:](<../urlauthenticationchallengesender/performdefaulthandling(for_).md>)
- [- rejectProtectionSpaceAndContinueWithChallenge:](<../urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with_).md>)

> [!important] Important
> Your delegate method is called on the thread where the connection is scheduled. Always call the methods above on that same thread.

You might also want to analyze `challenge` for the authentication scheme and the proposed credential before calling a [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md) method. You should never assume that a proposed credential is present. You can either create your own credential and respond with that, or you can send the proposed credential back. (Because this object is immutable, if you want to change it you must copy it and then modify the copy.)

## See Also

### Related Documentation

- [URL Loading System](../url-loading-system.md) — Interact with URLs and communicate with servers using standard Internet protocols.

### Connection Authentication

- [- connection:canAuthenticateAgainstProtectionSpace:](<connection(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication. _(deprecated)_
- [- connection:didCancelAuthenticationChallenge:](<connection(__didcancel_).md>) — Sent when a connection cancels an authentication challenge. _(deprecated)_
- [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>) — Sent when a connection must authenticate a challenge in order to download its request. _(deprecated)_
- [- connectionShouldUseCredentialStorage:](<connectionshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should use the credential storage for authenticating the connection.
