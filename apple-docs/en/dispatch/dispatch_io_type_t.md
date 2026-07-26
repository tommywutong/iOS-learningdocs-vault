---
title: dispatch_io_type_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_type_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_type_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_type_t.json'
content_hash: 'sha256:04866815ceca1fef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_type_t

<sub>Type Alias</sub>

The type of a dispatch I/O channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef unsigned long dispatch_io_type_t;
```

## Topics

### I/O Access Type

- [DISPATCH_IO_STREAM](dispatch_io_stream.md)
- [DISPATCH_IO_RANDOM](dispatch_io_random.md)

## See Also

### Creating a Dispatch I/O Object

- [dispatch_io_create](dispatch_io_create.md) — Creates a dispatch I/O channel and associates it with the specified file descriptor.
- [dispatch_io_create_with_io](dispatch_io_create_with_io.md) — Creates a new dispatch I/O channel from an existing channel.
- [dispatch_io_create_with_path](dispatch_io_create_with_path.md) — Creates a dispatch I/O channel with the associated path name.
- [dispatch_io_t](dispatch_io_t.md) — A dispatch I/O channel.
- [dispatch_fd_t](dispatch_fd_t.md) — A file descriptor used for I/O operations.
- [OS_dispatch_io](os_dispatch_io.md)
