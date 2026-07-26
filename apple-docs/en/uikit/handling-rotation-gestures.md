---
title: Handling rotation gestures
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-rotation-gestures
source_url: 'https://developer.apple.com/documentation/uikit/handling-rotation-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-rotation-gestures.json'
content_hash: 'sha256:1b111ec2059648f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Handling UIKit gestures](handling-uikit-gestures.md)

# Handling rotation gestures

<sub>Article</sub>

Measure the relative rotation of two fingers on the screen, and use that motion to rotate your content.

## Overview

A rotation gesture is a continuous gesture that occurs when the first two fingers that touch the screen rotate around each other. Use the [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) class to detect rotation gestures.

You can attach a gesture recognizer in one of these ways:

- Programmatically. Call the [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>) method of your view.
- In Interface Builder. Drag the appropriate object from the library and drop it onto your view.

![](../../../attachments/a6cbad77bad28b658f4185c680528d4e/handling-rotation-gestures-1@2x.png)

<sub>A diagram demonstrating how a rotation gesture begins when the first two fingers touch the screen and move to indicate a rotation.</sub>

Use a rotation gesture recognizer when you want to use rotational movements as input to your app. Rotational gestures are commonly used to manipulate objects onscreen. For example, you might use them to rotate a view or update the value of a custom control. Rotation gestures are continuous, so your action method is called whenever the rotation value changes, giving you a chance to update your content.

The gesture recognizer reports rotation values in radians. If you imagine a line between a person’s fingers, the line created by the fingers at their initial positions represents the initial point for measurements, and therefore represents a rotation angle of `0`. As a person’s fingers move, a new line is created between the fingers at each new location. The gesture recognizer measures the angle between the initial line and each new line and places the resulting value in its [rotation](uirotationgesturerecognizer/rotation.md) property.

A rotation gesture recognizer enters the [UIGestureRecognizerStateBegan](uigesturerecognizer/state-swift.enum/began.md) state as soon as the position of a person’s fingers changes in a way that indicates that rotation has begun. After that initial change, subsequent changes cause the gesture recognizer to enter the [UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md) state and update the angle of rotation. When a person’s fingers lift from the screen, the gesture recognizer enters the [UIGestureRecognizerStateEnded](uigesturerecognizer/state-swift.enum/ended.md) state.

> [!important] Important
> Take care when applying rotation values to your content, or you might get unexpected results. The rotation reported by the gesture recognizer represents the angle between the current finger position and the initial finger position. If you apply each new rotation value as is to your content, each new value compounds the previous one, causing your content to rotate too fast. Instead, cache the original value of your content, apply the rotation to the original value, and apply the new value back to your content. Alternatively, reset the [rotation](uirotationgesturerecognizer/rotation.md) factor to `0.0` after applying each new change.

The following code demonstrates how to rotate a view in a way that follows a person’s fingers. This action method applies the current rotation factor to the view’s transform and then resets the gesture recognizer’s [rotation](uirotationgesturerecognizer/rotation.md) property to `0.0`. Resetting the rotation factor causes the gesture recognizer to report only the amount of change since the value was reset, which results in the linear rotation of the view.

```swift
@IBAction func rotatePiece(_ gestureRecognizer : UIRotationGestureRecognizer) {
   // Move the anchor point of the view's layer to the center of a
   // person's two fingers. This creates a more natural looking rotation.
   guard gestureRecognizer.view != nil else { return }
        
   if gestureRecognizer.state == .began || gestureRecognizer.state == .changed {
      gestureRecognizer.view?.transform = gestureRecognizer.view!.transform.rotated(by: gestureRecognizer.rotation)
      gestureRecognizer.rotation = 0
   }
}
```

If the code for your rotation gesture recognizer isn’t called, or isn’t working correctly, check to see if the following conditions are true, and make corrections as needed:

- The [userInteractionEnabled](uiview/isuserinteractionenabled.md) property of the view is set to [true](../swift/true.md). Image views and labels set this property to [false](../swift/false.md) by default.
- At least two fingers are touching the screen.
- You’re applying rotation factors to your content correctly. Over-rotation happens when you apply the same rotation value more than once. To fix this problem, set the [rotation](uirotationgesturerecognizer/rotation.md) property to `0.0` after applying the current rotation value to your content.

## See Also

### Gestures

- [Handling tap gestures](handling-tap-gestures.md) — Use brief taps on the screen to implement button-like interactions with your content.
- [Handling long-press gestures](handling-long-press-gestures.md) — Detect extended duration taps on the screen, and use them to reveal contextually relevant content.
- [Handling pan gestures](handling-pan-gestures.md) — Trace the movement of fingers around the screen, and apply that movement to your content.
- [Handling swipe gestures](handling-swipe-gestures.md) — Detect a horizontal or vertical swipe motion on the screen, and use it to trigger navigation through your content.
- [Handling pinch gestures](handling-pinch-gestures.md) — Track the distance between two fingers and use that information to scale or zoom your content.
