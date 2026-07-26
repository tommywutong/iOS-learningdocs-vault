---
title: 'UIPointerEffect.hover(_:preferredTintMode:prefersShadow:prefersScaledContent:)'
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointereffect-swift.enum/hover(_:preferredtintmode:prefersshadow:prefersscaledcontent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointereffect-swift.enum/hover(_:preferredtintmode:prefersshadow:prefersscaledcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointereffect-swift.enum/hover%28_%3Apreferredtintmode%3Aprefersshadow%3Aprefersscaledcontent%3A%29.json'
content_hash: 'sha256:eec7d6ff03e16f28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerEffect](../uipointereffect-swift.enum.md)

# UIPointerEffect.hover(_:preferredTintMode:prefersShadow:prefersScaledContent:)

<sub>Case</sub>

An effect where visual changes apply to the view and the pointer retains its default shape.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case hover(UITargetedPreview, preferredTintMode: UIPointerEffect.TintMode = .overlay, prefersShadow: Bool = false, prefersScaledContent: Bool = true)
```

## Topics

### Specifying the Tint Mode

- [TintMode](tintmode.md) — An effect that defines how to apply a tint to a view during a pointer interaction.

## See Also

### Creating a specific effect

- [UIPointerEffect.highlight(_:)](<highlight(__).md>) — An effect where the pointer slides under the given view and morphs into the view’s shape.
- [UIPointerEffect.lift(_:)](<lift(__).md>) — An effect where the pointer slides under the given view and disappears as the view scales up and gains a shadow.
