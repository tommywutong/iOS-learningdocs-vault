---
title: dispatch_io_create_with_io
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_create_with_io
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_create_with_io'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_create_with_io.json'
content_hash: 'sha256:57865bf98710d73c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_create_with_io

<sub>Function</sub>

Creates a new dispatch I/O channel from an existing channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_io_tdispatch_io_create_with_io(dispatch_io_type_t type, dispatch_io_t io, dispatch_queue_t queue, void (^cleanup_handler)(int error));
```

## Parameters

- `type` — The type of channel to create. For a list of possible options, see [dispatch_io_type_t](dispatch_io_type_t.md).

- `io` — An existing channel whose file descriptor or path name you want to use.

- `queue` — The dispatch queue to associate with the channel. This queue is used to execute the channel’s clean up handler. The channel retains this queue.

- `cleanup_handler` — The block to enqueue when the system relinquishes control of the channel’s file descriptor. This channel takes a single parameter that indicates the reason why control was relinquished. If the `error` parameter contains a non zero value, control was relinquished because there was an error creating the channel; otherwise, this value should be `0`.

## Return Value

The dispatch I/O channel or `NULL` if an error occurred. The returned object is retained before it is returned; it is your responsibility to close the channel and then release this object when you are done using it.

## Discussion

This function creates a new dispatch I/O channel that inherits the file descriptor or path name of the specified channel but whose channel type and policies you can set to be different.

If the existing channel is associated with a file descriptor, the system maintains control over the file descriptor until the new channel is also closed, an error occurs on the file descriptor, or all references to channels tied to that file descriptor are released. When the file descriptor is released, the `cleanup_handler` block is enqueued on the specified `queue` and the system relinquishes control over the file descriptor.

While it controls the file descriptor, the system may modify that file descriptor on behalf of the application. For example, the system typically adds the `O_NONBLOCK` flag to ensure that any operations on the file descriptor are non-blocking. During that time, it is an error for your application to modify the file descriptor directly. However, you may create additional channels using the same file descriptor.

## See Also

### Creating a Dispatch I/O Object

- [dispatch_io_create](dispatch_io_create.md) — Creates a dispatch I/O channel and associates it with the specified file descriptor.
- [dispatch_io_create_with_path](dispatch_io_create_with_path.md) — Creates a dispatch I/O channel with the associated path name.
- [dispatch_io_t](dispatch_io_t.md) — A dispatch I/O channel.
- [dispatch_fd_t](dispatch_fd_t.md) — A file descriptor used for I/O operations.
- [OS_dispatch_io](os_dispatch_io.md)
- [dispatch_io_type_t](dispatch_io_type_t.md) — The type of a dispatch I/O channel.
