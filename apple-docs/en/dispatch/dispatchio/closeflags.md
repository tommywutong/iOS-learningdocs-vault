---
title: DispatchIO.CloseFlags
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchio/closeflags
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/closeflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/closeflags.json'
content_hash: 'sha256:d3dbc2b326c28be4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# DispatchIO.CloseFlags

<sub>Structure</sub>

Additional flags to use when closing an I/O channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CloseFlags
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Close Flags

- [stop](closeflags/stop.md) — Stop any in-progress read/write operations when closed.

### Initializing the Type

- [DISPATCH_IO_STOP](../dispatch_io_stop.md) — Stop any in-progress read and write operations when closed.

## See Also

### Closing the File

- [close(flags:)](<close(flags_).md>) — Closes the channel to new read and write operations.
