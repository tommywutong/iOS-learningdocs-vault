---
title: AnyGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anygesture
source_url: 'https://developer.apple.com/documentation/swiftui/anygesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anygesture.json'
content_hash: 'sha256:2aeba008485fe221'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyGesture

<sub>Structure</sub>

A type-erased gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct AnyGesture<Value>
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Implementing a custom gesture

- [init(_:)](<anygesture/init(__).md>) — Creates an instance from another gesture.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [HandActivationBehavior](handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
