---
title: NSURLConnectionDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnectiondelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate.json'
content_hash: 'sha256:858be8e1db3f7368'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLConnectionDelegate

<sub>Protocol</sub>

A protocol that delegates of a URL connection implement to receive status about and provide feedback to the connection object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSURLConnectionDelegate : NSObjectProtocol
```

## Overview

Delegates of [NSURLConnection](nsurlconnection.md) objects should implement either the [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md) or [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md) protocol in addition to the [NSURLConnectionDelegate](nsurlconnectiondelegate.md) protocol. Specifically:

- If you are using [NSURLConnection](nsurlconnection.md) in conjunction with Newsstand Kit’s `download(with:)` method, the delegate class should implement the [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md) protocol.
- Otherwise, the delegate class should implement the [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md) protocol.

Delegates that wish to perform custom authentication handling should implement the [- connection:willSendRequestForAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__willsendrequestfor_).md>) method, which is the preferred mechanism for responding to authentication challenges. (See [URLAuthenticationChallenge](urlauthenticationchallenge.md) for more information on authentication challenges.) If [- connection:willSendRequestForAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__willsendrequestfor_).md>) is not implemented, the older, deprecated methods [- connection:canAuthenticateAgainstProtectionSpace:](<nsurlconnectiondelegate/connection(__canauthenticateagainstprotectionspace_).md>), [- connection:didReceiveAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__didreceive_).md>), and [- connection:didCancelAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__didcancel_).md>) are called instead.

The [- connection:didFailWithError:](<nsurlconnectiondelegate/connection(__didfailwitherror_).md>) method is called at most once if an error occurs during the loading of a resource. The [- connectionShouldUseCredentialStorage:](<nsurlconnectiondelegate/connectionshouldusecredentialstorage(__).md>) method is called once, just before the loading of a resource begins.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md), [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md)

## Topics

### Connection Authentication

- [- connection:willSendRequestForAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__willsendrequestfor_).md>) — Tells the delegate that the connection will send a request for an authentication challenge.
- [- connection:canAuthenticateAgainstProtectionSpace:](<nsurlconnectiondelegate/connection(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication. _(deprecated)_
- [- connection:didCancelAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__didcancel_).md>) — Sent when a connection cancels an authentication challenge. _(deprecated)_
- [- connection:didReceiveAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__didreceive_).md>) — Sent when a connection must authenticate a challenge in order to download its request. _(deprecated)_
- [- connectionShouldUseCredentialStorage:](<nsurlconnectiondelegate/connectionshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should use the credential storage for authenticating the connection.

### Connection Completion

- [- connection:didFailWithError:](<nsurlconnectiondelegate/connection(__didfailwitherror_).md>) — Sent when a connection fails to load its request successfully.

## See Also

### URL Connection

- [NSURLConnection](nsurlconnection.md) — An object that enables you to start and stop URL requests.
- [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md) — A protocol that most delegates of a URL connection implement to receive data associated with the connection.
- [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md) — A protocol that delegates of a URL connection created with Newsstand Kit implement to receive data associated with a download.
