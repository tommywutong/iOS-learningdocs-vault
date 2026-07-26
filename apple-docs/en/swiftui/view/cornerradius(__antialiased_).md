---
title: 'cornerRadius(_:antialiased:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/cornerradius(_:antialiased:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/cornerradius(_:antialiased:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/cornerradius%28_%3Aantialiased%3A%29.json'
content_hash: 'sha256:8232768591fd7f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# cornerRadius(_:antialiased:)

<sub>Instance Method</sub>

Clips this view to its bounding frame, with the specified corner radius.

> [!warning] Deprecated
> Use [clipShape(_:style:)](<clipshape(__style_).md>) or [fill(style:)](<../shape/fill(style_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func cornerRadius(_ radius: CGFloat, antialiased: Bool = true) -> some View

```

## Parameters

- `radius` — A CGFloat value that specifies the corner radius to use when clipping the view to its bounding frame.

- `antialiased` — A Boolean value that indicates whether the rendering system applies smoothing to the edges of the clipping rectangle.

## Return Value

A view that clips this view to its bounding frame with the specified corner radius.

## Discussion

By default, a view’s bounding frame only affects its layout, so any content that extends beyond the edges of the frame remains visible. Use `cornerRadius(_:antialiased:)` to hide any content that extends beyond these edges while applying a corner radius.

The following code applies a corner radius of 25 to a text view:

```swift
Text("Rounded Corners")
    .frame(width: 175, height: 75)
    .foregroundColor(Color.white)
    .background(Color.black)
    .cornerRadius(25)
```

![A screenshot of a rectangle with rounded corners bounding a text](../../../../attachments/93dbf20ad2c8de571000a7dffdb1bea8/SwiftUI-View-cornerRadius@2x.png)

## See Also

### Graphics and rendering modifiers

- [accentColor(_:)](<accentcolor(__).md>) — Sets the accent color for this view and the views it contains. _(deprecated)_
- [mask(_:)](<mask(__).md>) — Masks this view using the alpha channel of the given view. _(deprecated)_
- [animation(_:)](<animation(__)-1hc0p.md>) — Applies the given animation to all animatable values within this view. _(deprecated)_
