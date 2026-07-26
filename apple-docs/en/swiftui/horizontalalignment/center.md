---
title: center
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/horizontalalignment/center
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/center.json'
content_hash: 'sha256:06e9ceb5864c5976'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# center

<sub>Type Property</sub>

A guide that marks the horizontal center of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let center: HorizontalAlignment
```

## Discussion

Use this guide to align the centers of views:

![A box that contains the word, Center. Vertical](../../../../attachments/98c827da09fff59ad521ae1431e95b70/HorizontalAlignment-center-1-iOS@2x.png)

The following code generates the image above using a [VStack](../vstack.md):

```swift
struct HorizontalAlignmentCenter: View {
    var body: some View {
        VStack(alignment: .center, spacing: 0) {
            Color.red.frame(width: 1)
            Text("Center").font(.title).border(.gray)
            Color.red.frame(width: 1)
        }
    }
}
```

## See Also

### Getting guides

- [leading](leading.md) — A guide that marks the leading edge of the view.
- [trailing](trailing.md) — A guide that marks the trailing edge of the view.
- [listRowSeparatorLeading](listrowseparatorleading.md) — A guide marking the leading edge of a `List` row separator.
- [listRowSeparatorTrailing](listrowseparatortrailing.md) — A guide marking the trailing edge of a `List` row separator.
