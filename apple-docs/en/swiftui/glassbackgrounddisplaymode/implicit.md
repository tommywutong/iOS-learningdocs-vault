---
title: GlassBackgroundDisplayMode.implicit
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glassbackgrounddisplaymode/implicit
source_url: 'https://developer.apple.com/documentation/swiftui/glassbackgrounddisplaymode/implicit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glassbackgrounddisplaymode/implicit.json'
content_hash: 'sha256:2c8b13a20de53952'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GlassBackgroundDisplayMode](../glassbackgrounddisplaymode.md)

# GlassBackgroundDisplayMode.implicit

<sub>Case</sub>

Display the glass material only when the view isn’t already contained in glass.

<sub>visionOS</sub>

```swift
case implicit
```

## Discussion

Use this value to avoid duplicate backgrounds when a view that has a glass background contains another view that also has a glass background.

This display mode doesn’t suppress duplicate glass backgrounds for views that are offset by any amount in the z-axis. For example, the two subviews of the following [HStack](../hstack.md) behave differently:

```swift
HStack {
    MyView()
        .glassBackgroundEffect(displayMode: .implicit)
    MyView()
        .glassBackgroundEffect(displayMode: .implicit)
        .offset(z: 100)
}
.glassBackgroundEffect(displayMode: .always)
```

The first instance of `MyView` doesn’t display a background because its container displays one. However the second instance does display a background because that view is offset from its container by 100 points along the z-axis.

## See Also

### Getting the mode

- [GlassBackgroundDisplayMode.always](always.md) — Always display the glass material.
- [GlassBackgroundDisplayMode.never](never.md) — Never display the glass material.
