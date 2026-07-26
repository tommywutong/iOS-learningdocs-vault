---
title: 'repeatForever(autoreverses:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/repeatforever(autoreverses:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/repeatforever(autoreverses:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/repeatforever%28autoreverses%3A%29.json'
content_hash: 'sha256:54a0aad6631bebd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# repeatForever(autoreverses:)

<sub>Instance Method</sub>

Repeats the animation for the lifespan of the view containing the animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func repeatForever(autoreverses: Bool = true) -> Animation
```

## Parameters

- `autoreverses` — A Boolean value that indicates whether the animation sequence plays in reverse after playing forward.

## Return Value

An animation that continuously repeats.

## Discussion

Use this method to repeat the animation until the instance of the view no longer exists, or the view’s explicit or structural identity changes. For example, the following code continuously rotates a gear symbol for the lifespan of the view.

```swift
struct ContentView: View {
    @State private var rotationDegrees = 0.0

    private var animation: Animation {
        .linear
        .speed(0.1)
        .repeatForever(autoreverses: false)
    }

    var body: some View {
        Image(systemName: "gear")
            .font(.system(size: 86))
            .rotationEffect(.degrees(rotationDegrees))
            .onAppear {
                withAnimation(animation) {
                    rotationDegrees = 360.0
                }
            }
    }
}
```

[A video that shows a gear that continuously rotates clockwise.](https://docs-assets.developer.apple.com/published/5f38c7b81009a180a46b8acb95e5832f/animation-17-repeat-forever.mp4)

## See Also

### Configuring an animation

- [delay(_:)](<delay(__).md>) — Delays the start of the animation by the specified number of seconds.
- [repeatCount(_:autoreverses:)](<repeatcount(__autoreverses_).md>) — Repeats the animation for a specific number of times.
- [speed(_:)](<speed(__).md>) — Changes the duration of an animation by adjusting its speed.
