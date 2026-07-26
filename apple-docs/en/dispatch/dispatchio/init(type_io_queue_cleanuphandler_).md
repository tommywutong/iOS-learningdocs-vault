---
title: 'init(type:io:queue:cleanupHandler:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/init(type:io:queue:cleanuphandler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/init(type:io:queue:cleanuphandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/init%28type%3Aio%3Aqueue%3Acleanuphandler%3A%29.json'
content_hash: 'sha256:843956840d4e6252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# init(type:io:queue:cleanupHandler:)

<sub>Initializer</sub>

Creates a new I/O channel from an existing I/O channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(type: DispatchIO.StreamType, io: DispatchIO, queue: DispatchQueue, cleanupHandler: @escaping (Int32) -> Void)
```

## Parameters

- `type` — The access semantics for the channel. For a list of possible values, see [StreamType](streamtype.md).

- `io` — An existing channel.

- `queue` — The dispatch queue on which to perform work.

- `cleanupHandler` — The handler to execute once the channel is closed. This block has no return value and takes the following parameter: - **error** — An `errno` condition if creating or opening the channel failed; otherwise, the value is `0`.

## See Also

### Creating a Dispatch I/O Object

- [init(type:fileDescriptor:queue:cleanupHandler:)](<init(type_filedescriptor_queue_cleanuphandler_).md>) — Creates a new I/O channel that accesses the specified file descriptor.
- [init(type:path:oflag:mode:queue:cleanupHandler:)](<init(type_path_oflag_mode_queue_cleanuphandler_)-50rb0.md>) — Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [StreamType](streamtype.md) — The semantics for accessing the contents of a file descriptor.
