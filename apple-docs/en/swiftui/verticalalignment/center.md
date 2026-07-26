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
doc_path: /documentation/swiftui/verticalalignment/center
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment/center.json'
content_hash: 'sha256:013d7cf2cf174ce9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VerticalAlignment](../verticalalignment.md)

# center

<sub>Type Property</sub>

A guide that marks the vertical center of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let center: VerticalAlignment
```

## Discussion

Use this guide to align the centers of views:

![A box that contains the word, Center. A horizontal](../../../../attachments/c032067a13700082475bc8abb4918c68/VerticalAlignment-center-1-iOS@2x.png)

The following code generates the image above using an [HStack](../hstack.md):

```swift
struct VerticalAlignmentCenter: View {
    var body: some View {
        HStack(alignment: .center, spacing: 0) {
            Color.red.frame(height: 1)
            Text("Center").font(.title).border(.gray)
            Color.red.frame(height: 1)
        }
    }
}
```

## See Also

### Getting guides

- [top](top.md) — A guide that marks the top edge of the view.
- [bottom](bottom.md) — A guide that marks the bottom edge of the view.
- [firstTextBaseline](firsttextbaseline.md) — A guide that marks the top-most text baseline in a view.
- [lastTextBaseline](lasttextbaseline.md) — A guide that marks the bottom-most text baseline in a view.
