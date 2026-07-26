---
title: 'imageScale(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/imagescale(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/imagescale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/imagescale%28_%3A%29.json'
content_hash: 'sha256:05958dd1a1aaaf21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# imageScale(_:)

<sub>Instance Method</sub>

Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func imageScale(_ scale: Image.Scale) -> some View

```

## Parameters

- `scale` — One of the relative sizes provided by the image scale enumeration.

## Discussion

The example below shows the relative scaling effect. The system renders the image at a relative size based on the available space and configuration options of the image it is scaling.

```swift
VStack {
    HStack {
        Image(systemName: "heart.fill")
            .imageScale(.small)
        Text("Small")
    }
    HStack {
        Image(systemName: "heart.fill")
            .imageScale(.medium)
        Text("Medium")
    }

    HStack {
        Image(systemName: "heart.fill")
            .imageScale(.large)
        Text("Large")
    }
}
```

![A view showing small, medium, and large hearts rendered at a size](../../../../attachments/75aceca7a4758e6a07e038b1baacf2f3/SwiftUI-View-imageScale@2x.png)

## See Also

### Configuring an image

- [Fitting images into available space](../fitting-images-into-available-space.md) — Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [imageScale](../environmentvalues/imagescale.md) — The image scale for this environment.
- [Scale](../image/scale.md) — A scale to apply to vector images relative to text.
- [Orientation](../image/orientation.md) — The orientation of an image.
- [ResizingMode](../image/resizingmode.md) — The modes that SwiftUI uses to resize an image to fit within its containing view.
