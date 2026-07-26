---
title: 'mask(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/mask(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/mask(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/mask%28_%3A%29.json'
content_hash: 'sha256:732fb3188f4f57ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# mask(_:)

<sub>Instance Method</sub>

Masks this view using the alpha channel of the given view.

> [!warning] Deprecated
> Use [mask(alignment:_:)](<mask(alignment___).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func mask<Mask>(_ mask: Mask) -> some View where Mask : View

```

## Parameters

- `mask` — The view whose alpha the rendering system applies to the specified view.

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask(Rectangle().opacity(0.1))
```

![A screenshot of a view masked by a rectangle with 10% opacity.](../../../../attachments/eb80d49199cb4ce05352313feb4e29e5/SwiftUI-View-mask@2x.png)

## See Also

### Graphics and rendering modifiers

- [accentColor(_:)](<accentcolor(__).md>) — Sets the accent color for this view and the views it contains. _(deprecated)_
- [animation(_:)](<animation(__)-1hc0p.md>) — Applies the given animation to all animatable values within this view. _(deprecated)_
- [cornerRadius(_:antialiased:)](<cornerradius(__antialiased_).md>) — Clips this view to its bounding frame, with the specified corner radius. _(deprecated)_
