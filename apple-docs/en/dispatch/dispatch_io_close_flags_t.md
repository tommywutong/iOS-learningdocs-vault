---
title: dispatch_io_close_flags_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_close_flags_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_close_flags_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_close_flags_t.json'
content_hash: 'sha256:67ed11253d1dfef4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_close_flags_t

<sub>Type Alias</sub>

Additional flags to use when closing an I/O channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef unsigned long dispatch_io_close_flags_t;
```

## Topics

### Channel Closing Options

- [DISPATCH_IO_STOP](dispatch_io_stop.md) — Stop any in-progress read and write operations when closed.

## See Also

### Closing the File

- [dispatch_io_close](dispatch_io_close.md) — Closes the specified channel to new read and write operations.
