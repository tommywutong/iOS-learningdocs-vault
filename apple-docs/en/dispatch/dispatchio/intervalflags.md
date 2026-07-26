---
title: DispatchIO.IntervalFlags
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchio/intervalflags
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/intervalflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/intervalflags.json'
content_hash: 'sha256:a502fe01cd101f57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# DispatchIO.IntervalFlags

<sub>Structure</sub>

The desired delivery behavior for interval events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IntervalFlags
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Interval Flags

- [strictInterval](intervalflags/strictinterval.md) — Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.
- [DISPATCH_IO_STRICT_INTERVAL](../dispatch_io_strict_interval.md) — Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

### Initializing the Type

- [init(nilLiteral:)](<intervalflags/init(nilliteral_).md>)

## See Also

### Managing the File Descriptor

- [dispatch_io_get_descriptor](filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_high_water](<setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_low_water](<setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [setInterval(interval:flags:)](<setinterval(interval_flags_).md>) — Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
