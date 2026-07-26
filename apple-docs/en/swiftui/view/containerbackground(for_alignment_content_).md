---
title: 'containerBackground(for:alignment:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/containerbackground(for:alignment:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/containerbackground(for:alignment:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/containerbackground%28for%3Aalignment%3Acontent%3A%29.json'
content_hash: 'sha256:ea9cfecc70b68c25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# containerBackground(for:alignment:content:)

<sub>Instance Method</sub>

Sets the container background of the enclosing container using a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func containerBackground<V>(for container: ContainerBackgroundPlacement, alignment: Alignment = .center, @ContentBuilder content: () -> V) -> some View where V : View

```

## Parameters

- `container` — The container that will use the background.

- `alignment` — The alignment that the modifier uses to position the implicit [ZStack](../zstack.md) that groups the background views. The default is [center](../alignment/center.md).

- `content` — The view to use as the background of the container.

## Discussion

The following example uses a custom [View](../view.md) as a background:

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Image") {
                    Text("Image")
                    .containerBackground(for: .navigation) {
                        Image(name: "ImageAsset")
                    }
                }
            }
        }
    }
}
```

The `.containerBackground(for:alignment:content:)` modifier differs from the [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) modifier by automatically filling an entire parent container. [ContainerBackgroundPlacement](../containerbackgroundplacement.md) describes the available containers.

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
- [containerBackground(_:for:)](<containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](../containerbackgroundplacement.md) — The placement of a container background.
