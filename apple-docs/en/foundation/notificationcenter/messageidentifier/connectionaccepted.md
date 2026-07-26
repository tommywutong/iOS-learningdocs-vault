---
title: connectionAccepted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/connectionaccepted
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/connectionaccepted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/connectionaccepted.json'
content_hash: 'sha256:01a40f47b9f6e47d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# connectionAccepted

<sub>Type Property</sub>

An identifier for a message about a file handle accepting a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var connectionAccepted: NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [ConnectionAcceptedMessage](../../filehandle/connectionacceptedmessage.md).

## See Also

### Identifying file handle messages

- [dataAvailable](dataavailable.md) — An identifier for a message about a file handle having data available for reading.
- [readToEndOfFileCompletion](readtoendoffilecompletion.md) — An identifier for a message about a file handle having reached the end of a file or communication channel.
- [readCompletion](readcompletion.md) — An identifier for a message about a file handle having read the currently available data from a file or communication channel.
