---
title: extractConnection()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/message/extractconnection()
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/message/extractconnection()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/message/extractconnection%28%29.json'
content_hash: 'sha256:127397845ac7389f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnectionGroup](../../nwconnectiongroup.md) · [Message](../message.md)

# extractConnection()

<sub>Instance Method</sub>

Converts a message you receive from an endpoint into a connection object that you use for long-term communication with that endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extractConnection() -> NWConnection?
```

## See Also

### Replying to Received Messages

- [reply(content:message:)](<reply(content_message_).md>) — Sends a reply to the specific endpoint that originates a group message you receive.
