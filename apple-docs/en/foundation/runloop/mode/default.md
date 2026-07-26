---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/mode/default
source_url: 'https://developer.apple.com/documentation/foundation/runloop/mode/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/mode/default.json'
content_hash: 'sha256:6df75e14c15af4c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [Mode](../mode.md)

# default

<sub>Type Property</sub>

The mode set to handle input sources other than connection objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: RunLoop.Mode
```

## Discussion

This is the most commonly used run-loop mode.

## See Also

### System Run Loop Modes

- [NSRunLoopCommonModes](common.md) — A pseudo-mode that includes one or more other run loop modes.
- [eventTracking](eventtracking.md) — The mode set when tracking events modally, such as a mouse-dragging loop.
- [modalPanel](modalpanel.md) — The mode set when waiting for input from a modal panel, such as a save or open panel.
- [tracking](tracking.md) — The mode set while tracking in controls takes place.
