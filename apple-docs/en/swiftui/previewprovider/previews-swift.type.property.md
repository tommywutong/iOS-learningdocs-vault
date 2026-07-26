---
title: previews
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewprovider/previews-swift.type.property
source_url: 'https://developer.apple.com/documentation/swiftui/previewprovider/previews-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewprovider/previews-swift.type.property.json'
content_hash: 'sha256:73be27e43e7bd94a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewProvider](../previewprovider.md)

# previews

<sub>Type Property</sub>

A collection of views to preview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency static var previews: Self.Previews { get }
```

## Discussion

Implement a computed `previews` property to indicate the content to preview. Xcode generates a preview for each view that you list. You can apply [View](../view.md) modifiers to the views, like you do when creating a custom view. For a preview, you can also use various preview-specific modifiers that customize the preview. For example, you can choose a specific device for the preview by adding the [previewDevice(_:)](<../view/previewdevice(__).md>) modifier:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

For the full list of preview-specific modifiers, see [Previews in Xcode](../previews-in-xcode.md).

## See Also

### Creating a preview

- [Previews](previews-swift.associatedtype.md) — The type to preview. _(deprecated)_
