---
title: dispatch_io_set_interval
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_set_interval
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_set_interval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_set_interval.json'
content_hash: 'sha256:ba863e9554570604'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_set_interval

<sub>Function</sub>

Sets the interval (in nanoseconds) at which to invoke the I/O handlers for the channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_io_set_interval(dispatch_io_t channel, uint64_t interval, dispatch_io_interval_flags_t flags);
```

## Parameters

- `channel` — The channel whose interval you want to configure.

- `interval` — The number of nanoseconds that must elapse before the scheduling of any I/O handlers is desired.

- `flags` — Flags indicating the desired delivery behavior at the interval time. For a list of flags, see [dispatch_io_interval_flags_t](dispatch_io_interval_flags_t.md).

## Discussion

A channel interval is a way for you to receive periodic progress reports on the state of a read or write operation. You can use this feedback to update progress bars or other parts of your application.

If you set an interval on a channel, the handlers for any read or write operations are enqueued at the given interval only if the amount of data that has been processed exceeds the current low-water mark for the channel. Passing the [DISPATCH_IO_STRICT_INTERVAL](dispatch_io_strict_interval.md) constant in the `flags` parameter forces the enqueueing of the handlers even if the low-water mark is not exceeded.

The system may add a small amount of leeway to the specified interval in order to align the delivery of handlers with other system activity. The purpose of this behavior is to improve overall performance or power consumption for the system.

## See Also

### Managing the File Descriptor

- [dispatch_io_get_descriptor](dispatchio/filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_interval_flags_t](dispatch_io_interval_flags_t.md) — The desired delivery behavior for interval events.
- [dispatch_io_set_low_water](<dispatchio/setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_high_water](<dispatchio/setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.
