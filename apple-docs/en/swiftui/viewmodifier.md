---
title: ViewModifier
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewmodifier
source_url: 'https://developer.apple.com/documentation/swiftui/viewmodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewmodifier.json'
content_hash: 'sha256:8c0ba61e17024f17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ViewModifier

<sub>Protocol</sub>

A modifier that you apply to a view or another view modifier, producing a different version of the original value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ViewModifier
```

## Overview

Adopt the [ViewModifier](viewmodifier.md) protocol when you want to create a reusable modifier that you can apply to any view. The example below combines several modifiers to create a new modifier that you can use to create blue caption text surrounded by a rounded rectangle:

```swift
struct BorderedCaption: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption2)
            .padding(10)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 1)
            )
            .foregroundColor(Color.blue)
    }
}
```

You can apply [modifier(_:)](<view/modifier(__).md>) directly to a view, but a more common and idiomatic approach uses [modifier(_:)](<view/modifier(__).md>) to define an extension to [View](view.md) itself that incorporates the view modifier:

```swift
extension View {
    func borderedCaption() -> some View {
        modifier(BorderedCaption())
    }
}
```

You can then apply the bordered caption to any view, similar to this:

```swift
Image(systemName: "bus")
    .resizable()
    .frame(width:50, height:50)
Text("Downtown Bus")
    .borderedCaption()
```

![A screenshot showing the image of a bus with a caption reading](../../../attachments/dc0170d83bbfb353e45ad5d2e90f7fe6/SwiftUI-View-ViewModifier@2x.png)

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Inherited By**: [AnimatableModifier](animatablemodifier.md), [EnvironmentalModifier](environmentalmodifier.md), [GeometryEffect](geometryeffect.md)

- **Conforming Types**: [AccessibilityAttachmentModifier](accessibilityattachmentmodifier.md), [EmptyModifier](emptymodifier.md), [LayoutRotationUnaryLayout](layoutrotationunarylayout.md), [ManipulableModifier](manipulablemodifier.md), [ManipulableResponderModifier](manipulablerespondermodifier.md), [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md), [ManipulationGeometryModifier](manipulationgeometrymodifier.md), [ManipulationGestureModifier](manipulationgesturemodifier.md), [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md), [ModifiedContent](modifiedcontent.md)

## Topics

### Creating a view modifier

- [body(content:)](<viewmodifier/body(content_).md>) — Gets the current body of the caller.
- [Body](viewmodifier/body.md) — The type of view representing the body.
- [Content](viewmodifier/content.md) — The content view type passed to `body()`.

### Adding animations to a view

- [animation(_:)](<viewmodifier/animation(__).md>) — Returns a new version of the modifier that will apply `animation` to all animatable values within the modifier.
- [concat(_:)](<viewmodifier/concat(__).md>) — Returns a new modifier that is the result of concatenating `self` with `modifier`.

### Handling view taps and gestures

- [transaction(_:)](<viewmodifier/transaction(__).md>) — Returns a new version of the modifier that will apply the transaction mutation function `transform` to all transactions within the modifier.

## See Also

### Modifying a view

- [Configuring views](configuring-views.md) — Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md) — Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](<view/modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [EmptyModifier](emptymodifier.md) — An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](modifiedcontent.md) — A value with a modifier applied to it.
- [EnvironmentalModifier](environmentalmodifier.md) — A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [Manipulable](manipulable.md) — A namespace for various manipulable related types.
