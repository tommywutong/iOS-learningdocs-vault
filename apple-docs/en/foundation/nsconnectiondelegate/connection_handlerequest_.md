---
title: 'connection:handleRequest:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnectiondelegate/connection:handlerequest:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate/connection:handlerequest:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate/connection%3Ahandlerequest%3A.json'
content_hash: 'sha256:6cf22862bcdc75d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnectionDelegate](../nsconnectiondelegate.md)

# connection:handleRequest:

<sub>Instance Method</sub>

This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) connection:(NSConnection *) connection handleRequest:(NSDistantObjectRequest *) doreq;
```

## Parameters

- `connection` — The connection object for which the receiver is the delegate.

- `doreq` — The distant object request.

## Return Value

[true](../../swift/true.md) if the request was handled by the delegate, [false](../../swift/false.md) if the request should proceed as if the delegate did not intercept it.

## See Also

### Responding to a Connection

- [connection:shouldMakeNewConnection:](connection_shouldmakenewconnection_.md) — Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created. _(deprecated)_
- [createConversationForConnection:](createconversationforconnection_.md) — Returns an arbitrary object identifying a new conversation being created for the connection in the current thread. _(deprecated)_
- [makeNewConnection:sender:](makenewconnection_sender_.md) — Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured. _(deprecated)_
