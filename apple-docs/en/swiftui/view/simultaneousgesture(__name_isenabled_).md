---
title: 'simultaneousGesture(_:name:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/simultaneousgesture(_:name:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/simultaneousgesture(_:name:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/simultaneousgesture%28_%3Aname%3Aisenabled%3A%29.json'
content_hash: 'sha256:a2b28ffe836ef203'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# simultaneousGesture(_:name:isEnabled:)

<sub>Instance Method</sub>

Attaches a gesture to the view to process simultaneously with gestures defined by the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func simultaneousGesture<T>(_ gesture: T, name: String, isEnabled: Bool = true) -> some View where T : Gesture

```

## Parameters

- `gesture` — A gesture to attach to the view.

- `name` — A string that identifies the gesture. In iOS, the name can be used to set up failure relationships between UIKit gesture recognizers and this gesture.

- `isEnabled` — Whether the added gesture is enabled. The default value is `true`.

## Discussion

Use this method when you need to define and process  a view specific gesture simultaneously with the same priority as the view’s existing gestures. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s [VStack](../vstack.md). Inside the [VStack](../vstack.md) is a red heart [Image](../image.md) defines its own [TapGesture](../tapgesture.md) handler that also prints a message to the console and a blue rectangle with no custom gesture handlers.

You can also use the `isEnabled` parameter to conditionally disable the gesture.

Tapping or clicking the “heart” image sends two messages to the console: one for the image’s tap gesture handler, and the other from a custom gesture handler attached to the enclosing vertical stack. Tapping or clicking on the blue rectangle results only in the single message to the console from the tap recognizer attached to the [VStack](../vstack.md):

```swift
struct SimultaneousGestureExample: View {
    @State private var message = "Message"
    var isGestureEnabled: Bool
    let newGesture = TapGesture().onEnded {
        print("Gesture on VStack.")
    }

    var body: some View {
        VStack(spacing:25) {
            Image(systemName: "heart.fill")
                .resizable()
                .frame(width: 75, height: 75)
                .padding()
                .foregroundColor(.red)
                .onTapGesture {
                    print("Gesture on image.")
                }
            Rectangle()
                .fill(Color.blue)
        }
        .simultaneousGesture(
            newGesture, isEnabled: isGestureEnabled)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## See Also

### Combining gestures

- [Composing SwiftUI gestures](../composing-swiftui-gestures.md) — Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](<simultaneousgesture(__including_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](<simultaneousgesture(__isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SequenceGesture](../sequencegesture.md) — A gesture that’s a sequence of two gestures.
- [SimultaneousGesture](../simultaneousgesture.md) — A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [ExclusiveGesture](../exclusivegesture.md) — A gesture that consists of two gestures where only one of them can succeed.
