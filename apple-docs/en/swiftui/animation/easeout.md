---
title: easeOut
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animation/easeout
source_url: 'https://developer.apple.com/documentation/swiftui/animation/easeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/easeout.json'
content_hash: 'sha256:ca758e378bf25f0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# easeOut

<sub>Type Property</sub>

An animation that starts quickly and then slows towards the end of the movement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var easeOut: Animation { get }
```

## Return Value

An ease-out animation with the default duration.

## Discussion

An easing animation provides motion with a natural feel by varying the acceleration and deceleration of the animation, which matches how things tend to move in reality. With an ease out animation, the motion starts quickly and decreases its speed towards the end.

The `easeOut` animation has a default duration of 0.35 seconds. To specify a different duration, use [easeOut(duration:)](<easeout(duration_).md>).

The following code shows an example of animating the size changes of a [Circle](../circle.md) using an ease out animation.

```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scale(scale)
                .animation(.easeOut, value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
    }
}
```

[A video that shows a circle enlarging, then shrinking to its original size using an ease-out animation.](https://docs-assets.developer.apple.com/published/be9a4eb76cffd31920ea7f76677e2968/animation-10-easeout.mp4)

## See Also

### Getting eased animations

- [easeIn](easein.md) — An animation that starts slowly and then increases speed towards the end of the movement.
- [easeIn(duration:)](<easein(duration_).md>) — An animation with a specified duration that starts slowly and then increases speed towards the end of the movement.
- [easeOut(duration:)](<easeout(duration_).md>) — An animation with a specified duration that starts quickly and then slows towards the end of the movement.
- [easeInOut](easeinout.md) — An animation that combines the behaviors of in and out easing animations.
- [easeInOut(duration:)](<easeinout(duration_).md>) — An animation with a specified duration that combines the behaviors of in and out easing animations.
