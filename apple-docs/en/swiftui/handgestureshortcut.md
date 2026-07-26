---
title: HandGestureShortcut
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/handgestureshortcut
source_url: 'https://developer.apple.com/documentation/swiftui/handgestureshortcut'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/handgestureshortcut.json'
content_hash: 'sha256:f325762461aeb029'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HandGestureShortcut

<sub>Structure</sub>

Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
struct HandGestureShortcut
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [primaryAction](handgestureshortcut/primaryaction.md) — The hand gesture shortcut for the primary action.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](handactivationbehavior.md) — An activation behavior specific to hand-driven input.
