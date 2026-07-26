---
title: 'close(flags:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/close(flags:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/close(flags:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/close%28flags%3A%29.json'
content_hash: 'sha256:3b4208b8aec7f8b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# close(flags:)

<sub>Instance Method</sub>

Closes the channel to new read and write operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func close(flags: DispatchIO.CloseFlags = [])
```

## Parameters

- `flags` — The options to use when closing the channel. For a list of possible values, see [CloseFlags](closeflags.md).

## Discussion

After calling this method, do not schedule any more read or write operations on the channel. Doing so causes an error to be sent to your handler.

If the [stop](closeflags/stop.md) option is specified in the flags parameter, the system attempts to interrupt any outstanding read and write operations on the I/O channel. If you specify this flag, the corresponding handlers may be invoked with partial results. In addition, the final invocation of the handler is passed the `POSIXErrorCode.ECANCELED` error code to indicate that the operation was interrupted. If you do not specify the [stop](closeflags/stop.md) flag, read and write operations on the channel run to completion as normal.

## See Also

### Closing the File

- [CloseFlags](closeflags.md) — Additional flags to use when closing an I/O channel.
