---
title: defaultMessage
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/contentcontext/defaultmessage
source_url: 'https://developer.apple.com/documentation/network/nwconnection/contentcontext/defaultmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/contentcontext/defaultmessage.json'
content_hash: 'sha256:50c80bf01c9fa3b4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [ContentContext](../contentcontext.md)

# defaultMessage

<sub>Type Property</sub>

A static context representing a message with default properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let defaultMessage: NWConnection.ContentContext
```

## Discussion

You should use this context for sending content unless there is a reason to override some values.

## See Also

### Using Constant Send Contexts

- [finalMessage](finalmessage.md) — A static context that’s marked as the final message in a connection.
- [defaultStream](defaultstream.md) — A static context representing the total stream of bytes on a connection.
