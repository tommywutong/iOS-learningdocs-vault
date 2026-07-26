---
title: UIPanGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipangesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uipangesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipangesturerecognizer.json'
content_hash: 'sha256:1626a6af62dbf811'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPanGestureRecognizer

<sub>Class</sub>

A continuous gesture recognizer that interprets panning gestures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIPanGestureRecognizer
```

## Overview

[UIPanGestureRecognizer](uipangesturerecognizer.md) is a concrete subclass of [UIGestureRecognizer](uigesturerecognizer.md).

Clients of this class can, in their action methods, query the [UIPanGestureRecognizer](uipangesturerecognizer.md) object for the current translation of the gesture ([- translationInView:](<uipangesturerecognizer/translation(in_).md>)) and the velocity of the translation ([- velocityInView:](<uipangesturerecognizer/velocity(in_).md>)). They can specify a view’s coordinate system to use for the translation and velocity values. Clients can also reset the translation to a desired value.

A panning gesture is continuous. The user must press one or more fingers on a view while panning it. The gesture begins ([UIGestureRecognizerStateBegan](uigesturerecognizer/state-swift.enum/began.md)) when the user moves the minimum number of fingers allowed ([minimumNumberOfTouches](uipangesturerecognizer/minimumnumberoftouches.md)) enough distance for recognition as a pan. It changes ([UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md)) when the user moves a finger while pressing with the minimum number of fingers. It ends ([UIGestureRecognizerStateEnded](uigesturerecognizer/state-swift.enum/ended.md)) when the user lifts all fingers.

## Relationships

- **Inherits From**: [UIGestureRecognizer](uigesturerecognizer.md)

- **Inherited By**: [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the gesture recognizer

- [maximumNumberOfTouches](uipangesturerecognizer/maximumnumberoftouches.md) — The maximum number of fingers that can touch the view for gesture recognition.
- [minimumNumberOfTouches](uipangesturerecognizer/minimumnumberoftouches.md) — The minimum number of fingers that can touch the view for gesture recognition.

### Tracking the location and velocity of the gesture

- [- translationInView:](<uipangesturerecognizer/translation(in_).md>) — Interprets the pan gesture in the coordinate system of the specified view.
- [- setTranslation:inView:](<uipangesturerecognizer/settranslation(__in_).md>) — Sets the translation value in the coordinate system of the specified view.
- [- velocityInView:](<uipangesturerecognizer/velocity(in_).md>) — Interprets the velocity of the pan gesture in the coordinate system of the specified view.

### Tracking scroll events

- [allowedScrollTypesMask](uipangesturerecognizer/allowedscrolltypesmask.md) — A scroll type mask that enables recognition of scroll events.
- [UIScrollTypeMask](uiscrolltypemask.md) — A bit mask identifying the scroll type of a pan gesture.
- [UIScrollType](uiscrolltype.md) — Constants that define the type of the scroll.

## See Also

### Standard gestures

- [Handling UIKit gestures](handling-uikit-gestures.md) — Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md) — Discover how to use multiple gesture recognizers on the same view.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md) — Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — A continuous gesture recognizer that interprets pointer movement over a view.
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — A continuous gesture recognizer that interprets long-press gestures.
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — A continuous gesture recognizer that interprets pinching gestures involving two touches.
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — A discrete gesture recognizer that interprets single or multiple taps.
