---
title: 'init(type:fileDescriptor:queue:cleanupHandler:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/init(type:filedescriptor:queue:cleanuphandler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/init(type:filedescriptor:queue:cleanuphandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/init%28type%3Afiledescriptor%3Aqueue%3Acleanuphandler%3A%29.json'
content_hash: 'sha256:d3173d8c60df90cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# init(type:fileDescriptor:queue:cleanupHandler:)

<sub>Initializer</sub>

Creates a new I/O channel that accesses the specified file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(type: DispatchIO.StreamType, fileDescriptor: Int32, queue: DispatchQueue, cleanupHandler: @escaping (Int32) -> Void)
```

## Parameters

- `type` — The access semantics for the channel. For a list of possible values, see [StreamType](streamtype.md).

- `fileDescriptor` — The file descriptor from which to read or write data.

- `queue` — The dispatch queue on which to perform work.

- `cleanupHandler` — The handler to execute once the channel is closed. This block has no return value and takes the following parameter: - **error** — An `errno` condition if creating or opening the channel failed; otherwise, the value is `0`.

## Discussion

The channel takes control of the specified file descriptor until the channel closes, either deliberately on your part or because an error occurred. While the channel owns the file descriptor, the system modifies flags such as `O_NONBLOCK` automatically. It is a programmer error for you to modify the file descriptor while the channel owns it. However, you may create additional channels based on the same file descriptor.

## See Also

### Creating a Dispatch I/O Object

- [init(type:path:oflag:mode:queue:cleanupHandler:)](<init(type_path_oflag_mode_queue_cleanuphandler_)-50rb0.md>) — Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [init(type:io:queue:cleanupHandler:)](<init(type_io_queue_cleanuphandler_).md>) — Creates a new I/O channel from an existing I/O channel.
- [StreamType](streamtype.md) — The semantics for accessing the contents of a file descriptor.
