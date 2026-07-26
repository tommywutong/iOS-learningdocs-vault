---
title: invocation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdistantobjectrequest/invocation
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/invocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobjectrequest/invocation.json'
content_hash: 'sha256:af6157aa860ab633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObjectRequest](../nsdistantobjectrequest.md)

# invocation

<sub>Instance Property</sub>

Returns the `NSInvocation` object for the request.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (retain, readonly) NSInvocation * invocation;
```

## Return Value

The `NSInvocation` object for the request.

## See Also

### Getting Information About a Request

- [connection](connection.md) — Returns the `NSConnection` object involved in the request. _(deprecated)_
- [conversation](conversation.md) — Returns the token object representing the conversation in which the receiver was created. _(deprecated)_
