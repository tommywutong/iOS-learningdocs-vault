---
title: DispatchSourceWrite
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourcewrite
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcewrite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcewrite.json'
content_hash: 'sha256:2bbcc90ce5f47858'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceWrite

<sub>Protocol</sub>

A dispatch source object for writing data to a file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceWrite : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeWriteSource(fileDescriptor:queue:)](<dispatchsource/makewritesource(filedescriptor_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## See Also

### Creating a File System Source

- [makeReadSource(fileDescriptor:queue:)](<dispatchsource/makereadsource(filedescriptor_queue_).md>) — Creates a new dispatch source object for reading bytes from the specified file.
- [makeWriteSource(fileDescriptor:queue:)](<dispatchsource/makewritesource(filedescriptor_queue_).md>) — Creates a new dispatch source object for writing data to the specified file.
- [makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)](<dispatchsource/makefilesystemobjectsource(filedescriptor_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring file-system events.
- [DispatchSourceRead](dispatchsourceread.md) — A dispatch source object for reading data from a file descriptor.
- [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md) — A dispatch source that monitors events associated with a file descriptor.
- [FileSystemEvent](dispatchsource/filesystemevent.md) — Events involving a change to a file system object.
