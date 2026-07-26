---
title: 'init(type:path:oflag:mode:queue:cleanupHandler:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-50rb0'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-50rb0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/init%28type%3Apath%3Aoflag%3Amode%3Aqueue%3Acleanuphandler%3A%29-50rb0.json'
content_hash: 'sha256:17a17ef1086dd69d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# init(type:path:oflag:mode:queue:cleanupHandler:)

<sub>Initializer</sub>

Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: @escaping (Int32) -> Void)
```

## Parameters

- `type` — The access semantics for the channel. For a list of possible values, see [StreamType](streamtype.md).

- `path` — The absolute path of the file you want to open.

- `oflag` — The flags to pass to `open(2)` when opening the file at the specified path.

- `mode` — The mode flags to pass to `open(2)`. Specify `O_CREAT` to create the file at the specified path; otherwise, specify 0.

- `queue` — The dispatch queue on which to perform work.

- `cleanupHandler` — The handler to execute once the channel is closed. This block has no return value and takes the following parameter: - **error** — An `errno` condition if creating or opening the channel failed; otherwise, the value is `0`.

## Discussion

This method opens the channel by passing the `path`, `oflag`, and mode parameters to the low-level `open(2)` function. The file descriptor returned by that function remains open and under system control until you close the channel, or until an error occurs that causes the channel to release the file descriptor. After closing the file descriptor, the channel executes the specified `cleanupHandler` block on `queue`.

## See Also

### Creating a Dispatch I/O Object

- [init(type:fileDescriptor:queue:cleanupHandler:)](<init(type_filedescriptor_queue_cleanuphandler_).md>) — Creates a new I/O channel that accesses the specified file descriptor.
- [init(type:io:queue:cleanupHandler:)](<init(type_io_queue_cleanuphandler_).md>) — Creates a new I/O channel from an existing I/O channel.
- [StreamType](streamtype.md) — The semantics for accessing the contents of a file descriptor.
