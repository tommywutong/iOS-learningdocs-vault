---
title: UINotificationFeedbackGenerator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinotificationfeedbackgenerator
source_url: 'https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinotificationfeedbackgenerator.json'
content_hash: 'sha256:04ac59150034036b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINotificationFeedbackGenerator

<sub>Class</sub>

A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UINotificationFeedbackGenerator
```

## Overview

Use notification feedback to communicate that a task or action succeeded, failed, or produced a warning of some kind.

For more information, read [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md).

## Relationships

- **Inherits From**: [UIFeedbackGenerator](uifeedbackgenerator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIInteraction](uiinteraction.md)

## Topics

### Producing notification feedback

- [- notificationOccurred:](<uinotificationfeedbackgenerator/notificationoccurred(__).md>) — Triggers notification feedback.
- [- notificationOccurred:atLocation:](<uinotificationfeedbackgenerator/notificationoccurred(__at_).md>) — Triggers notification feedback at the specified location.
- [FeedbackType](uinotificationfeedbackgenerator/feedbacktype.md) — The type of notification that a notification feedback generator object generates.

## See Also

### Haptic feedback

- [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md) — Provide tactile feedback when people perform certain actions in your app.
- [UIFeedbackGenerator](uifeedbackgenerator.md) — The abstract superclass for all feedback generators.
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.
