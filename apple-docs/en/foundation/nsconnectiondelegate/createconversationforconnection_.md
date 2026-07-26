---
title: 'createConversationForConnection:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnectiondelegate/createconversationforconnection:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate/createconversationforconnection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate/createconversationforconnection%3A.json'
content_hash: 'sha256:4066baa2d01dbc36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnectionDelegate](../nsconnectiondelegate.md)

# createConversationForConnection:

<sub>Instance Method</sub>

Returns an arbitrary object identifying a new conversation being created for the connection in the current thread.

<sub>Mac Catalyst, macOS</sub>

```objc
- (id) createConversationForConnection:(NSConnection *) conn;
```

## Parameters

- `conn` — The connection object for which the receiver is the delegate.

## Return Value

An arbitrary object identifying a new conversation being created for the connection in the current thread.

## Discussion

New conversations are created only if [independentConversationQueueing](../nsconnection/independentconversationqueueing.md) is [true](../../swift/true.md) for `conn`. If you do not implement this method, `NSConnection` object creates an instance of `NSObject`.

## See Also

### Related Documentation

- [currentConversation](../nsconnection/currentconversation.md) — Returns a token object representing any conversation in progress in the current thread. _(deprecated)_

### Responding to a Connection

- [connection:shouldMakeNewConnection:](connection_shouldmakenewconnection_.md) — Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created. _(deprecated)_
- [connection:handleRequest:](connection_handlerequest_.md) — This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests. _(deprecated)_
- [makeNewConnection:sender:](makenewconnection_sender_.md) — Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured. _(deprecated)_
