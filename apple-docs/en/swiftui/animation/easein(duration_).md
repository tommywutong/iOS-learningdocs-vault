---
title: 'easeIn(duration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/easein(duration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/easein(duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/easein%28duration%3A%29.json'
content_hash: 'sha256:68a0799ea221544a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# easeIn(duration:)

<sub>Type Method</sub>

An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func easeIn(duration: TimeInterval) -> Animation
```

## Parameters

- `duration` — The length of time, expressed in seconds, that the animation takes to complete.

## Return Value

An ease-in animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. With an ease in animation, the motion starts slowly and increases its speed towards the end.

Use `easeIn(duration:)` when you want to specify the time it takes for the animation to complete. Otherwise, use [easeIn](easein.md) to perform the animation for a default length of time.

The following code shows an example of animating the size changes of a [Circle](../circle.md) using an ease in animation with a duration of one second.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeIn(duration: 1.0), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

[A video that shows a circle enlarging for one second, then shrinking for another second to its original size using an ease-in animation.](https://docs-assets.developer.apple.com/published/c0b2e2b38ca5e40487780fc772b4ab5b/animation-09-easein-duration.mp4)

## See Also

### Getting eased animations

- [easeIn](easein.md) — An animation that starts slowly and then increases speed towards the end of the movement.
- [easeOut](easeout.md) — An animation that starts quickly and then slows towards the end of the movement.
- [easeOut(duration:)](<easeout(duration_).md>) — An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [easeInOut](easeinout.md) — An animation that combines the behaviors of in and out easing animations.
- [easeInOut(duration:)](<easeinout(duration_).md>) — An animation with a specified duration that combines the behaviors of in and out easing animations.
