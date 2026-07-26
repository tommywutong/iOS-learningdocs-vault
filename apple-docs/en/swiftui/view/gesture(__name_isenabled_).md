---
title: 'gesture(_:name:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/gesture(_:name:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/gesture(_:name:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/gesture%28_%3Aname%3Aisenabled%3A%29.json'
content_hash: 'sha256:03f4909d5fc1ca5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# gesture(_:name:isEnabled:)

<sub>Instance Method</sub>

Attaches a gesture to the view with a lower precedence than gestures defined by the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func gesture<T>(_ gesture: T, name: String, isEnabled: Bool = true) -> some View where T : Gesture

```

## Parameters

- `gesture` — A gesture to attach to the view.

- `name` — A string that identifies the gesture. In iOS, the name can be used to set up failure relationships between UIKit gesture recognizers and this gesture.

- `isEnabled` — Whether the added gesture is enabled. The default value is `true`.

## Discussion

Use this method when you need to attach a gesture to a view. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s [VStack](../vstack.md). Inside the [VStack](../vstack.md) a red heart [Image](../image.md) defines its own [TapGesture](../tapgesture.md) handler that also prints a message to the console, and blue rectangle with no custom gesture handlers. Tapping or clicking the image prints a message to the console from the tap gesture handler on the image, while tapping or clicking  the rectangle inside the [VStack](../vstack.md) prints a message in the console from the enclosing vertical stack gesture handler.

You can also use the `isEnabled` parameter to conditionally disable the gesture.

```swift
struct GestureExample: View {
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
        .gesture(newGesture, isEnabled: isGestureEnabled)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](<gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](../draggesture.md) — A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](../windowdraggesture.md) — A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](../magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](../rotategesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](../rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](../gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
