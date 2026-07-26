---
title: 'connection(_:didCancel:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnectiondelegate/connection(_:didcancel:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didcancel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate/connection%28_%3Adidcancel%3A%29.json'
content_hash: 'sha256:93e3034803cd6e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDelegate](../nsurlconnectiondelegate.md)

# connection(_:didCancel:)

<sub>Instance Method</sub>

Sent when a connection cancels an authentication challenge.

> [!warning] Deprecated
> Use -connection:willSendRequestForAuthenticationChallenge: instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, didCancel challenge: URLAuthenticationChallenge)
```

## Parameters

- `connection` — The connection sending the message.

- `challenge` — The challenge that was canceled.

## See Also

### Connection Authentication

- [- connection:willSendRequestForAuthenticationChallenge:](<connection(__willsendrequestfor_).md>) — Tells the delegate that the connection will send a request for an authentication challenge.
- [- connection:canAuthenticateAgainstProtectionSpace:](<connection(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication. _(deprecated)_
- [- connection:didReceiveAuthenticationChallenge:](<connection(__didreceive_).md>) — Sent when a connection must authenticate a challenge in order to download its request. _(deprecated)_
- [- connectionShouldUseCredentialStorage:](<connectionshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should use the credential storage for authenticating the connection.
