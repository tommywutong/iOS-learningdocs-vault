---
title: 'glassBackgroundEffect(_:in:displayMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/glassbackgroundeffect(_:in:displaymode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(_:in:displaymode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/glassbackgroundeffect%28_%3Ain%3Adisplaymode%3A%29.json'
content_hash: 'sha256:f202ff8bcd26c8db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# glassBackgroundEffect(_:in:displayMode:)

<sub>Instance Method</sub>

Fills the view’s background with a custom glass background effect and a shape that you specify.

<sub>visionOS</sub>

```swift
nonisolated func glassBackgroundEffect<T, S>(_ effect: S, in shape: T, displayMode: GlassBackgroundDisplayMode = .always) -> some View where T : InsettableShape, S : GlassBackgroundEffect

```

## Parameters

- `effect` — A [GlassBackgroundEffect](../glassbackgroundeffect.md) instance that SwiftUI uses to the fill the background shape that you specify.

- `shape` — An [InsettableShape](../insettableshape.md) instance that SwiftUI draws behind the view.

- `displayMode` — When to display the glass background. The default is [GlassBackgroundDisplayMode.always](../glassbackgrounddisplaymode/always.md).

## Return Value

A view with a glass background.

## See Also

### Background elements

- [background(alignment:content:)](<background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [alternatingRowBackgrounds(_:)](<alternatingrowbackgrounds(__).md>) — Overrides whether lists and tables in this view have alternating row backgrounds.
- [listRowBackground(_:)](<listrowbackground(__).md>) — Places a custom background view behind a list row item.
- [scrollContentBackground(_:)](<scrollcontentbackground(__).md>) — Specifies the visibility of the background for scrollable views within this view.
- [containerBackground(_:for:)](<containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [glassBackgroundEffect(displayMode:)](<glassbackgroundeffect(displaymode_).md>) — Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(_:displayMode:)](<glassbackgroundeffect(__displaymode_).md>) — Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](<glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [backgroundExtensionEffect()](<backgroundextensioneffect().md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [backgroundExtensionEffect(isEnabled:)](<backgroundextensioneffect(isenabled_).md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
