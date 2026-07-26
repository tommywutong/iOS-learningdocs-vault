---
title: URLSessionDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiondelegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondelegate.json'
content_hash: 'sha256:35c1dc675e0e5a86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionDelegate

<sub>Protocol</sub>

A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLSessionDelegate : NSObjectProtocol, Sendable
```

## Overview

In addition to the methods defined in this protocol, most delegates should also implement some or all of the methods in the [URLSessionTaskDelegate](urlsessiontaskdelegate.md), [URLSessionDataDelegate](urlsessiondatadelegate.md), and [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) protocols to handle task-level events. These include events like the beginning and end of individual tasks, and periodic progress updates from data or download tasks.

> [!note] Note
> Your [URLSession](urlsession.md) object doesn’t need to have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [URLSessionDataDelegate](urlsessiondatadelegate.md), [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md), [URLSessionStreamDelegate](urlsessionstreamdelegate.md), [URLSessionTaskDelegate](urlsessiontaskdelegate.md), [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)

## Topics

### Handling session life cycle changes

- [- URLSession:didBecomeInvalidWithError:](<urlsessiondelegate/urlsession(__didbecomeinvalidwitherror_).md>) — Tells the URL session that the session has been invalidated.
- [- URLSessionDidFinishEventsForBackgroundURLSession:](<urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession_).md>) — Tells the delegate that all messages enqueued for a session have been delivered.

### Handling authentication challenges

- [- URLSession:didReceiveChallenge:completionHandler:](<urlsessiondelegate/urlsession(__didreceive_completionhandler_).md>) — Requests credentials from the delegate in response to a session-level authentication request from the remote server.
- [AuthChallengeDisposition](urlsession/authchallengedisposition.md) — Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.

## See Also

### Working with a delegate

- [delegate](urlsession/delegate.md) — The delegate assigned when this object was created.
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
- [delegateQueue](urlsession/delegatequeue.md) — The operation queue provided when this object was created.
