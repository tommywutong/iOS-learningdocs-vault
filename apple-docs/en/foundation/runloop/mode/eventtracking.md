---
title: eventTracking
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/mode/eventtracking
source_url: 'https://developer.apple.com/documentation/foundation/runloop/mode/eventtracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/mode/eventtracking.json'
content_hash: 'sha256:45b1d55886940ee6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [Mode](../mode.md)

# eventTracking

<sub>Type Property</sub>

The mode set when tracking events modally, such as a mouse-dragging loop.

<sub>macOS</sub>

```swift
static let eventTracking: RunLoop.Mode
```

## See Also

### System Run Loop Modes

- [NSRunLoopCommonModes](common.md) — A pseudo-mode that includes one or more other run loop modes.
- [NSDefaultRunLoopMode](default.md) — The mode set to handle input sources other than connection objects.
- [modalPanel](modalpanel.md) — The mode set when waiting for input from a modal panel, such as a save or open panel.
- [tracking](tracking.md) — The mode set while tracking in controls takes place.
