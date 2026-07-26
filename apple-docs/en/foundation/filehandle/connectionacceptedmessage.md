---
title: FileHandle.ConnectionAcceptedMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/connectionacceptedmessage
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/connectionacceptedmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/connectionacceptedmessage.json'
content_hash: 'sha256:5fd9e2b32d629a2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# FileHandle.ConnectionAcceptedMessage

<sub>Structure</sub>

A message a file handle sends when it creates a socket connection between two processes and creates a file handle for one end of the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ConnectionAcceptedMessage
```

## Overview

Before adding an observer for this message type, call either [- acceptConnectionInBackgroundAndNotify](<acceptconnectioninbackgroundandnotify().md>) or [- acceptConnectionInBackgroundAndNotifyForModes:](<acceptconnectioninbackgroundandnotify(formodes_).md>) on a [FileHandle](../filehandle.md) object that represents a server stream-type socket.

Observe this message with the identifier [connectionAccepted](../notificationcenter/messageidentifier/connectionaccepted.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [FileHandle](../filehandle.md).

This message interoperates with the notification [NSFileHandleConnectionAcceptedNotification](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init(fileHandleItem:)](<connectionacceptedmessage/init(filehandleitem_).md>) — Creates a message for a file handle connection acceptance.

### Working with message properties

- [fileHandleItem](connectionacceptedmessage/filehandleitem.md) — A result instance that contains either the file handle representing the “near” end of a socket connection, or an error.

## See Also

### Working with notification messages

- [DataAvailableMessage](dataavailablemessage.md) — A message a file handle sends when it determines data is available for reading from a file or communications channel.
- [ReadCompletionMessage](readcompletionmessage.md) — A message a file handle sends when it reads the data currently available in a file or a communication channel.
- [ReadToEndOfFileCompletionMessage](readtoendoffilecompletionmessage.md) — A message a file handle sends when it reads all data in a file, or another process in a communication channel signals the end of the data.
