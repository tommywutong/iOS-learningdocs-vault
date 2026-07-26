---
title: 'repeatCount(_:autoreverses:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/repeatcount(_:autoreverses:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/repeatcount(_:autoreverses:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/repeatcount%28_%3Aautoreverses%3A%29.json'
content_hash: 'sha256:f45b4c0fa57ef512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# repeatCount(_:autoreverses:)

<sub>Instance Method</sub>

Repeats the animation for a specific number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func repeatCount(_ repeatCount: Int, autoreverses: Bool = true) -> Animation
```

## Parameters

- `repeatCount` — The number of times that the animation repeats. Each repeated sequence starts at the beginning when `autoreverse` is `false`.

- `autoreverses` — A Boolean value that indicates whether the animation sequence plays in reverse after playing forward. Autoreverse counts towards the `repeatCount`. For instance, a `repeatCount` of one plays the animation forward once, but it doesn’t play in reverse even if `autoreverse` is `true`. When `autoreverse` is `true` and `repeatCount` is `2`, the animation moves forward, then reverses, then stops.

## Return Value

An animation that repeats for specific number of times.

## Discussion

Use this method to repeat the animation a specific number of times. For example, in the following code, the animation moves a truck from one edge of the view to the other edge. It repeats this animation three times.

```swift
struct ContentView: View {
    @State private var driveForward = true

    private var driveAnimation: Animation {
        .easeInOut
        .repeatCount(3, autoreverses: true)
        .speed(0.5)
    }

    var body: some View {
        VStack(alignment: driveForward ? .leading : .trailing, spacing: 40) {
            Image(systemName: "box.truck")
                .font(.system(size: 48))
                .animation(driveAnimation, value: driveForward)

            HStack {
                Spacer()
                Button("Animate") {
                    driveForward.toggle()
                }
                Spacer()
            }
        }
    }
}
```

[A video that shows a box truck moving from the leading edge of a view to the trailing edge, and back again before looping in the opposite direction.](https://docs-assets.developer.apple.com/published/0487e62f57bb52b02ae23586025ad4f3/animation-16-repeat-count.mp4)

The first time the animation runs, the truck moves from the leading edge to the trailing edge of the view. The second time the animation runs, the truck moves from the trailing edge to the leading edge because `autoreverse` is `true`. If `autoreverse` were `false`, the truck would jump back to leading edge before moving to the trailing edge. The third time the animation runs, the truck moves from the leading to the trailing edge of the view.

## See Also

### Configuring an animation

- [delay(_:)](<delay(__).md>) — Delays the start of the animation by the specified number of seconds.
- [repeatForever(autoreverses:)](<repeatforever(autoreverses_).md>) — Repeats the animation for the lifespan of the view containing the animation.
- [speed(_:)](<speed(__).md>) — Changes the duration of an animation by adjusting its speed.
