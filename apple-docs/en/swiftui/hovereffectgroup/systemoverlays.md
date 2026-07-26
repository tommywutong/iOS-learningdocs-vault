---
title: systemOverlays
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffectgroup/systemoverlays
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffectgroup/systemoverlays'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffectgroup/systemoverlays.json'
content_hash: 'sha256:72f6c65e860ec22c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffectGroup](../hovereffectgroup.md)

# systemOverlays

<sub>Type Property</sub>

A `HoverEffectGroup` that becomes active when system overlays are visible.

<sub>visionOS</sub>

```swift
static var systemOverlays: HoverEffectGroup { get }
```

## Discussion

Use this group to synchronize effects with system overlays. In the following example, the back button will be hidden whenever system overlays are hidden.

```swift
Button("Back") { }
    .hoverEffect(in: .systemOverlays) { e, isActive, _ in
        e.animation(
            isActive ? .systemOverlayAppearance : .systemOverlayDelayedDisappearance
        ) {
            $0.opacity(isActive ? 1 : 0)
        }
    }
    .persistentSystemOverlays(.hidden)
```

This example uses the `systemOverlayAppearance` and `systemOverlayDisappearance` animations to ensure the effect using the same timing as system overlays.

If `persistentSystemOverlays` is not `.hidden`, this group will always be active.
