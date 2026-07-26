---
title: 'linear(duration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/linear(duration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/linear(duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/linear%28duration%3A%29.json'
content_hash: 'sha256:9f52bf47e5d30574'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# linear(duration:)

<sub>Type Method</sub>

An animation that moves at a constant speed during a specified duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func linear(duration: TimeInterval) -> Animation
```

## Parameters

- `duration` — The length of time, expressed in seconds, that the animation takes to complete.

## Return Value

A linear animation with a specified duration.

## Discussion

A linear animation provides a mechanical feel to the motion because its speed is consistent from start to finish of the animation. This constant speed makes a linear animation ideal for animating the movement of objects where changes in the speed might feel awkward, such as with an activity indicator.

Use `linear(duration:)` when you want to specify the time it takes for the animation to complete. Otherwise, use [linear](linear.md) to perform the animation for a default length of time.

The following code shows an example of using linear animation with a duration of two seconds to animate the movement of a circle as it moves between the leading and trailing edges of the view. The color of the circle also animates from red to blue as it moves across the view.

```swift
struct ContentView: View {
    @State private var isActive = false

    var body: some View {
        VStack(alignment: isActive ? .trailing : .leading) {
            Circle()
                .fill(isActive ? Color.red : Color.blue)
                .frame(width: 50, height: 50)

            Button("Animate") {
                withAnimation(.linear(duration: 2.0)) {
                    isActive.toggle()
                }
            }
            .frame(maxWidth: .infinity)
        }
    }
}
```

[A video that shows a circle moving from the leading edge of the view to the trailing edge. The color of the circle also changes from red to blue as it moves across the view. Then the circle moves from the trailing edge back to the leading edge while also changing colors from blue to red.](https://docs-assets.developer.apple.com/published/62f2993e970b3eaeb50af95099df0ff5/animation-07-linear-duration.mp4)

## See Also

### Getting linear animations

- [linear](linear.md) — An animation that moves at a constant speed.
