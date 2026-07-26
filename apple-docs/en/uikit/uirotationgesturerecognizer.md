---
title: UIRotationGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uirotationgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirotationgesturerecognizer.json'
content_hash: 'sha256:578882795ba129d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRotationGestureRecognizer

<sub>Class</sub>

A continuous gesture recognizer that interprets rotation gestures involving two touches.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIRotationGestureRecognizer
```

## Overview

[UIRotationGestureRecognizer](uirotationgesturerecognizer.md) is a concrete subclass of [UIGestureRecognizer](uigesturerecognizer.md).

The user must press two fingers on a view while rotating it. When the user moves the fingers opposite each other in a circular motion, the underlying view rotates in a corresponding direction and speed.

Rotation is a continuous gesture. It begins when the user moves the two fingers enough to create a rotation gesture. The gesture changes when a finger moves while both fingers remain touching. It ends when the user lifts both fingers. At each stage in the gesture, the gesture recognizer sends its action message.

## Relationships

- **Inherits From**: [UIGestureRecognizer](uigesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Interpreting the gesture

- [rotation](uirotationgesturerecognizer/rotation.md) — The rotation of the gesture in radians.
- [velocity](uirotationgesturerecognizer/velocity.md) — The velocity of the rotation gesture in radians per second.

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
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — A discrete gesture recognizer that interprets single or multiple taps.
