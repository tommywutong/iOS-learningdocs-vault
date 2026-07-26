---
title: readCompletion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/readcompletion
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/readcompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/readcompletion.json'
content_hash: 'sha256:290f013789706859'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# readCompletion

<sub>Type Property</sub>

An identifier for a message about a file handle having read the currently available data from a file or communication channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var readCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadCompletionMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [ReadCompletionMessage](../../filehandle/readcompletionmessage.md).

## See Also

### Identifying file handle messages

- [connectionAccepted](connectionaccepted.md) — An identifier for a message about a file handle accepting a connection.
- [dataAvailable](dataavailable.md) — An identifier for a message about a file handle having data available for reading.
- [readToEndOfFileCompletion](readtoendoffilecompletion.md) — An identifier for a message about a file handle having reached the end of a file or communication channel.
