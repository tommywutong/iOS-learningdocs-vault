---
title: 'connectionShouldUseCredentialStorage(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate/connectionshouldusecredentialstorage%28_%3A%29.json'
content_hash: 'sha256:43e5a0fc926bb74c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDelegate](../nsurlconnectiondelegate.md)

# connectionShouldUseCredentialStorage(_:)

<sub>Instance Method</sub>

Sent to determine whether the URL loader should use the credential storage for authenticating the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connectionShouldUseCredentialStorage(_ connection: NSURLConnection) -> Bool
```

## Parameters

- `connection` — The connection sending the message.

## Discussion

This method is called before any attempt to authenticate is made.

If you return [false](../../swift/false.md), the connection does not consult the credential storage automatically, and does not store credentials. However, in your connection:didReceiveAuthenticationChallenge: method, you can consult the credential storage yourself and store credentials yourself, as needed.

Not implementing this method is the same as returning [true](../../swift/true.md).

> [!important] Important
> Prior to iOS 7 and OS X v10.9, the `connectionShouldUseCredentialStorage:` method is never called on delegates that implement the [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) method.
>
> In later operating systems, if the delegate implements the [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) method, the `connectionShouldUseCredentialStorage:` method is called _only_ if the app’s deployment target is at least iOS 7 or OS X v10.9.

## See Also

### Connection Authentication

- [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) — Tells the delegate that the connection will send a request for an authentication challenge.
- [- connection:canAuthenticateAgainstProtectionSpace:](<connection(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication. _(deprecated)_
- [- connection:didCancelAuthenticationChallenge:](<connection(__didcancel_).md>) — Sent when a connection cancels an authentication challenge. _(deprecated)_
- [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>) — Sent when a connection must authenticate a challenge in order to download its request. _(deprecated)_
