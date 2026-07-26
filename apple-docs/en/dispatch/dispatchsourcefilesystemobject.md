---
title: DispatchSourceFileSystemObject
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourcefilesystemobject
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcefilesystemobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcefilesystemobject.json'
content_hash: 'sha256:fdda20cc33e17549'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceFileSystemObject

<sub>Protocol</sub>

A dispatch source that monitors events associated with a file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceFileSystemObject : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)](<dispatchsource/makefilesystemobjectsource(filedescriptor_eventmask_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Getting the Data Handle

- [handle](dispatchsourcefilesystemobject/handle.md) — The file descriptor of the file or socket.

### Getting the Event Data

- [data](dispatchsourcefilesystemobject/data.md) — The type of the last file system event.
- [mask](dispatchsourcefilesystemobject/mask.md) — The file descriptor attributes being monitored by the dispatch source.

## See Also

### Creating a File System Source

- [makeReadSource(fileDescriptor:queue:)](<dispatchsource/makereadsource(filedescriptor_queue_).md>) — Creates a new dispatch source object for reading bytes from the specified file.
- [makeWriteSource(fileDescriptor:queue:)](<dispatchsource/makewritesource(filedescriptor_queue_).md>) — Creates a new dispatch source object for writing data to the specified file.
- [makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)](<dispatchsource/makefilesystemobjectsource(filedescriptor_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring file-system events.
- [DispatchSourceRead](dispatchsourceread.md) — A dispatch source object for reading data from a file descriptor.
- [DispatchSourceWrite](dispatchsourcewrite.md) — A dispatch source object for writing data to a file descriptor.
- [FileSystemEvent](dispatchsource/filesystemevent.md) — Events involving a change to a file system object.
