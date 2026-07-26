---
title: UITapGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitapgesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uitapgesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitapgesturerecognizer.json'
content_hash: 'sha256:df6c929d3915818f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITapGestureRecognizer

<sub>Class</sub>

A discrete gesture recognizer that interprets single or multiple taps.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITapGestureRecognizer
```

## Overview

[UITapGestureRecognizer](uitapgesturerecognizer.md) is a concrete subclass of [UIGestureRecognizer](uigesturerecognizer.md).

For gesture recognition, the specified number of fingers must tap the view a specified number of times. Although taps are discrete gestures, they’re discrete for each state of the gesture recognizer. The system sends the associated action message when the gesture begins and then again for each intermediate state until (and including) the ending state of the gesture. Code that handles tap gestures should test for the state of the gesture, for example:

**Swift**

```swift
func handleTap(sender: UITapGestureRecognizer) {
    if sender.state == .ended {
        // handling code
    }
}
```

**Objective-C**

```objc
- (void)handleTap:(UITapGestureRecognizer *)sender
{
    if (sender.state == UIGestureRecognizerStateEnded)
    {
        // handling code
    }
}
```

Action methods handling this gesture can get the location of the gesture as a whole by calling the [UIGestureRecognizer](uigesturerecognizer.md) method [- locationInView:](<uigesturerecognizer/location(in_).md>). If there are multiple taps, this location is the first tap. If there are multiple touches, this location is the centroid of all fingers tapping the view. Clients can get the location of particular touches in the tap by calling [- locationOfTouch:inView:](<uigesturerecognizer/location(oftouch_in_).md>). If multiple taps are allowed, this location is the first tap.

## Relationships

- **Inherits From**: [UIGestureRecognizer](uigesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the gesture

- [buttonMaskRequired](uitapgesturerecognizer/buttonmaskrequired.md) — The bit mask of the buttons the user must press for gesture recognition.
- [numberOfTapsRequired](uitapgesturerecognizer/numberoftapsrequired.md) — The number of taps necessary for gesture recognition.
- [numberOfTouchesRequired](uitapgesturerecognizer/numberoftouchesrequired.md) — The number of fingers that the user must tap for gesture recognition.

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
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — A discrete gesture recognizer that interprets swiping gestures in one or more directions.
