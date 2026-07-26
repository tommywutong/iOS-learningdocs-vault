---
title: 'download(_:didReceive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:didreceive:)-1pc0v'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didreceive:)-1pc0v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Adidreceive%3A%29-1pc0v.json'
content_hash: 'sha256:d20a33599ec2a543'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:didReceive:)

<sub>Instance Method</sub>

Sent when the URL download must authenticate a challenge in order to download the request.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, didReceive challenge: URLAuthenticationChallenge)
```

## Parameters

- `download` — The URL download object sending the message.

- `challenge` — The URL authentication challenge that must be authenticated in order to download the request.

## Discussion

This method gives the delegate the opportunity to determine the course of action taken for the challenge: provide credentials, continue without providing credentials or cancel the authentication challenge and the download.

The delegate can determine the number of previous authentication challenges by sending the message [previousFailureCount](../urlauthenticationchallenge/previousfailurecount.md) to `challenge`.

If the previous failure count is 0 and the value returned by [proposedCredential](../urlauthenticationchallenge/proposedcredential.md) is `nil`, the delegate can create a new NSURLCredential object, providing information specific to the type of credential, and send a [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>) message to `[challenge sender]`, passing the credential and `challenge` as parameters. If [proposedCredential](../urlauthenticationchallenge/proposedcredential.md) is not `nil`, the value is a credential from the URL or the shared credential storage that can be provided to the user as feedback.

The delegate may decide to abandon further attempts at authentication at any time by sending `[challenge sender]` a [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) or a [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>) message. The specific action is implementation dependent.

If the delegate implements this method, the download will suspend until `[challenge sender]` is sent one of the following messages: [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>), [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) or [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>).

If the delegate does not implement this method the default implementation is used. If a valid credential for the request is provided as part of the URL, or is available from the NSURLCredentialStorage the `[challenge sender]` is sent a [- useCredential:forAuthenticationChallenge:](<../urlauthenticationchallengesender/use(__for_).md>) with the credential. If the challenge has no credential or the credentials fail to authorize access, then [- continueWithoutCredentialForAuthenticationChallenge:](<../urlauthenticationchallengesender/continuewithoutcredential(for_).md>) is sent to `[challenge sender]` instead.

## See Also

### Download Authentication

- [- download:canAuthenticateAgainstProtectionSpace:](<download(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [- download:didCancelAuthenticationChallenge:](<download(__didcancel_).md>) — Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [- downloadShouldUseCredentialStorage:](<downloadshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should consult the credential storage to authenticate the download.
