---
title: 'makeNewConnection:sender:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnectiondelegate/makenewconnection:sender:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate/makenewconnection:sender:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate/makenewconnection%3Asender%3A.json'
content_hash: 'sha256:e2bff072a7abc0ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnectionDelegate](../nsconnectiondelegate.md)

# makeNewConnection:sender:

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) makeNewConnection:(NSConnection *) conn sender:(NSConnection *) ancestor;
```

## Parameters

- `conn` — The new connection.

- `ancestor` — The parent connection.

## Return Value

[true](../../swift/true.md) if `ancestor` should allow `conn` to be created and configured, [false](../../swift/false.md) if `ancestor` should refuse and immediately release `conn`.

## Discussion

Use this method to limit the number of `NSConnection` objects created in your application or to change the parameters of child `NSConnection` objects.

Use [NSConnectionDidInitializeNotification](../nsconnectiondidinitializenotification.md) instead of this delegate method if possible.

## See Also

### Responding to a Connection

- [connection:shouldMakeNewConnection:](connection_shouldmakenewconnection_.md) — Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created. _(deprecated)_
- [connection:handleRequest:](connection_handlerequest_.md) — This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests. _(deprecated)_
- [createConversationForConnection:](createconversationforconnection_.md) — Returns an arbitrary object identifying a new conversation being created for the connection in the current thread. _(deprecated)_
