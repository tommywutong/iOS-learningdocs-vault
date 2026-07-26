---
title: top
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/verticalalignment/top
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment/top'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment/top.json'
content_hash: 'sha256:fc8f450e244872d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VerticalAlignment](../verticalalignment.md)

# top

<sub>Type Property</sub>

A guide that marks the top edge of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let top: VerticalAlignment
```

## Discussion

Use this guide to align the top edges of views:

![A box that contains the word, Top. A horizontal](../../../../attachments/3dc36d23d9c2d6c1e864ab77287943ba/VerticalAlignment-top-1-iOS@2x.png)

The following code generates the image above using an [HStack](../hstack.md):

```swift
struct VerticalAlignmentTop: View {
    var body: some View {
        HStack(alignment: .top, spacing: 0) {
            Color.red.frame(height: 1)
            Text("Top").font(.title).border(.gray)
            Color.red.frame(height: 1)
        }
    }
}
```

## See Also

### Getting guides

- [center](center.md) — A guide that marks the vertical center of the view.
- [bottom](bottom.md) — A guide that marks the bottom edge of the view.
- [firstTextBaseline](firsttextbaseline.md) — A guide that marks the top-most text baseline in a view.
- [lastTextBaseline](lasttextbaseline.md) — A guide that marks the bottom-most text baseline in a view.
