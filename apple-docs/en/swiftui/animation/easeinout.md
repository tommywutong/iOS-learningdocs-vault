---
title: easeInOut
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animation/easeinout
source_url: 'https://developer.apple.com/documentation/swiftui/animation/easeinout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/easeinout.json'
content_hash: 'sha256:de01cbdca6923ce5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# easeInOut

<sub>Type Property</sub>

An animation that combines the behaviors of in and out easing animations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var easeInOut: Animation { get }
```

## Return Value

An ease-in ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. An ease in and out animation starts slowly, increasing its speed towards the halfway point, and finally decreasing the speed towards the end of the animation.

The `easeInOut` animation has a default duration of 0.35 seconds. To specify the duration, use the [easeInOut(duration:)](<easeinout(duration_).md>) method.

The following code shows an example of animating the size changes of a [Circle](../circle.md) using an ease in and out animation.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeInOut, value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

[A video that shows a circle enlarging, then shrinking to its original size using an ease-in ease-out animation.](https://docs-assets.developer.apple.com/published/e1a2c61fcf72b991ecfb3f265e8a4cd0/animation-12-easeineaseout.mp4)

## See Also

### Getting eased animations

- [easeIn](easein.md) — An animation that starts slowly and then increases speed towards the end of the movement.
- [easeIn(duration:)](<easein(duration_).md>) — An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [easeOut](easeout.md) — An animation that starts quickly and then slows towards the end of the movement.
- [easeOut(duration:)](<easeout(duration_).md>) — An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [easeInOut(duration:)](<easeinout(duration_).md>) — An animation with a specified duration that combines the behaviors of in and out easing animations.
