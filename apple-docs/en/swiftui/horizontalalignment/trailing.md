---
title: trailing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/horizontalalignment/trailing
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/trailing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/trailing.json'
content_hash: 'sha256:d6ceeb7cf1bda734'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# trailing

<sub>Type Property</sub>

A guide that marks the trailing edge of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let trailing: HorizontalAlignment
```

## Discussion

Use this guide to align the trailing edges of views. For a device that uses a left-to-right language, the trailing edge is on the right:

![A box that contains the word, Trailing. Vertical](../../../../attachments/3d36e49a665b5b5f456af2746870ae1c/HorizontalAlignment-trailing-1-iOS@2x.png)

The following code generates the image above using a [VStack](../vstack.md):

```swift
struct HorizontalAlignmentTrailing: View {
    var body: some View {
        VStack(alignment: .trailing, spacing: 0) {
            Color.red.frame(width: 1)
            Text("Trailing").font(.title).border(.gray)
            Color.red.frame(width: 1)
        }
    }
}
```

## See Also

### Getting guides

- [leading](leading.md) — A guide that marks the leading edge of the view.
- [center](center.md) — A guide that marks the horizontal center of the view.
- [listRowSeparatorLeading](listrowseparatorleading.md) — A guide marking the leading edge of a `List` row separator.
- [listRowSeparatorTrailing](listrowseparatortrailing.md) — A guide marking the trailing edge of a `List` row separator.
