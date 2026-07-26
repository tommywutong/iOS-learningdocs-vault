---
title: FileHandle.ReadCompletionMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/readcompletionmessage
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readcompletionmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readcompletionmessage.json'
content_hash: 'sha256:a286c1397510a616'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# FileHandle.ReadCompletionMessage

<sub>Structure</sub>

A message a file handle sends when it reads the data currently available in a file or a communication channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReadCompletionMessage
```

## Overview

Before adding an observer for this message type, call either [- readInBackgroundAndNotify](<readinbackgroundandnotify().md>) or [- readInBackgroundAndNotifyForModes:](<readinbackgroundandnotify(formodes_).md>) on an appropriate [FileHandle](../filehandle.md) object.

Observe this message with the identifier [readCompletion](../notificationcenter/messageidentifier/readcompletion.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [FileHandle](../filehandle.md).

This message interoperates with the notification [NSFileHandleReadCompletionNotification](readcompletionnotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init(dataItem:)](<readcompletionmessage/init(dataitem_).md>) — Creates a message that indicates a file handle read data.

### Working with message properties

- [dataItem](readcompletionmessage/dataitem.md) — A result instance containing either the data read from the file or connection, or else an error.

## See Also

### Working with notification messages

- [ConnectionAcceptedMessage](connectionacceptedmessage.md) — A message a file handle sends when it creates a socket connection between two processes and creates a file handle for one end of the connection.
- [DataAvailableMessage](dataavailablemessage.md) — A message a file handle sends when it determines data is available for reading from a file or communications channel.
- [ReadToEndOfFileCompletionMessage](readtoendoffilecompletionmessage.md) — A message a file handle sends when it reads all data in a file, or another process in a communication channel signals the end of the data.
