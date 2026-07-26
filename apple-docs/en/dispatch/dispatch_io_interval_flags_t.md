---
title: dispatch_io_interval_flags_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_interval_flags_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_interval_flags_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_interval_flags_t.json'
content_hash: 'sha256:606b7a1ab70499f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_interval_flags_t

<sub>Type Alias</sub>

The desired delivery behavior for interval events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef unsigned long dispatch_io_interval_flags_t;
```

## Topics

### Channel Configuration Options

- [DISPATCH_IO_STRICT_INTERVAL](dispatch_io_strict_interval.md) — Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

## See Also

### Managing the File Descriptor

- [dispatch_io_get_descriptor](dispatchio/filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_interval](dispatch_io_set_interval.md) — Sets the interval (in nanoseconds) at which to invoke the I/O handlers for the channel.
- [dispatch_io_set_low_water](<dispatchio/setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_high_water](<dispatchio/setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.
