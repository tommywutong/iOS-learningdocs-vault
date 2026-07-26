---
title: 'setReceiveHandler(maximumMessageSize:rejectOversizedMessages:handler:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnectiongroup/setreceivehandler(maximummessagesize:rejectoversizedmessages:handler:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/setreceivehandler(maximummessagesize:rejectoversizedmessages:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/setreceivehandler%28maximummessagesize%3Arejectoversizedmessages%3Ahandler%3A%29.json'
content_hash: 'sha256:33b1fb94988ec06f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# setReceiveHandler(maximumMessageSize:rejectOversizedMessages:handler:)

<sub>Instance Method</sub>

Sets a handler that receives inbound messages from members of the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func setReceiveHandler(maximumMessageSize: Int = Int.max, rejectOversizedMessages: Bool = true, handler: (@Sendable (NWConnectionGroup.Message, Data?, Bool) -> Void)?)
```

## See Also

### Sending and Receiving Group Messages

- [send(content:to:message:completion:)](<send(content_to_message_completion_).md>) — Sends data to the entire group, or to a specific member of the group.
- [Message](message.md) — An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.
