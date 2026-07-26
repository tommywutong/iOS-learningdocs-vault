---
title: UIScreenEdgePanGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreenedgepangesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenedgepangesturerecognizer.json'
content_hash: 'sha256:1a96669d273b4e91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScreenEdgePanGestureRecognizer

<sub>Class</sub>

A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIScreenEdgePanGestureRecognizer
```

## Overview

The system uses screen edge gestures in some cases to initiate view controller transitions. You can use this class to replicate the same gesture behavior for your own actions.

After creating a screen edge pan gesture recognizer, assign an appropriate value to the [edges](uiscreenedgepangesturerecognizer/edges.md) property before attaching the gesture recognizer to your view. You use this property to specify the edges where the gesture can start. This gesture recognizer ignores any touches beyond the first touch.

## Relationships

- **Inherits From**: [UIPanGestureRecognizer](uipangesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying the starting edges

- [edges](uiscreenedgepangesturerecognizer/edges.md) — The acceptable starting edges for the gesture.
- [UIRectEdge](uirectedge.md) — Constants that specify the edges of a rectangle.

## See Also

### Standard gestures

- [Handling UIKit gestures](handling-uikit-gestures.md) — Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md) — Discover how to use multiple gesture recognizers on the same view.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md) — Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — A continuous gesture recognizer that interprets pointer movement over a view.
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — A continuous gesture recognizer that interprets long-press gestures.
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — A continuous gesture recognizer that interprets panning gestures.
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — A continuous gesture recognizer that interprets pinching gestures involving two touches.
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — A discrete gesture recognizer that interprets single or multiple taps.
