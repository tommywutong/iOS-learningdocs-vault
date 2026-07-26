---
title: conversation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdistantobjectrequest/conversation
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/conversation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobjectrequest/conversation.json'
content_hash: 'sha256:cc9b64f40f39e5c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObjectRequest](../nsdistantobjectrequest.md)

# conversation

<sub>Instance Property</sub>

Returns the token object representing the conversation in which the receiver was created.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (retain, readonly) id conversation;
```

## Return Value

The token object representing the conversation in which the receiver was created.

## Discussion

If both ends of the distributed objects connection has [independentConversationQueueing](../nsconnection/independentconversationqueueing.md) set to [false](../../swift/false.md) (the default), the conversation object is always `nil`. Otherwise, it is either a proxy (or a copy) of the object created by the sender of the message or a locally created object, depending which end of the connection has independent queueing on.

## See Also

### Getting Information About a Request

- [connection](connection.md) — Returns the `NSConnection` object involved in the request. _(deprecated)_
- [invocation](invocation.md) — Returns the `NSInvocation` object for the request. _(deprecated)_
