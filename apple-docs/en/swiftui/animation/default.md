---
title: default
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animation/default
source_url: 'https://developer.apple.com/documentation/swiftui/animation/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/default.json'
content_hash: 'sha256:f6b66577f9771245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# default

<sub>Type Property</sub>

A default animation instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: Animation
```

## Discussion

The `default` animation is [spring(response:dampingFraction:blendDuration:)](<spring(response_dampingfraction_blendduration_).md>) with:

- `response` equal to `0.55`
- `dampingFraction` equal to `1.0`
- `blendDuration` equal to `0.0`

Prior to iOS 17, macOS 14, tvOS 17, and watchOS 10, the `default` animation is [easeInOut](easeinout.md).

The global function [withAnimation(_:_:)](<../withanimation(____).md>) uses the default animation if you don’t provide one. For instance, the following code listing shows an example of using the `default` animation to flip the text “Hello” each time someone clicks the Animate button.

```swift
struct ContentView: View {
    @State private var degrees = Double.zero

    var body: some View {
        VStack {
            Spacer()
            Text("Hello")
                .font(.largeTitle)
                .rotation3DEffect(.degrees(degrees), axis: (x: 0, y: 1, z: 0))

            Spacer()
            Button("Animate") {
                withAnimation {
                    degrees = (degrees == .zero) ? 180 : .zero
                }
            }
        }
    }
}
```

[A video that shows the word Hello flip horizontally so that its letters appear backwards. Then it flips in reverse so that the word Hello appears correctly.](https://docs-assets.developer.apple.com/published/5dc509ab7229b85190cf5f494b5093a0/animation-04-default-flip.mp4)

To use the `default` animation when adding the [animation(_:value:)](<../view/animation(__value_).md>) view modifier, specify it explicitly as the animation type. For instance, the following code shows an example of the `default` animation to spin the text “Hello” each time someone clicks the Animate button.

```swift
struct ContentView: View {
    @State private var degrees = Double.zero

    var body: some View {
        VStack {
            Spacer()
            Text("Hello")
                .font(.largeTitle)
                .rotationEffect(.degrees(degrees))
                .animation(.default, value: degrees)

            Spacer()
            Button("Animate") {
                degrees = (degrees == .zero) ? 360 : .zero
            }
        }
    }
}
```

[A video that shows the word Hello spinning clockwise for one full rotation, that is, 360 degrees. Then Hello spins counterclockwise for one full rotation.](https://docs-assets.developer.apple.com/published/3c7cc17bbb42c934cc4e26cea6d4feec/animation-05-default-spin.mp4)

A `default` animation instance is only equal to other `default` animation instances (using `==`), and not equal to other animation instances even when the animations are identical. For example, if you create an animation using the [spring(response:dampingFraction:blendDuration:)](<spring(response_dampingfraction_blendduration_).md>) modifier with the same parameter values that `default` uses, the animation isn’t equal to `default`. This behavior lets you differentiate between animations that you intentionally choose and those that use the `default` animation.
