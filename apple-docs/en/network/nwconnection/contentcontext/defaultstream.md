---
title: defaultStream
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/contentcontext/defaultstream
source_url: 'https://developer.apple.com/documentation/network/nwconnection/contentcontext/defaultstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/contentcontext/defaultstream.json'
content_hash: 'sha256:787dcc0bf897e936'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [ContentContext](../contentcontext.md)

# defaultStream

<sub>Type Property</sub>

A static context representing the total stream of bytes on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let defaultStream: NWConnection.ContentContext
```

## Discussion

Once this context is used for sending, and the send is marked as complete, no more data can be sent on the connection.

## See Also

### Using Constant Send Contexts

- [defaultMessage](defaultmessage.md) — A static context representing a message with default properties.
- [finalMessage](finalmessage.md) — A static context that’s marked as the final message in a connection.
