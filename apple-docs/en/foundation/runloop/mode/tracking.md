---
title: tracking
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/mode/tracking
source_url: 'https://developer.apple.com/documentation/foundation/runloop/mode/tracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/mode/tracking.json'
content_hash: 'sha256:4b0229af3c0da886'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [Mode](../mode.md)

# tracking

<sub>Type Property</sub>

The mode set while tracking in controls takes place.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let tracking: RunLoop.Mode
```

## Discussion

You can use this mode to add timers that fire during tracking.

## See Also

### System Run Loop Modes

- [NSRunLoopCommonModes](common.md) — A pseudo-mode that includes one or more other run loop modes.
- [NSDefaultRunLoopMode](default.md) — The mode set to handle input sources other than connection objects.
- [eventTracking](eventtracking.md) — The mode set when tracking events modally, such as a mouse-dragging loop.
- [modalPanel](modalpanel.md) — The mode set when waiting for input from a modal panel, such as a save or open panel.
