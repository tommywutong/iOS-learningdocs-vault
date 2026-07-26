---
title: 'highPriorityGesture(_:name:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/highprioritygesture(_:name:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/highprioritygesture(_:name:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/highprioritygesture%28_%3Aname%3Aisenabled%3A%29.json'
content_hash: 'sha256:60054dac920e5c4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# highPriorityGesture(_:name:isEnabled:)

<sub>Instance Method</sub>

Attaches a gesture to the view with a higher precedence than gestures defined by the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func highPriorityGesture<T>(_ gesture: T, name: String, isEnabled: Bool = true) -> some View where T : Gesture

```

## Parameters

- `gesture` — A gesture to attach to the view.

- `name` — A string that identifies the gesture. In iOS, the name can be used to set up failure relationships between UIKit gesture recognizers and this gesture.

- `isEnabled` — Whether the added gesture is enabled. The default value is `true`.

## Discussion

Use this method when you need to define a high priority gesture to take precedence over the view’s existing gestures. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s [VStack](../vstack.md). Inside the [VStack](../vstack.md) a red heart [Image](../image.md) defines its own [TapGesture](../tapgesture.md) handler that also prints a message to the console, and a blue rectangle with no custom gesture handlers. Tapping or clicking any of the views results in a console message from the high priority gesture attached to the enclosing [VStack](../vstack.md).

You can also use the `isEnabled` parameter to conditionally disable the gesture.

```swift
struct HighPriorityGestureExample: View {
    @State private var message = "Message"
    var isGestureEnabled: Bool
    let newGesture = TapGesture().onEnded {
        print("Tap on VStack.")
    }

    var body: some View {
        VStack(spacing:25) {
            Image(systemName: "heart.fill")
                .resizable()
                .frame(width: 75, height: 75)
                .padding()
                .foregroundColor(.red)
                .onTapGesture {
                    print("Tap on image.")
                }
            Rectangle()
                .fill(Color.blue)
        }
        .highPriorityGesture(
            newGesture, isEnabled: isGestureEnabled)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](<highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](../gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](../anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](../handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](../handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
