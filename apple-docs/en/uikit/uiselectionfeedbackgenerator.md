---
title: UISelectionFeedbackGenerator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiselectionfeedbackgenerator
source_url: 'https://developer.apple.com/documentation/uikit/uiselectionfeedbackgenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiselectionfeedbackgenerator.json'
content_hash: 'sha256:47690cdb0c6cdf8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISelectionFeedbackGenerator

<sub>Class</sub>

A concrete feedback generator subclass that creates haptics to indicate a change in selection.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UISelectionFeedbackGenerator
```

## Overview

Use selection feedback to communicate movement through a series of discrete values. For example, you might trigger selection feedback to indicate that a UI element’s values are changing.

The following code example shows how to play selection feedback in response to a long-press gesture.

```swift
var feedback = UISelectionFeedbackGenerator()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Create a selection feedback object and associate it with the view.
    feedback = UISelectionFeedbackGenerator(view: view)
    
    // Add a custom long-press gesture to the view.
    let longPressGesture = UILongPressGestureRecognizer(target: self, action: #selector(longPress(_:)))
    longPressGesture.numberOfTouchesRequired = 2
    view.addGestureRecognizer(longPressGesture)
}

@objc
private func longPress(_ sender: UILongPressGestureRecognizer) {
    if sender.state == .began {
        // Play selection feedback to indicate a selection change.
        feedback.selectionChanged(at: sender.location(in: view))
        
        // Update the UI in response to a selection change.
        // ...
    }
}
```

For more information, read [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md).

## Relationships

- **Inherits From**: [UIFeedbackGenerator](uifeedbackgenerator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIInteraction](uiinteraction.md)

## Topics

### Reporting selection changes

- [- selectionChanged](<uiselectionfeedbackgenerator/selectionchanged().md>) — Triggers selection feedback.
- [- selectionChangedAtLocation:](<uiselectionfeedbackgenerator/selectionchanged(at_).md>) — Triggers selection feedback at the specified location.

## See Also

### Haptic feedback

- [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md) — Provide tactile feedback when people perform certain actions in your app.
- [UIFeedbackGenerator](uifeedbackgenerator.md) — The abstract superclass for all feedback generators.
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.
