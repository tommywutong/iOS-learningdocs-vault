---
title: currentConversation
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/currentconversation
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/currentconversation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/currentconversation.json'
content_hash: 'sha256:29608e5411f1d4b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# currentConversation

<sub>Type Method</sub>

Returns a token object representing any conversation in progress in the current thread.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) currentConversation;
```

## Return Value

A token object representing any conversation in progress in the current thread, or `nil` if there is no conversation in progress.

## See Also

### Related Documentation

- [createConversationForConnection:](../nsconnectiondelegate/createconversationforconnection_.md) — Returns an arbitrary object identifying a new conversation being created for the connection in the current thread. _(deprecated)_
