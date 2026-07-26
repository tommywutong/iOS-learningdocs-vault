---
title: fileDescriptor
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchio/filedescriptor
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/filedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/filedescriptor.json'
content_hash: 'sha256:f4344f01f4d43739'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# fileDescriptor

<sub>Instance Property</sub>

Returns the file descriptor associated with the specified channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileDescriptor: Int32 { get }
```

## Discussion

If the path name associated with the channel has not yet been opened, calling this function does not normally open the corresponding file, with one exception. If you call the function from a barrier block scheduled on the channel, the function does open the file and return the resulting file descriptor.

## See Also

### Managing the File Descriptor

- [dispatch_io_set_high_water](<setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_low_water](<setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [setInterval(interval:flags:)](<setinterval(interval_flags_).md>) — Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [IntervalFlags](intervalflags.md) — The desired delivery behavior for interval events.
