---
title: 'easeInOut(duration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/easeinout(duration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/easeinout(duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/easeinout%28duration%3A%29.json'
content_hash: 'sha256:07a727360547def4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# easeInOut(duration:)

<sub>Type Method</sub>

An animation with a specified duration that combines the behaviors of in and out easing animations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func easeInOut(duration: TimeInterval) -> Animation
```

## Parameters

- `duration` — The length of time, expressed in seconds, that the animation takes to complete.

## Return Value

An ease-in ease-out animation with a specified duration.

## Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. An ease in and out animation starts slowly, increasing its speed towards the halfway point, and finally decreasing the speed towards the end of the animation.

Use `easeInOut(duration:)` when you want to specify the time it takes for the animation to complete. Otherwise, use [easeInOut](easeinout.md) to perform the animation for a default length of time.

The following code shows an example of animating the size changes of a [Circle](../circle.md) using an ease in and out animation with a duration of one second.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeInOut(duration: 1.0), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

[A video that shows a circle enlarging for one second, then shrinking for another second to its original size using an ease-in ease-out animation.](https://docs-assets.developer.apple.com/published/954bd4aee69c3031d2690693b24b44af/animation-13-easeineaseout-duration.mp4)

## See Also

### Getting eased animations

- [easeIn](easein.md) — An animation that starts slowly and then increases speed towards the end of the movement.
- [easeIn(duration:)](<easein(duration_).md>) — An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [easeOut](easeout.md) — An animation that starts quickly and then slows towards the end of the movement.
- [easeOut(duration:)](<easeout(duration_).md>) — An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [easeInOut](easeinout.md) — An animation that combines the behaviors of in and out easing animations.
