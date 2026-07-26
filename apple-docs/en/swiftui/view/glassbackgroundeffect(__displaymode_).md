---
title: 'glassBackgroundEffect(_:displayMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/glassbackgroundeffect(_:displaymode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(_:displaymode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/glassbackgroundeffect%28_%3Adisplaymode%3A%29.json'
content_hash: 'sha256:a988b060b6c7c2ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# glassBackgroundEffect(_:displayMode:)

<sub>Instance Method</sub>

Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.

<sub>visionOS</sub>

```swift
nonisolated func glassBackgroundEffect<S>(_ effect: S, displayMode: GlassBackgroundDisplayMode = .always) -> some View where S : GlassBackgroundEffect

```

## Parameters

- `effect` — A [GlassBackgroundEffect](../glassbackgroundeffect.md) instance that SwiftUI uses to draw a background of the modified view.

- `displayMode` — When to display the glass background. The default is [GlassBackgroundDisplayMode.always](../glassbackgrounddisplaymode/always.md).

## Return Value

A view with a glass background.

## Discussion

Use this modifier to add a glass material that may include thickness, specularity, glass blur, shadows, and other effects. Because of its physical depth, the background influences z-axis layout. For different effect, the background may influences x-axis and y-axis layout.

To ensure that the effect renders properly when you add it to a collection of views in a [ZStack](../zstack.md), add the modifier to the stack rather to one of the views in the stack. This includes when you create an implicit stack with view modifiers like [overlay(alignment:content:)](<overlay(alignment_content_).md>) or [background(alignment:content:)](<background(alignment_content_).md>). In those cases, you might need to create an explicit [ZStack](../zstack.md) inside the `content` closure to have a place to add the background modifier.

Non closed shapes will be rendered as their convex hull.

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
- [glassBackgroundEffect(in:displayMode:)](<glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [glassBackgroundEffect(_:in:displayMode:)](<glassbackgroundeffect(__in_displaymode_).md>) — Fills the view’s background with a custom glass background effect and a shape that you specify.
- [backgroundExtensionEffect()](<backgroundextensioneffect().md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [backgroundExtensionEffect(isEnabled:)](<backgroundextensioneffect(isenabled_).md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
