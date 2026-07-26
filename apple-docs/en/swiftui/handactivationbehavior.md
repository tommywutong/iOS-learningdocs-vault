---
title: HandActivationBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/handactivationbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/handactivationbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/handactivationbehavior.json'
content_hash: 'sha256:2be8dd7016fe7e08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HandActivationBehavior

<sub>Structure</sub>

An activation behavior specific to hand-driven input.

<sub>visionOS</sub>

```swift
struct HandActivationBehavior
```

## Overview

Hand activation behavior determines what hand input modes activate a gesture.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Getting the behaviors

- [automatic](handactivationbehavior/automatic.md) — The default activation behavior, including direct touch, direct pinch, and indirect pinch.
- [pinch](handactivationbehavior/pinch.md) — Activation that requires a pinched hand.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](anygesture.md) — A type-erased gesture.
- [HandGestureShortcut](handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
