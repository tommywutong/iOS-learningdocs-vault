---
title: allowsSimultaneousRecognitionDuringLift
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/allowssimultaneousrecognitionduringlift
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/allowssimultaneousrecognitionduringlift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/allowssimultaneousrecognitionduringlift.json'
content_hash: 'sha256:7d8433bd607afef7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteraction](../uidraginteraction.md)

# allowsSimultaneousRecognitionDuringLift

<sub>Instance Property</sub>

A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsSimultaneousRecognitionDuringLift: Bool { get set }
```

## Discussion

If you set the [allowsSimultaneousRecognitionDuringLift](allowssimultaneousrecognitionduringlift.md) property to [true](../../swift/true.md), the interaction is canceled when another gesture is recognized. If you set this property to [false](../../swift/false.md) (the default value), competing gesture recognizers fail.

> [!note] Note
> [UILongPressGestureRecognizer](../uilongpressgesturerecognizer.md) instances are always delayed and happen simultaneously during the lift activity.

## See Also

### Managing drag interactions

- [delegate](delegate.md) — An object that configures and controls a drag interaction.
- [UIDragInteractionDelegate](../uidraginteractiondelegate.md) — The interface for configuring and controlling a drag interaction.
