---
title: firstTextBaseline
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/verticalalignment/firsttextbaseline
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment/firsttextbaseline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment/firsttextbaseline.json'
content_hash: 'sha256:4f4348e4797596ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VerticalAlignment](../verticalalignment.md)

# firstTextBaseline

<sub>Type Property</sub>

A guide that marks the top-most text baseline in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let firstTextBaseline: VerticalAlignment
```

## Discussion

Use this guide to align with the baseline of the top-most text in a view. The guide aligns with the bottom of a view that contains no text:

![A box that contains the text, First Text Baseline.](../../../../attachments/e676907b319612805deae559c8d91cc4/VerticalAlignment-firstTextBaseline-1-iOS@2x.png)

The following code generates the image above using an [HStack](../hstack.md):

```swift
struct VerticalAlignmentFirstTextBaseline: View {
    var body: some View {
        HStack(alignment: .firstTextBaseline, spacing: 0) {
            Color.red.frame(height: 1)
            Text("First Text Baseline").font(.title).border(.gray)
            Color.red.frame(height: 1)
        }
    }
}
```

## See Also

### Getting guides

- [top](top.md) — A guide that marks the top edge of the view.
- [center](center.md) — A guide that marks the vertical center of the view.
- [bottom](bottom.md) — A guide that marks the bottom edge of the view.
- [lastTextBaseline](lasttextbaseline.md) — A guide that marks the bottom-most text baseline in a view.
