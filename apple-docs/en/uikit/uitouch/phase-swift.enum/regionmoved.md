---
title: UITouch.Phase.regionMoved
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/phase-swift.enum/regionmoved
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/phase-swift.enum/regionmoved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/phase-swift.enum/regionmoved.json'
content_hash: 'sha256:678b0e92489aa3e1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITouch](../../uitouch.md) · [Phase](../phase-swift.enum.md)

# UITouch.Phase.regionMoved

<sub>Case</sub>

A touch for the given event is within a window on the screen, but has not yet pressed down.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case regionMoved
```

## Discussion

The [UITouchPhaseRegionEntered](regionentered.md), [UITouchPhaseRegionMoved](regionmoved.md), and [UITouchPhaseRegionExited](regionexited.md) phases don’t always align with the [state](../../uigesturerecognizer/state-swift.property.md) property of a [UIHoverGestureRecognizer](../../uihovergesturerecognizer.md). States of the hover gesture recognizer only apply within the context of the gesture’s view, whereas the touch states apply within the window.

## See Also

### Constants

- [UITouchPhaseBegan](began.md) — A touch for a given event has pressed down on the screen.
- [UITouchPhaseMoved](moved.md) — A touch for a given event has moved over the screen.
- [UITouchPhaseStationary](stationary.md) — A touch for a given event is pressed down on the screen, but hasn’t moved since the previous event.
- [UITouchPhaseEnded](ended.md) — A touch for a given event has lifted from the screen.
- [UITouchPhaseCancelled](cancelled.md) — The system canceled tracking for a touch, for example, when the user moves the device against their face.
- [UITouchPhaseRegionEntered](regionentered.md) — A touch for a given event has entered a window on the screen.
- [UITouchPhaseRegionExited](regionexited.md) — A touch for a given event has left a window on the screen.
