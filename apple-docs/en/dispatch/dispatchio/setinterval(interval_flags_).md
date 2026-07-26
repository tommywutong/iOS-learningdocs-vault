---
title: 'setInterval(interval:flags:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/setinterval(interval:flags:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/setinterval(interval:flags:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/setinterval%28interval%3Aflags%3A%29.json'
content_hash: 'sha256:dde237ba0e492242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# setInterval(interval:flags:)

<sub>Instance Method</sub>

Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags = [])
```

## Parameters

- `interval` — The number of nanoseconds that must elapse before the scheduling of any I/O handlers is desired.

- `flags` — Flags indicating the desired delivery behavior at the interval time. For a list of flags, see [IntervalFlags](intervalflags.md).

## Discussion

A channel interval is a way for you to receive periodic progress reports on the state of a read or write operation. You can use this feedback to update progress bars or other parts of your application.

If you set an interval on a channel, the handlers for any read or write operations are enqueued at the given interval only if the amount of data that has been processed exceeds the current low-water mark for the channel. Passing the [strictInterval](intervalflags/strictinterval.md) constant in the `flags` parameter forces the enqueueing of the handlers even if the low-water mark is not exceeded.

The system may add a small amount of leeway to the specified interval in order to align the delivery of handlers with other system activity. The purpose of this behavior is to improve overall performance or power consumption for the system.

## See Also

### Managing the File Descriptor

- [dispatch_io_get_descriptor](filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_high_water](<setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_low_water](<setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [IntervalFlags](intervalflags.md) — The desired delivery behavior for interval events.
