---
title: 'highPriorityGesture(_:including:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/highprioritygesture(_:including:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/highprioritygesture(_:including:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/highprioritygesture%28_%3Aincluding%3A%29.json'
content_hash: 'sha256:7a0056ce71c817f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# highPriorityGesture(_:including:)

<sub>Instance Method</sub>

Attaches a gesture to the view with a higher precedence than gestures defined by the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func highPriorityGesture<T>(_ gesture: T, including mask: GestureMask = .all) -> some View where T : Gesture

```

## Parameters

- `gesture` — A gesture to attach to the view.

- `mask` — A value that controls how adding this gesture to the view affects other gestures recognized by the view and its subviews. Defaults to [all](../gesturemask/all.md).

## Discussion

Use this method when you need to define a high priority gesture to take precedence over the view’s existing gestures. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s [VStack](../vstack.md). Inside the [VStack](../vstack.md) a red heart [Image](../image.md) defines its own [TapGesture](../tapgesture.md) handler that also prints a message to the console, and a blue rectangle with no custom gesture handlers. Tapping or clicking any of the views results in a console message from the high priority gesture attached to the enclosing [VStack](../vstack.md).

```swift
struct HighPriorityGestureExample: View {
    @State private var message = "Message"
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
        .highPriorityGesture(newGesture)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## See Also

### Defining custom gestures

- [highPriorityGesture(_:isEnabled:)](<highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](../gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](../anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](../handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](../handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
