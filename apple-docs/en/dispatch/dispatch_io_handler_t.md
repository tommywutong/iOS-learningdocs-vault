---
title: dispatch_io_handler_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_handler_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_handler_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_handler_t.json'
content_hash: 'sha256:40aca5cc52452194'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_handler_t

<sub>Type Alias</sub>

A handler block used to process operations on a dispatch I/O channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(_Bool, NSObject<OS_dispatch_data> *, int) dispatch_io_handler_t;
```

## Discussion

The parameters of a dispatch I/O handler are as follows:

- `done` - A flag indicating whether the operation is complete.
- `data` - The data object to be handled. This object is retained by the system for the duration of the handler’s execution and is released when the handler block returns.
- `error` - The error number (if any) reported for the operation. An error number of `0` typically indicates the operation was successful.

## See Also

### Reading from the File

- [dispatch_read](dispatch_read.md) — Schedules an asynchronous read operation using the specified file descriptor.
- [dispatch_io_read](dispatch_io_read.md) — Schedules an asynchronous read operation on the specified channel.
