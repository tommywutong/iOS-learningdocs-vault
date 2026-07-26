---
title: Gesture
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesture
source_url: 'https://developer.apple.com/documentation/swiftui/gesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture.json'
content_hash: 'sha256:fa366ee4d1f403ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Gesture

<sub>Protocol</sub>

An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol Gesture<Value>
```

## Overview

Create custom gestures by declaring types that conform to the `Gesture` protocol.

## Relationships

- **Conforming Types**: [AnyGesture](anygesture.md), [DragGesture](draggesture.md), [ExclusiveGesture](exclusivegesture.md), [GestureStateGesture](gesturestategesture.md), [LongPressGesture](longpressgesture.md), [MagnificationGesture](magnificationgesture.md), [MagnifyGesture](magnifygesture.md), [RotateGesture](rotategesture.md), [RotateGesture3D](rotategesture3d.md), [RotationGesture](rotationgesture.md), [SequenceGesture](sequencegesture.md), [SimultaneousGesture](simultaneousgesture.md), [SpatialEventGesture](spatialeventgesture.md), [SpatialTapGesture](spatialtapgesture.md), [TapGesture](tapgesture.md), [WindowDragGesture](windowdraggesture.md)

## Topics

### Implementing a custom gesture

- [body](gesture/body-swift.property.md) — The content and behavior of the gesture.
- [Body](gesture/body-swift.associatedtype.md) — The type of gesture representing the body of `Self`.

### Performing the gesture

- [updating(_:body:)](<gesture/updating(__body_).md>) — Updates the provided gesture state property as the gesture’s value changes.
- [onChanged(_:)](<gesture/onchanged(__).md>) — Adds an action to perform when the gesture’s value changes.
- [onEnded(_:)](<gesture/onended(__).md>) — Adds an action to perform when the gesture ends.
- [Value](gesture/value.md) — The type representing the gesture’s value.

### Composing gestures

- [simultaneously(with:)](<gesture/simultaneously(with_).md>) — Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [sequenced(before:)](<gesture/sequenced(before_).md>) — Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.
- [exclusively(before:)](<gesture/exclusively(before_).md>) — Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.

### Adding modifier keys to a gesture

- [modifiers(_:)](<gesture/modifiers(__).md>) — Combines a gesture with keyboard modifiers.

### Transforming a gesture

- [map(_:)](<gesture/map(__).md>) — Returns a gesture that uses the given closure to map over this gesture’s value.

### Customizing gesture activation

- [handActivationBehavior(_:)](<gesture/handactivationbehavior(__).md>) — Customizes the activation behavior for a gesture when driven by hand or hand-like input.

### Using a gesture with a RealityKit entity

- [targetedToAnyEntity()](<gesture/targetedtoanyentity().md>) — Requires this gesture to target an entity.
- [targetedToEntity(_:)](<gesture/targetedtoentity(__).md>) — Requires this gesture to target an entity or a descendant of entity.
- [targetedToEntity(where:)](<gesture/targetedtoentity(where_).md>) — Requires this gesture to target an entity that can be found in the results of the query.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [AnyGesture](anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
