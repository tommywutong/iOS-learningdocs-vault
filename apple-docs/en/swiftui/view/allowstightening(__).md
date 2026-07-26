---
title: 'allowsTightening(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/allowstightening(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/allowstightening(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/allowstightening%28_%3A%29.json'
content_hash: 'sha256:f0c735ee26e76947'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# allowsTightening(_:)

<sub>Instance Method</sub>

Sets whether text in this view can compress the space between characters when necessary to fit text in a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func allowsTightening(_ flag: Bool) -> some View

```

## Parameters

- `flag` — A Boolean value that indicates whether the space between characters compresses when necessary.

## Return Value

A view that can compress the space between characters when necessary to fit text in a line.

## Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects of `allowsTightening(_:)` on the compression of the spacing between characters:

```swift
VStack {
    Text("This is a wide text element")
        .font(.body)
        .frame(width: 200, height: 50, alignment: .leading)
        .lineLimit(1)
        .allowsTightening(true)

    Text("This is a wide text element")
        .font(.body)
        .frame(width: 200, height: 50, alignment: .leading)
        .lineLimit(1)
        .allowsTightening(false)
}
```

![A screenshot showing the effect of enabling text tightening in a](../../../../attachments/7875ef8b31de58ae8d8efc6485da09b0/SwiftUI-view-allowsTightening@2x.png)

## See Also

### Controlling hit testing

- [contentShape(_:eoFill:)](<contentshape(__eofill_).md>) — Defines the content shape for hit testing.
- [contentShape(_:_:eoFill:)](<contentshape(____eofill_).md>) — Sets the content shape for this view.
- [ContentShapeKinds](../contentshapekinds.md) — A kind for the content shape of a view.
