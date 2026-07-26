---
title: 'delay(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/delay(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/delay(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/delay%28_%3A%29.json'
content_hash: 'sha256:917e8941b736f894'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# delay(_:)

<sub>Instance Method</sub>

Delays the start of the animation by the specified number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func delay(_ delay: TimeInterval) -> Animation
```

## Parameters

- `delay` — The number of seconds to delay the start of the animation.

## Return Value

An animation with a delayed start.

## Discussion

Use this method to delay the start of an animation. For example, the following code animates the height change of two capsules. Animation of the first [Capsule](../capsule.md) begins immediately. However, animation of the second one doesn’t begin until a half second later.

```swift
struct ContentView: View {
    @State private var adjustBy = 100.0

    var body: some View {
        VStack(spacing: 40) {
            HStack(alignment: .bottom) {
                Capsule()
                    .frame(width: 50, height: 175 - adjustBy)
                    .animation(.easeInOut, value: adjustBy)
                Capsule()
                    .frame(width: 50, height: 175 + adjustBy)
                    .animation(.easeInOut.delay(0.5), value: adjustBy)
            }

            Button("Animate") {
                adjustBy *= -1
            }
        }
    }
}
```

[A video that shows two capsules side by side that animate using the ease-in ease-out animation. The capsule on the left is short, while the capsule on the right is tall. As they animate, the short capsule grows upwards to match the height of the tall capsule. Then the tall capsule shrinks to match the original height of the short capsule. Then the capsule on the left shrinks to its original height, followed by the capsule on the right growing to its original height.](https://docs-assets.developer.apple.com/published/0f1ee5cdba675e14c754226cde99382d/animation-15-delay.mp4)

## See Also

### Configuring an animation

- [repeatCount(_:autoreverses:)](<repeatcount(__autoreverses_).md>) — Repeats the animation for a specific number of times.
- [repeatForever(autoreverses:)](<repeatforever(autoreverses_).md>) — Repeats the animation for the lifespan of the view containing the animation.
- [speed(_:)](<speed(__).md>) — Changes the duration of an animation by adjusting its speed.
