---
title: UILongPressGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilongpressgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilongpressgesturerecognizer.json'
content_hash: 'sha256:33f8f3030f747e08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILongPressGestureRecognizer

<sub>Class</sub>

A continuous gesture recognizer that interprets long-press gestures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UILongPressGestureRecognizer
```

## Overview

[UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) is a concrete subclass of [UIGestureRecognizer](uigesturerecognizer.md).

The user must press one or more fingers on a view and hold them there for a minimum period of time before the action triggers. While down, the userʼs fingers canʼt move more than a specified distance or the gesture fails.

A long-press gesture is continuous. The gesture begins ([UIGestureRecognizerStateBegan](uigesturerecognizer/state-swift.enum/began.md)) when the user presses the number of allowable fingers ([numberOfTouchesRequired](uilongpressgesturerecognizer/numberoftouchesrequired.md)) for the specified period ([minimumPressDuration](uilongpressgesturerecognizer/minimumpressduration.md)) and the touches don’t move beyond the allowable range of movement ([allowableMovement](uilongpressgesturerecognizer/allowablemovement.md)). The gesture recognizer transitions to the Change state whenever a finger moves, and it ends ([UIGestureRecognizerStateEnded](uigesturerecognizer/state-swift.enum/ended.md)) when the user lifts any of the fingers.

## Relationships

- **Inherits From**: [UIGestureRecognizer](uigesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the gesture recognizer

- [minimumPressDuration](uilongpressgesturerecognizer/minimumpressduration.md) — The minimum time that the user must press on the view for the gesture to be recognized.
- [numberOfTouchesRequired](uilongpressgesturerecognizer/numberoftouchesrequired.md) — The number of fingers that must touch the view for gesture recognition.
- [numberOfTapsRequired](uilongpressgesturerecognizer/numberoftapsrequired.md) — The number of taps on the view necessary for gesture recognition.
- [allowableMovement](uilongpressgesturerecognizer/allowablemovement.md) — The maximum movement of the fingers on the view before the gesture fails.

## See Also

### Standard gestures

- [Handling UIKit gestures](handling-uikit-gestures.md) — Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md) — Discover how to use multiple gesture recognizers on the same view.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md) — Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — A continuous gesture recognizer that interprets pointer movement over a view.
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — A continuous gesture recognizer that interprets panning gestures.
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — A continuous gesture recognizer that interprets pinching gestures involving two touches.
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — A discrete gesture recognizer that interprets single or multiple taps.
