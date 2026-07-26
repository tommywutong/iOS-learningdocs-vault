---
title: 'connection(_:canAuthenticateAgainstProtectionSpace:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate/connection%28_%3Acanauthenticateagainstprotectionspace%3A%29.json'
content_hash: 'sha256:6a35578f6ed050d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDelegate](../nsurlconnectiondelegate.md)

# connection(_:canAuthenticateAgainstProtectionSpace:)

<sub>Instance Method</sub>

Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.

> [!warning] Deprecated
> Use -connection:willSendRequestForAuthenticationChallenge: instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool
```

## Parameters

- `connection` — The connection sending the message.

- `protectionSpace` — The protection space that generates an authentication challenge.

## Return Value

[true](../../swift/true.md) if the delegate if able to respond to a protection space’s form of authentication, otherwise [false](../../swift/false.md).

## Discussion

This method is called before [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>), allowing the delegate to inspect a protection space before attempting to authenticate against it. By returning [true](../../swift/true.md), the delegate indicates that it can handle the form of authentication, which it does in the subsequent call to [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>). If the delegate returns [false](../../swift/false.md), the system attempts to use the user’s keychain to authenticate. If your delegate does not implement this method and the protection space uses client certificate authentication or server trust authentication, the system behaves as if you returned [false](../../swift/false.md). The system behaves as if you returned [true](../../swift/true.md) for all other authentication methods.

> [!note] Note
> This method is not called if the delegate implements the [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) method.

## See Also

### Connection Authentication

- [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) — Tells the delegate that the connection will send a request for an authentication challenge.
- [- connection:didCancelAuthenticationChallenge:](<connection(__didcancel_).md>) — Sent when a connection cancels an authentication challenge. _(deprecated)_
- [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>) — Sent when a connection must authenticate a challenge in order to download its request. _(deprecated)_
- [- connectionShouldUseCredentialStorage:](<connectionshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should use the credential storage for authenticating the connection.
