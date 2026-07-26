---
title: leading
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/horizontalalignment/leading
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/leading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/leading.json'
content_hash: 'sha256:64daa260df532efb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# leading

<sub>Type Property</sub>

A guide that marks the leading edge of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let leading: HorizontalAlignment
```

## Discussion

Use this guide to align the leading edges of views. For a device that uses a left-to-right language, the leading edge is on the left:

![A box that contains the word, Leading. Vertical](../../../../attachments/7bde2ddd5347556c261423c21c988e18/HorizontalAlignment-leading-1-iOS@2x.png)

The following code generates the image above using a [VStack](../vstack.md):

```swift
struct HorizontalAlignmentLeading: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Color.red.frame(width: 1)
            Text("Leading").font(.title).border(.gray)
            Color.red.frame(width: 1)
        }
    }
}
```

## See Also

### Getting guides

- [center](center.md) — A guide that marks the horizontal center of the view.
- [trailing](trailing.md) — A guide that marks the trailing edge of the view.
- [listRowSeparatorLeading](listrowseparatorleading.md) — A guide marking the leading edge of a `List` row separator.
- [listRowSeparatorTrailing](listrowseparatortrailing.md) — A guide marking the trailing edge of a `List` row separator.
