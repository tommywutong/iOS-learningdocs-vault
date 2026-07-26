---
title: common
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/mode/common
source_url: 'https://developer.apple.com/documentation/foundation/runloop/mode/common'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/mode/common.json'
content_hash: 'sha256:7d9e820a0ef3b15e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [Mode](../mode.md)

# common

<sub>Type Property</sub>

A pseudo-mode that includes one or more other run loop modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let common: RunLoop.Mode
```

## Discussion

When you add an object to a run loop using this mode, the runloop monitors the object when running in any of the common modes. For details about adding a runloop mode to the set of common modes, see [CFRunLoopAddCommonMode(_:_:)](<../../../corefoundation/cfrunloopaddcommonmode(____).md>).

## See Also

### System Run Loop Modes

- [NSDefaultRunLoopMode](default.md) — The mode set to handle input sources other than connection objects.
- [eventTracking](eventtracking.md) — The mode set when tracking events modally, such as a mouse-dragging loop.
- [modalPanel](modalpanel.md) — The mode set when waiting for input from a modal panel, such as a save or open panel.
- [tracking](tracking.md) — The mode set while tracking in controls takes place.
