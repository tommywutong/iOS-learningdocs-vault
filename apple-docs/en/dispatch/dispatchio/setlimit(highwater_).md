---
title: 'setLimit(highWater:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/setlimit(highwater:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/setlimit(highwater:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/setlimit%28highwater%3A%29.json'
content_hash: 'sha256:3adc3d31244c0eb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# setLimit(highWater:)

<sub>Instance Method</sub>

Sets the maximum number of bytes to process before enqueueing a handler block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setLimit(highWater high_water: Int)
```

## Parameters

- `high_water` — The maximum number of bytes to read or write before enqueueing the corresponding I/O handler block.

## Discussion

During a read or write operation, the channel uses the high- and low-water mark values to determine how often to enqueue the associated handler block. It enqueues the block when the number of bytes read or written is between these two values.

The default high-water mark for channels is set to `SIZE_MAX`.

## See Also

### Managing the File Descriptor

- [dispatch_io_get_descriptor](filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_low_water](<setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [setInterval(interval:flags:)](<setinterval(interval_flags_).md>) — Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [IntervalFlags](intervalflags.md) — The desired delivery behavior for interval events.
