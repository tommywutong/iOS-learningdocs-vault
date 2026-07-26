---
title: UIImpactFeedbackGenerator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimpactfeedbackgenerator
source_url: 'https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimpactfeedbackgenerator.json'
content_hash: 'sha256:824e857fff63564d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIImpactFeedbackGenerator

<sub>Class</sub>

A concrete feedback generator subclass that creates haptics to simulate physical impacts.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIImpactFeedbackGenerator
```

## Overview

Use impact feedback to indicate when an impact occurs. For example, you might trigger impact feedback when a user interface object collides with another object.

The following code example shows how to use a pan gesture to drag a square, playing haptic feedback to indicate when the square collides with the edge of its superview.

```swift
var feedback = UIImpactFeedbackGenerator()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Create an impact feedback object and associate it with the view.
    feedback = UIImpactFeedbackGenerator(view: view)
    
    // Draw a basic square and add it to the view hierarchy.
    let center = CGPoint(x: view.center.x - 50, y: view.center.y - 50)
    let square = UIView(frame: CGRect(origin: center,
                                     size: CGSize(width: 100, height: 100)))
    square.backgroundColor = .tintColor
    view.addSubview(square)
    
    // Add a pan gesture to allow dragging the square.
    let panGesture = UIPanGestureRecognizer(target: self, action: #selector(dragSquare(_:)))
    square.isUserInteractionEnabled = true
    square.addGestureRecognizer(panGesture)
}

@objc
private func dragSquare(_ sender: UIPanGestureRecognizer) {
    guard let square = sender.view else { return }
    
    if sender.state == .began {
        // Prepare the feedback object.
        feedback.prepare()
    }

    // Move the square in response to a pan gesture.
    let distance = sender.translation(in: view)
    square.center = CGPoint(x: square.center.x + distance.x, y: square.center.y + distance.y)
    sender.setTranslation(CGPoint.zero, in: view)

    // Play impact feedback if the square bumps into the edge of its superview.
    if square.hitEdge(of: view) {
        feedback.impactOccurred(intensity: 1, at: sender.location(in: view))
    }
}
```

For more information, read [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md).

## Relationships

- **Inherits From**: [UIFeedbackGenerator](uifeedbackgenerator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIInteraction](uiinteraction.md)

## Topics

### Initializing the feedback generator

- [+ feedbackGeneratorWithStyle:forView:](<uiimpactfeedbackgenerator/init(style_view_).md>) — Creates an impact feedback generator with the specified style and view.
- [FeedbackStyle](uiimpactfeedbackgenerator/feedbackstyle.md) — The mass of the objects in the collision simulated by an impact feedback generator object.

### Reporting impacts

- [- impactOccurred](<uiimpactfeedbackgenerator/impactoccurred().md>) — Triggers impact feedback.
- [- impactOccurredWithIntensity:](<uiimpactfeedbackgenerator/impactoccurred(intensity_).md>) — Triggers impact feedback with a specific intensity.
- [- impactOccurredAtLocation:](<uiimpactfeedbackgenerator/impactoccurred(at_).md>) — Triggers impact feedback at the specified location.
- [- impactOccurredWithIntensity:atLocation:](<uiimpactfeedbackgenerator/impactoccurred(intensity_at_).md>) — Triggers impact feedback with a specific intensity at the specified location.

### Deprecated

- [- initWithStyle:](<uiimpactfeedbackgenerator/init(style_).md>) — Creates an impact feedback generator with the specified style. _(deprecated)_

## See Also

### Haptic feedback

- [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md) — Provide tactile feedback when people perform certain actions in your app.
- [UIFeedbackGenerator](uifeedbackgenerator.md) — The abstract superclass for all feedback generators.
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.
