---
title: UICanvasFeedbackGenerator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicanvasfeedbackgenerator
source_url: 'https://developer.apple.com/documentation/uikit/uicanvasfeedbackgenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicanvasfeedbackgenerator.json'
content_hash: 'sha256:5e4d2a61ff6d6fed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICanvasFeedbackGenerator

<sub>Class</sub>

A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UICanvasFeedbackGenerator
```

## Overview

Use canvas feedback to indicate when a drawing event occurs, such as an object snapping to a guide or ruler. When using Apple Pencil Pro with a compatible iPad, this type of feedback can provide a tactile response.

The following code example shows how to use a pan gesture to drag a square, playing haptic feedback to indicate when the square aligns with a gridline on the canvas.

```swift
var gridlines: [Gridline] = []
var feedback = UICanvasFeedbackGenerator()

override func viewDidLoad() {
    super.viewDidLoad()
    configureGridlines()
    
    // Create a canvas feedback object and associate it with the view.
    feedback = UICanvasFeedbackGenerator(view: view)
    
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
    
    // Play canvas feedback if the square aligns with one of the gridlines.
    if square.aligned(gridlines: gridlines) {
        feedback.alignmentOccurred(at: sender.location(in: view))
    }
}
```

For more information, read [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md).

## Relationships

- **Inherits From**: [UIFeedbackGenerator](uifeedbackgenerator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIInteraction](uiinteraction.md)

## Topics

### Reporting canvas events

- [- alignmentOccurredAtLocation:](<uicanvasfeedbackgenerator/alignmentoccurred(at_).md>) — Triggers feedback to indicate when an alignment occurs, such as snapping an object to a guide or ruler.
- [- pathCompletedAtLocation:](<uicanvasfeedbackgenerator/pathcompleted(at_).md>) — Triggers feedback to indicate path completion or shape recognition.

## See Also

### Haptic feedback

- [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md) — Provide tactile feedback when people perform certain actions in your app.
- [UIFeedbackGenerator](uifeedbackgenerator.md) — The abstract superclass for all feedback generators.
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate a change in selection.
