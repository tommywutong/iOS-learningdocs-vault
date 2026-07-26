---
title: 'connection:shouldMakeNewConnection:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnectiondelegate/connection:shouldmakenewconnection:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate/connection:shouldmakenewconnection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate/connection%3Ashouldmakenewconnection%3A.json'
content_hash: 'sha256:e141e44d6ca29f55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnectionDelegate](../nsconnectiondelegate.md)

# connection:shouldMakeNewConnection:

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) connection:(NSConnection *) ancestor shouldMakeNewConnection:(NSConnection *) conn;
```

## Parameters

- `ancestor` — The connection object for which the receiver is the delegate.

- `conn` — The new connection.

## Return Value

[true](../../swift/true.md) if `ancestor` should allow `conn` to be created and set up, [false](../../swift/false.md) if `ancestor` should refuse and immediately release `conn`.

## Discussion

Use this method to limit the amount of `NSConnection` objects created in your application or to change the parameters of child `NSConnection` objects.

Use [NSConnectionDidInitializeNotification](../nsconnectiondidinitializenotification.md) instead of this delegate method if possible.

## See Also

### Responding to a Connection

- [connection:handleRequest:](connection_handlerequest_.md) — This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests. _(deprecated)_
- [createConversationForConnection:](createconversationforconnection_.md) — Returns an arbitrary object identifying a new conversation being created for the connection in the current thread. _(deprecated)_
- [makeNewConnection:sender:](makenewconnection_sender_.md) — Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured. _(deprecated)_
