---
title: readToEndOfFileCompletion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier/readtoendoffilecompletion
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/readtoendoffilecompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/readtoendoffilecompletion.json'
content_hash: 'sha256:08b0e53fb88832f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# readToEndOfFileCompletion

<sub>Type Property</sub>

An identifier for a message about a file handle having reached the end of a file or communication channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var readToEndOfFileCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadToEndOfFileCompletionMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [ReadToEndOfFileCompletionMessage](../../filehandle/readtoendoffilecompletionmessage.md).

## See Also

### Identifying file handle messages

- [connectionAccepted](connectionaccepted.md) — An identifier for a message about a file handle accepting a connection.
- [dataAvailable](dataavailable.md) — An identifier for a message about a file handle having data available for reading.
- [readCompletion](readcompletion.md) — An identifier for a message about a file handle having read the currently available data from a file or communication channel.
