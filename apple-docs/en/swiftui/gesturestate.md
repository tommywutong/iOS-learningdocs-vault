---
title: GestureState
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesturestate
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestate.json'
content_hash: 'sha256:287785e2bd76f0e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GestureState

<sub>Structure</sub>

A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@propertyWrapper @frozen struct GestureState<Value>
```

## Overview

Declare a property as `@GestureState`, pass as a binding to it as a parameter to a gesture’s [updating(_:body:)](<gesture/updating(__body_).md>) callback, and receive updates to it. A property that’s declared as `@GestureState` implicitly resets when the gesture becomes inactive, making it suitable for tracking transient state.

Add a long-press gesture to a [Circle](circle.md), and update the interface during the gesture by declaring a property as `@GestureState`:

```swift
struct SimpleLongPressGestureView: View {
    @GestureState private var isDetectingLongPress = false

    var longPress: some Gesture {
        LongPressGesture(minimumDuration: 3)
            .updating($isDetectingLongPress) { currentState, gestureState, transaction in
                gestureState = currentState
            }
    }

    var body: some View {
        Circle()
            .fill(self.isDetectingLongPress ? Color.red : Color.green)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(longPress)
    }
}
```

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a gesture state

- [init(initialValue:)](<gesturestate/init(initialvalue_).md>) — Creates a view state that’s derived from a gesture with an initial value.
- [init(initialValue:reset:)](<gesturestate/init(initialvalue_reset_).md>) — Creates a view state that’s derived from a gesture with an initial state value and a closure that provides a transaction to reset it.
- [init(initialValue:resetTransaction:)](<gesturestate/init(initialvalue_resettransaction_).md>) — Creates a view state that’s derived from a gesture with an initial state value and a transaction to reset it.
- [init(reset:)](<gesturestate/init(reset_).md>) — Creates a view state that’s derived from a gesture with a closure that provides a transaction to reset it.
- [init(resetTransaction:)](<gesturestate/init(resettransaction_).md>) — Creates a view state that’s derived from a gesture with a transaction to reset it.
- [init(wrappedValue:)](<gesturestate/init(wrappedvalue_).md>) — Creates a view state that’s derived from a gesture.
- [init(wrappedValue:reset:)](<gesturestate/init(wrappedvalue_reset_).md>) — Creates a view state that’s derived from a gesture with a wrapped state value and a closure that provides a transaction to reset it.
- [init(wrappedValue:resetTransaction:)](<gesturestate/init(wrappedvalue_resettransaction_).md>) — Creates a view state that’s derived from a gesture with a wrapped state value and a transaction to reset it.

### Getting the state

- [wrappedValue](gesturestate/wrappedvalue.md) — The wrapped value referenced by the gesture state property.
- [projectedValue](gesturestate/projectedvalue.md) — A binding to the gesture state property.

## See Also

### Managing gesture state

- [GestureStateGesture](gesturestategesture.md) — A gesture that updates the state provided by a gesture’s updating callback.
