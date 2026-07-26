---
title: 'phaseAnimator(_:trigger:content:animation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/phaseanimator(_:trigger:content:animation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/phaseanimator(_:trigger:content:animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/phaseanimator%28_%3Atrigger%3Acontent%3Aanimation%3A%29.json'
content_hash: 'sha256:07308660c1f0d41b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# phaseAnimator(_:trigger:content:animation:)

<sub>Instance Method</sub>

Animates effects that you apply to a view over a sequence of phases that change based on a trigger.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func phaseAnimator<Phase>(_ phases: some Sequence, trigger: some Equatable, @ContentBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable

```

## Parameters

- `phases` — The sequence of phases to cycle through. Ensure that the sequence isn’t empty. If it is, SwiftUI logs a runtime warning and also returns a visual warning as the output view.

- `trigger` — A value whose changes cause the animator to use the next phase.

- `content` — A content builder closure that takes two parameters: a proxy value representing the modified view and the current phase. You can apply effects to the proxy based on the current phase.

- `animation` — A closure that takes the current phase as input. Return the animation to use when transitioning to the next phase. If you return `nil`, the transition doesn’t animate. If you don’t set this parameter, SwiftUI uses a default animation.

## Discussion

When the modified view first appears, this modifier renders its `content` closure using the first phase as input to the closure, along with a proxy for the modified view. Apply effects to the proxy — and thus to the modified view — in a way that’s appropriate for the first phase value.

Later, when the value of the `trigger` input changes, the modifier provides its `content` closure with the value of the second phase. Update the effects that you apply to the proxy view accordingly, and the modifier animates the change for you. The next time the `trigger` input changes, this procedure repeats using successive phases until reaching the last phase, at which point the modifier loops back to the first phase.

## See Also

### Creating phase-based animation

- [Controlling the timing and movements of your animations](../controlling-the-timing-and-movements-of-your-animations.md) — Build sophisticated animations that you control using phase and keyframe animators.
- [phaseAnimator(_:content:animation:)](<phaseanimator(__content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change continuously.
- [PhaseAnimator](../phaseanimator.md) — A container that animates its content by automatically cycling through a collection of phases that you provide, each defining a discrete step within an animation.
