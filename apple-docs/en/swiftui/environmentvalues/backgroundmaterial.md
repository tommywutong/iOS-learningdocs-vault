---
title: backgroundMaterial
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/backgroundmaterial
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/backgroundmaterial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/backgroundmaterial.json'
content_hash: 'sha256:00185cbcc04d27fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# backgroundMaterial

<sub>Instance Property</sub>

The material underneath the current view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var backgroundMaterial: Material? { get set }
```

## Discussion

This value is `nil` if the current background isn’t one of the standard materials. If you set a material, the standard content styles enable their vibrant rendering modes.

You set this value by calling one of the background modifiers that takes a [ShapeStyle](../shapestyle.md), like [background(_:ignoresSafeAreaEdges:)](<../view/background(__ignoressafeareaedges_).md>) or [background(_:in:fillStyle:)](<../view/background(__in_fillstyle_).md>), and passing in a [Material](../material.md). You can also set the value manually, using `nil` to disable vibrant rendering, or a [Material](../material.md) instance to enable the vibrancy style associated with the specified material.

## See Also

### Layering views

- [Adding a background to your view](../adding-a-background-to-your-view.md) — Compose a background behind your view and extend it beyond the safe area insets.
- [ZStack](../zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](<../view/zindex(__).md>) — Controls the display order of overlapping views.
- [background(alignment:content:)](<../view/background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<../view/background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<../view/background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<../view/background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<../view/background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](<../view/overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<../view/overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<../view/overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [containerBackground(_:for:)](<../view/containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<../view/containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](../containerbackgroundplacement.md) — The placement of a container background.
