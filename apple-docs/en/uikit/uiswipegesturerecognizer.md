---
title: UISwipeGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswipegesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswipegesturerecognizer.json'
content_hash: 'sha256:855ec07050c3dd24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISwipeGestureRecognizer

<sub>Class</sub>

A discrete gesture recognizer that interprets swiping gestures in one or more directions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISwipeGestureRecognizer
```

## Overview

[UISwipeGestureRecognizer](uiswipegesturerecognizer.md) is a concrete subclass of [UIGestureRecognizer](uigesturerecognizer.md).` `

[UISwipeGestureRecognizer](uiswipegesturerecognizer.md) recognizes a swipe when the user moves the specified number of touches ([numberOfTouchesRequired](uiswipegesturerecognizer/numberoftouchesrequired.md)) in an allowable direction ([direction](uiswipegesturerecognizer/direction-swift.property.md)) far enough to create a swipe. Swipes can be slow or fast. A slow swipe requires high directional precision but a small distance; a fast swipe requires low directional precision but a large distance. Because a swipe is a discrete gesture, the system sends the associated action message just once per gesture.

You can determine the location where a swipe begins by calling the [UIGestureRecognizer](uigesturerecognizer.md) methods [- locationInView:](<uigesturerecognizer/location(in_).md>) and [- locationOfTouch:inView:](<uigesturerecognizer/location(oftouch_in_).md>). The former method provides the centroid if the gesture contains more than one touch; the latter provides the location of a particular touch.

## Relationships

- **Inherits From**: [UIGestureRecognizer](uigesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the gesture

- [direction](uiswipegesturerecognizer/direction-swift.property.md) — The permitted direction of the swipe for this gesture recognizer.
- [numberOfTouchesRequired](uiswipegesturerecognizer/numberoftouchesrequired.md) — The number of touches necessary for swipe recognition.
- [Direction](uiswipegesturerecognizer/direction-swift.struct.md) — The direction of the swipe.

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
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — A discrete gesture recognizer that interprets single or multiple taps.
