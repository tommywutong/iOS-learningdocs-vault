---
title: CFMachPortCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmachportcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportcallback.json'
content_hash: 'sha256:51134ed29116e178'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortCallBack

<sub>Type Alias</sub>

Callback invoked to process a message received on a CFMachPort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFMachPortCallBack = (CFMachPort?, UnsafeMutableRawPointer?, CFIndex, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `port` — The CFMachPort object on which the message `msg` was received.

- `msg` — The Mach message received on `port`. The pointer is to a `mach_msg_header_t` structure.

- `size` — Size of the Mach message `msg`, excluding the message trailer.

- `info` — The `info` member of the [CFMachPortContext](cfmachportcontext.md) structure used when creating `port`.

## Discussion

You specify this callback when creating a CFMachPort object with either [CFMachPortCreate](<cfmachportcreate(________).md>) or [CFMachPortCreateWithPort](<cfmachportcreatewithport(__________).md>). To receive messages on a CFMachPort object (and have this callback invoked), you must create a run loop source for the port and add it to a run loop.

## See Also

### Callbacks

- [CFMachPortInvalidationCallBack](cfmachportinvalidationcallback.md) — Callback invoked when a CFMachPort object is invalidated.
