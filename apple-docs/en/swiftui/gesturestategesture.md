---
title: GestureStateGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesturestategesture
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestategesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestategesture.json'
content_hash: 'sha256:aadc9f2d777638b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GestureStateGesture

<sub>Structure</sub>

A gesture that updates the state provided by a gesture’s updating callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct GestureStateGesture<Base, State> where Base : Gesture
```

## Overview

A gesture’s [updating(_:body:)](<gesture/updating(__body_).md>) callback returns a `GestureStateGesture` instance for updating a transient state property that’s annotated with the [GestureState](gesturestate.md) property wrapper.

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating an in-progress gesture

- [init(base:state:body:)](<gesturestategesture/init(base_state_body_).md>) — Creates a new gesture that’s the result of an ongoing gesture.
- [base](gesturestategesture/base.md) — The originating gesture.
- [state](gesturestategesture/state.md) — A value that changes as the user performs the gesture.

### Supporting types

- [body](gesturestategesture/body.md) — The updating gesture containing the originating gesture’s value, the updated state of the gesture, and a transaction.

## See Also

### Managing gesture state

- [GestureState](gesturestate.md) — A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.
