---
title: 'containerBackground(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/containerbackground(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/containerbackground(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/containerbackground%28_%3Afor%3A%29.json'
content_hash: 'sha256:b00ba5cea5e33a24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# containerBackground(_:for:)

<sub>Instance Method</sub>

Sets the container background of the enclosing container using a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func containerBackground<S>(_ style: S, for container: ContainerBackgroundPlacement) -> some View where S : ShapeStyle

```

## Discussion

The following example uses a [LinearGradient](../lineargradient.md) as a background:

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Blue") {
                    Text("Blue")
                    .containerBackground(.blue.gradient, for: .navigation)
                }
                NavigationLink("Red") {
                    Text("Red")
                    .containerBackground(.red.gradient, for: .navigation)
                }
            }
        }
    }
}
```

The `.containerBackground(_:for:)` modifier differs from the [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) modifier by automatically filling an entire parent container. [ContainerBackgroundPlacement](../containerbackgroundplacement.md) describes the available containers.

- Parameters

    - style: The shape style to use as the container background.
    - container: The container that will use the background.

## See Also

### Layering views

- [Adding a background to your view](../adding-a-background-to-your-view.md) — Compose a background behind your view and extend it beyond the safe area insets.
- [ZStack](../zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](<zindex(__).md>) — Controls the display order of overlapping views.
- [background(alignment:content:)](<background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](<overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [backgroundMaterial](../environmentvalues/backgroundmaterial.md) — The material underneath the current view.
- [containerBackground(for:alignment:content:)](<containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](../containerbackgroundplacement.md) — The placement of a container background.
