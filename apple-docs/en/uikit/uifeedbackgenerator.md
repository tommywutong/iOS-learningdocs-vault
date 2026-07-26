---
title: UIFeedbackGenerator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifeedbackgenerator
source_url: 'https://developer.apple.com/documentation/uikit/uifeedbackgenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifeedbackgenerator.json'
content_hash: 'sha256:54305445a153e846'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFeedbackGenerator

<sub>Class</sub>

The abstract superclass for all feedback generators.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIFeedbackGenerator
```

## Overview

Don’t subclass or create instances of this class yourself. Instead, instantiate one of the concrete feedback generator subclasses:

- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md). Use impact feedback to indicate when an impact occurs. For example, you might trigger impact feedback when a user interface object collides with something or snaps into place.
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md). Use selection feedback to indicate a change in selection.
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md). Use notification feedback to indicate successes, failures, and warnings.
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md). Use canvas feedback to indicate when a drawing event occurs, such as an object snapping to a guide or ruler.

For more information, read [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md), [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md), [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md), [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Initializing a feedback generator

- [+ feedbackGeneratorForView:](<uifeedbackgenerator/init(view_).md>) — Creates a feedback generator and attaches it to the specified view.

### Preparing to generate feedback

- [- prepare](<uifeedbackgenerator/prepare().md>) — Prepares the generator to trigger feedback.

### Deprecated

- [- init](<uifeedbackgenerator/init().md>) — Creates a feedback generator. _(deprecated)_

## See Also

### Haptic feedback

- [Playing haptic feedback in your app](../applepencil/playing-haptic-feedback-in-your-app.md) — Provide tactile feedback when people perform certain actions in your app.
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md) — A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.
