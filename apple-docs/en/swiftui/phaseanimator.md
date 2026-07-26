---
title: PhaseAnimator
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/phaseanimator
source_url: 'https://developer.apple.com/documentation/swiftui/phaseanimator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/phaseanimator.json'
content_hash: 'sha256:83bfd9696b62a773'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PhaseAnimator

<sub>Structure</sub>

A container that animates its content by automatically cycling through a collection of phases that you provide, each defining a discrete step within an animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct PhaseAnimator<Phase, Content> where Phase : Equatable, Content : View
```

## Overview

Use one of the phase animator view modifiers like [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) to create a phased animation in your app.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a phase animator

- [init(_:content:animation:)](<phaseanimator/init(__content_animation_).md>) — Cycles through a sequence of phases continuously, animating updates to a view on each phase change.
- [init(_:trigger:content:animation:)](<phaseanimator/init(__trigger_content_animation_).md>) — Cycles through a sequence of phases in response to changes in a specified value, animating updates to a view on each phase change.

## See Also

### Creating phase-based animation

- [Controlling the timing and movements of your animations](controlling-the-timing-and-movements-of-your-animations.md) — Build sophisticated animations that you control using phase and keyframe animators.
- [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change continuously.
- [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) — Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
