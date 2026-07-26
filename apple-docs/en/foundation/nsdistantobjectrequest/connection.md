---
title: connection
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdistantobjectrequest/connection
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/connection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobjectrequest/connection.json'
content_hash: 'sha256:93dd475956b9fd59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObjectRequest](../nsdistantobjectrequest.md)

# connection

<sub>Instance Property</sub>

Returns the `NSConnection` object involved in the request.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (retain, readonly) NSConnection * connection;
```

## Return Value

The `NSConnection` object involved in the request.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Getting Information About a Request

- [conversation](conversation.md) — Returns the token object representing the conversation in which the receiver was created. _(deprecated)_
- [invocation](invocation.md) — Returns the `NSInvocation` object for the request. _(deprecated)_
