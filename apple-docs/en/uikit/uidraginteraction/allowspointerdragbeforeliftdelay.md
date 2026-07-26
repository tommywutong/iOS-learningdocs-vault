---
title: allowsPointerDragBeforeLiftDelay
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/allowspointerdragbeforeliftdelay
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/allowspointerdragbeforeliftdelay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/allowspointerdragbeforeliftdelay.json'
content_hash: 'sha256:0a6a43c73b15290c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteraction](../uidraginteraction.md)

# allowsPointerDragBeforeLiftDelay

<sub>Instance Property</sub>

A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsPointerDragBeforeLiftDelay: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md), a pointer-initiated drag begins as soon as the pointer crosses the minimum movement threshold, regardless of whether the lift delay has elapsed.

When this property is [false](../../swift/false.md), a pointer-initiated drag waits for the lift delay to elapse before checking whether the pointer has crossed the minimum movement threshold. This matches touch-based drag initiation behavior.

Set this property to [false](../../swift/false.md) in gesture-rich views (such as a canvas) where people also interact frequently with secondary gestures in the same view. This ensures consistent gesture disambiguation regardless of input device.

The default value is [true](../../swift/true.md) in iOS and [false](../../swift/false.md) in macOS.

For touch-based gesture timing, use [liftBehavior](liftbehavior-swift.property.md).

## See Also

### Configuring lift behavior

- [liftBehavior](liftbehavior-swift.property.md) — A value that controls the timing behavior for initiating a drag gesture from a touch. _(beta)_
- [LiftBehavior](liftbehavior-swift.enum.md) — Constants that determine the lift behavior for a drag interaction. _(beta)_
