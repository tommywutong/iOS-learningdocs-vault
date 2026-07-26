---
title: DispatchIO.StreamType
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchio/streamtype
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/streamtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/streamtype.json'
content_hash: 'sha256:824c5420111c2da4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# DispatchIO.StreamType

<sub>Enumeration</sub>

The semantics for accessing the contents of a file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum StreamType
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Stream Types

- [DispatchIO.StreamType.stream](streamtype/stream.md) — Access content sequentially, in a stream.
- [DispatchIO.StreamType.random](streamtype/random.md) — Access content randomly.

### Initializing the Type

- [DISPATCH_IO_RANDOM](../dispatch_io_random.md)
- [DISPATCH_IO_STREAM](../dispatch_io_stream.md)

## See Also

### Creating a Dispatch I/O Object

- [init(type:fileDescriptor:queue:cleanupHandler:)](<init(type_filedescriptor_queue_cleanuphandler_).md>) — Creates a new I/O channel that accesses the specified file descriptor.
- [init(type:path:oflag:mode:queue:cleanupHandler:)](<init(type_path_oflag_mode_queue_cleanuphandler_)-50rb0.md>) — Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [init(type:io:queue:cleanupHandler:)](<init(type_io_queue_cleanuphandler_).md>) — Creates a new I/O channel from an existing I/O channel.
