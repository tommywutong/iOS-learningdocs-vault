---
title: dispatch_io_write
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_write
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_write'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_write.json'
content_hash: 'sha256:d5da7daa6900190e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_write

<sub>Function</sub>

Schedules an asynchronous write operation for the specified channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_io_write(dispatch_io_t channel, off_t offset, dispatch_data_t data, dispatch_queue_t queue, dispatch_io_handler_t io_handler);
```

## Parameters

- `channel` — The channel to use when writing the data.

- `offset` — For random-access channels, this parameter specifies the offset into the channel at which to write. The offset is specified relative to the initial file pointer of the channel’s file descriptor at the time the channel was created. For stream-based channels, this parameter is ignored and data is written to the current position.

- `data` — The data to write to the channel.

- `queue` — The dispatch queue on which to submit the `io_handler` block.

- `io_handler` — The block to use to report any progress. This block may be queued multiple times to process a given data request. Each time the block is queued, the `data` parameter passed to the handler contains the data that remains to be written. Your block need not be reentrant. The system guarantees that only one instance of this block is executed at any given time.

## Discussion

This function writes the specified data and submits the `io_handler` block to the `queue` to report on the progress of the operation. If the `done` parameter of the handler is set to [false](../swift/false.md), it means that only part of the data was written. If the `done` parameter is set to [true](../swift/true.md), it means the write operation is complete and the handler is not submitted again. If the operation was successful, the handler’s `error` parameter is set to `0`. However, if an unrecoverable error occurs on the channel’s file descriptor, the `done` parameter is set to [true](../swift/true.md) and an appropriate error value is reported in the handler’s `error` parameter.

## See Also

### Writing to the File

- [dispatch_write](dispatch_write.md) — Schedules an asynchronous write operation using the specified file descriptor.
