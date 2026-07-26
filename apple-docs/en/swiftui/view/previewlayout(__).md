---
title: 'previewLayout(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/previewlayout(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/previewlayout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/previewlayout%28_%3A%29.json'
content_hash: 'sha256:660f60eb09b8ad7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# previewLayout(_:)

<sub>Instance Method</sub>

Overrides the size of the container for the preview.

> [!warning] Deprecated
> Use [Preview(_:traits:_:body:)](<../preview(__traits___body_).md>) with [sizeThatFitsLayout](../../developertoolssupport/previewtrait/sizethatfitslayout.md) or  [fixedLayout(width:height:)](<../../developertoolssupport/previewtrait/fixedlayout(width_height_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func previewLayout(_ value: PreviewLayout) -> some View

```

## Parameters

- `value` — A layout to use for preview.

## Return Value

A preview that uses the given layout.

## Discussion

By default, previews use the `PreviewLayout/device` layout, which places the view inside a visual representation of the chosen device. You can instead tell a preview to use a different layout by choosing one of the `PreviewLayout` values, like `PreviewLayout/sizeThatFits`:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewLayout(.sizeThatFits)
    }
}
```

## See Also

### Customizing a preview

- [previewDevice(_:)](<previewdevice(__).md>) — Overrides the device for a preview. _(deprecated)_
- [PreviewDevice](../previewdevice.md) — A simulator device that runs a preview. _(deprecated)_
- [previewInterfaceOrientation(_:)](<previewinterfaceorientation(__).md>) — Overrides the orientation of the preview. _(deprecated)_
- [InterfaceOrientation](../interfaceorientation.md) — The orientation of the interface from the user’s perspective.
