---
title: 'connection(_:didReceive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnectiondelegate/connection(_:didreceive:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didreceive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate/connection%28_%3Adidreceive%3A%29.json'
content_hash: 'sha256:35b0d866a4034265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDelegate](../nsurlconnectiondelegate.md)

# connection(_:didReceive:)

<sub>Instance Method</sub>

Sent when a connection must authenticate a challenge in order to download its request.

> [!warning] Deprecated
> Use -connection:willSendRequestForAuthenticationChallenge: instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, didReceive challenge: URLAuthenticationChallenge)
```

## Parameters

- `connection` — The connection sending the message.

- `challenge` — The challenge that `connection` must authenticate in order to download its request.

## Discussion

This method gives the delegate the opportunity to determine the course of action taken for the challenge: provide credentials, continue without providing credentials, or cancel the authentication challenge and the download.

> [!note] Note
> This method is not called if the delegate implements the [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) method.

The delegate can determine the number of previous authentication challenges by sending the message [previousFailureCount](../urlauthenticationchallenge/previousfailurecount.md) to `challenge`.

If the previous failure count is 0 and the value returned by [proposedCredential](../urlauthenticationchallenge/proposedcredential.md) is `nil`, the delegate can create a new NSURLCredential object, providing information specific to the type of credential, and send a [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>) message to `[challenge sender]`, passing the credential and `challenge` as parameters. If [proposedCredential](../urlauthenticationchallenge/proposedcredential.md) is not `nil`, the value is a credential from the URL or the shared credential storage that can be provided to the user as feedback.

The delegate may decide to abandon further attempts at authentication at any time by sending `[challenge sender]` a [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) or a [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>) message. The specific action is implementation dependent.

If the delegate implements this method, the download will suspend until `[challenge sender]` is sent one of the following messages: [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>), [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) or [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>).

If the delegate does not implement this method the default implementation is used. If a valid credential for the request is provided as part of the URL, or is available from the NSURLCredentialStorage the `[challenge sender]` is sent a [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>) with the credential. If the challenge has no credential or the credentials fail to authorize access, then [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) is sent to `[challenge sender]` instead.

## See Also

### Related Documentation

- [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>) — Attempt to use a given credential for a given authentication challenge.
- [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) — Attempt to continue downloading a request without providing a credential for a given challenge.
- [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>) — Cancels a given authentication challenge.

### Connection Authentication

- [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) — Tells the delegate that the connection will send a request for an authentication challenge.
- [- connection:canAuthenticateAgainstProtectionSpace:](<connection(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication. _(deprecated)_
- [- connection:didCancelAuthenticationChallenge:](<connection(__didcancel_).md>) — Sent when a connection cancels an authentication challenge. _(deprecated)_
- [- connectionShouldUseCredentialStorage:](<connectionshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should use the credential storage for authenticating the connection.
