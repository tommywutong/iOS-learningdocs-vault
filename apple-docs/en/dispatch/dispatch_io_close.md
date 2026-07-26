---
title: dispatch_io_close
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_close
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_close'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_close.json'
content_hash: 'sha256:5a24b499489721c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_close

<sub>Function</sub>

Closes the specified channel to new read and write operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_io_close(dispatch_io_t channel, dispatch_io_close_flags_t flags);
```

## Parameters

- `channel` — The channel to close.

- `flags` — The options to use when closing the channel. For a list of possible values, see [dispatch_io_close_flags_t](dispatch_io_close_flags_t.md).

## Discussion

After calling this function, you should not schedule any more read or write operations on the channel. Doing so causes an error to be sent to your handler.

If the [DISPATCH_IO_STOP](dispatch_io_stop.md) option is specified in the `flags` parameter, the system attempts to interrupt any outstanding read and write operations on the I/O channel. Even if you specify this flag, the corresponding handlers may be invoked with partial results. In addition, the final invocation of the handler is passed the `ECANCELED` error code to indicate that the operation was interrupted. If you do not specify the [DISPATCH_IO_STOP](dispatch_io_stop.md) flag, read and write operations on the channel run to completion as normal.

## See Also

### Closing the File

- [dispatch_io_close_flags_t](dispatch_io_close_flags_t.md) — Additional flags to use when closing an I/O channel.
