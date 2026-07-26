---
title: 'init(_:content:animation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/phaseanimator/init(_:content:animation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/phaseanimator/init(_:content:animation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/phaseanimator/init%28_%3Acontent%3Aanimation%3A%29.json'
content_hash: 'sha256:063fb8cfdb459505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PhaseAnimator](../phaseanimator.md)

# init(_:content:animation:)

<sub>Initializer</sub>

Cycles through a sequence of phases continuously, animating updates to a view on each phase change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ phases: some Sequence<Phase>, @ContentBuilder content: @escaping (Phase) -> Content, animation: @escaping (Phase) -> Animation? = { _ in .default })
```

## Parameters

- `phases` — The sequence of phases to cycle through. Ensure that the sequence isn’t empty. If it is, SwiftUI logs a runtime warning and also returns a visual warning as the output view.

- `content` — A content builder closure that takes the current phase as an input. Return a view that’s based on the current phase.

- `animation` — A closure that takes the current phase as input. Return the animation to use when transitioning to the next phase. If you return `nil`, the transition doesn’t animate. If you don’t set this parameter, SwiftUI uses a default animation.

## Discussion

When the phase animator first appears, this initializer renders the `content` closure using the first phase as input to the closure. The animator then begins immediately animating to the view produced by sending the second phase to the `content` closure using the animation returned from the `animation` closure. This procedure repeats for successive phases until reaching the last phase, after which the animator loops back to the first phase again.

## See Also

### Creating a phase animator

- [init(_:trigger:content:animation:)](<init(__trigger_content_animation_).md>) — Cycles through a sequence of phases in response to changes in a specified value, animating updates to a view on each phase change.
