---
title: 'speed(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/speed(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/speed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/speed%28_%3A%29.json'
content_hash: 'sha256:4fdab6bcd9c821d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# speed(_:)

<sub>Instance Method</sub>

Changes the duration of an animation by adjusting its speed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func speed(_ speed: Double) -> Animation
```

## Parameters

- `speed` — The speed at which SwiftUI performs the animation.

## Return Value

An animation with the adjusted speed.

## Discussion

Setting the speed of an animation changes the duration of the animation by a factor of `speed`. A higher speed value causes a faster animation sequence due to a shorter duration. For example, a one-second animation with a speed of `2.0` completes in half the time (half a second).

```swift
struct ContentView: View {
    @State private var adjustBy = 100.0

    private var oneSecondAnimation: Animation {
       .easeInOut(duration: 1.0)
    }

    var body: some View {
        VStack(spacing: 40) {
            HStack(alignment: .bottom) {
                Capsule()
                    .frame(width: 50, height: 175 - adjustBy)
                Capsule()
                    .frame(width: 50, height: 175 + adjustBy)
            }
            .animation(oneSecondAnimation.speed(2.0), value: adjustBy)

            Button("Animate") {
                adjustBy *= -1
            }
        }
    }
}
```

[A video that shows two capsules side by side that animate using the ease-in ease-out animation. The capsule on the left is short, while the capsule on the right is tall. They animate for half a second with the short capsule growing upwards to match the height of the tall capsule. Then the tall capsule shrinks to match the original height of the short capsule. For another half second, the capsule on the left shrinks to its original height, followed by the capsule on the right growing to its original height.](https://docs-assets.developer.apple.com/published/3d310db24e3792cf9a4df12f20ea7273/animation-18-speed.mp4)

Setting `speed` to a lower number slows the animation, extending its duration. For example, a one-second animation with a speed of `0.25` takes four seconds to complete.

```swift
struct ContentView: View {
    @State private var adjustBy = 100.0

    private var oneSecondAnimation: Animation {
       .easeInOut(duration: 1.0)
    }

    var body: some View {
        VStack(spacing: 40) {
            HStack(alignment: .bottom) {
                Capsule()
                    .frame(width: 50, height: 175 - adjustBy)
                Capsule()
                    .frame(width: 50, height: 175 + adjustBy)
            }
            .animation(oneSecondAnimation.speed(0.25), value: adjustBy)

            Button("Animate") {
                adjustBy *= -1
            }
        }
    }
}
```

[A video that shows two capsules side by side that animate using the ease-in ease-out animation. The capsule on the left is short, while the right-side capsule is tall. They animate for four seconds with the short capsule growing upwards to match the height of the tall capsule. Then the tall capsule shrinks to match the original height of the short capsule. For another four seconds, the capsule on the left shrinks to its original height, followed by the capsule on the right growing to its original height.](https://docs-assets.developer.apple.com/published/7cf64cddc821a35409ea887020e2ac04/animation-19-speed-slow.mp4)

## See Also

### Configuring an animation

- [delay(_:)](<delay(__).md>) — Delays the start of the animation by the specified number of seconds.
- [repeatCount(_:autoreverses:)](<repeatcount(__autoreverses_).md>) — Repeats the animation for a specific number of times.
- [repeatForever(autoreverses:)](<repeatforever(autoreverses_).md>) — Repeats the animation for the lifespan of the view containing the animation.
