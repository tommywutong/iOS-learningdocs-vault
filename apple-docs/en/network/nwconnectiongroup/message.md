---
title: NWConnectionGroup.Message
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/message
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/message'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/message.json'
content_hash: 'sha256:456c2d4b54fce189'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# NWConnectionGroup.Message

<sub>Class</sub>

An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Message
```

## Relationships

- **Inherits From**: [ContentContext](../nwconnection/contentcontext.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting Received Messages

- [remoteEndpoint](message/remoteendpoint.md) — The endpoint that originates the message you receive.
- [localEndpoint](message/localendpoint.md) — The local address and port you use to receive the message.
- [path](message/path.md) — The network path on which you receive the message.

### Replying to Received Messages

- [reply(content:message:)](<message/reply(content_message_).md>) — Sends a reply to the specific endpoint that originates a group message you receive.
- [extractConnection()](<message/extractconnection().md>) — Converts a message you receive from an endpoint into a connection object that you use for long-term communication with that endpoint.

### Sending Messages

- [default](message/default.md) — A static object you use to send a message with default properties.
- [init(identifier:expiration:priority:isFinal:antecedent:metadata:)](<message/init(identifier_expiration_priority_isfinal_antecedent_metadata_).md>) — Initializes a custom message context you use to send data.

### Initializers

- [init(nw:)](<message/init(nw_).md>)

### Instance Methods

- [metadata(definition:)](<message/metadata(definition_).md>)

## See Also

### Sending and Receiving Group Messages

- [setReceiveHandler(maximumMessageSize:rejectOversizedMessages:handler:)](<setreceivehandler(maximummessagesize_rejectoversizedmessages_handler_).md>) — Sets a handler that receives inbound messages from members of the group.
- [send(content:to:message:completion:)](<send(content_to_message_completion_).md>) — Sends data to the entire group, or to a specific member of the group.
