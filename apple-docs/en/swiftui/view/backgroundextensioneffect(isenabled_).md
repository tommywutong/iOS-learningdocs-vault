---
title: 'backgroundExtensionEffect(isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/backgroundextensioneffect(isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect(isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/backgroundextensioneffect%28isenabled%3A%29.json'
content_hash: 'sha256:19f2012366c072d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# backgroundExtensionEffect(isEnabled:)

<sub>Instance Method</sub>

Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func backgroundExtensionEffect(isEnabled: Bool) -> some View

```

## Parameters

- `isEnabled` — Should the extension effect be active or not.

## Discussion

Use this modifier when you want to create copies outside of the safe area so the view and its copies together can function as backgrounds for other elements on top. The most common use case is to apply this to a view in the detail column of a navigation split view so it can extend under the sidebar or inspector region to provide seamless immersive visuals.

```swift
@State private var extendBackground: Bool = true

NavigationSplitView {
    // sidebar content
} detail: {
    ZStack {
        BannerView()
            .backgroundExtensionEffect(isEnabled: extendBackground)
    }
}
.inspector(isPresented: $showInspector) {
    // inspector content
}
```

Apply this modifier with discretion. This should often be used with only a single instance of background content with consideration of visual clarity and performance.

> [!note] Note
> This modifier will clip the view to prevent copies from overlapping with each other.

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
- [glassBackgroundEffect(_:in:displayMode:)](<glassbackgroundeffect(__in_displaymode_).md>) — Fills the view’s background with a custom glass background effect and a shape that you specify.
- [backgroundExtensionEffect()](<backgroundextensioneffect().md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
