---
title: 'send(content:to:message:completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnectiongroup/send(content:to:message:completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/send(content:to:message:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/send%28content%3Ato%3Amessage%3Acompletion%3A%29.json'
content_hash: 'sha256:e22091b7cab9b974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# send(content:to:message:completion:)

<sub>Instance Method</sub>

Sends data to the entire group, or to a specific member of the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func send(content: Data?, to: NWEndpoint? = nil, message: NWConnectionGroup.Message = .default, completion: @escaping (NWError?) -> Void)
```

## Parameters

- `content` — The data to send.

- `to` — An optional endpoint that specifies a member of the group that receives the data. If the endpoint is `nil`, the data will be sent to the entire group.

- `message` — The metadata that defines how the message is sent.

- `completion` — A completion that notifies you when the connection group has processed and sent the data.

## See Also

### Sending and Receiving Group Messages

- [setReceiveHandler(maximumMessageSize:rejectOversizedMessages:handler:)](<setreceivehandler(maximummessagesize_rejectoversizedmessages_handler_).md>) — Sets a handler that receives inbound messages from members of the group.
- [Message](message.md) — An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.
