---
title: lastTextBaseline
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/verticalalignment/lasttextbaseline
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment/lasttextbaseline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment/lasttextbaseline.json'
content_hash: 'sha256:09be8680cae54735'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VerticalAlignment](../verticalalignment.md)

# lastTextBaseline

<sub>Type Property</sub>

A guide that marks the bottom-most text baseline in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let lastTextBaseline: VerticalAlignment
```

## Discussion

Use this guide to align with the baseline of the bottom-most text in a view. The guide aligns with the bottom of a view that contains no text.

![A box that contains the text, Last Text Baseline.](../../../../attachments/f5faacd72c9610f5feadce01aa0a1c5a/VerticalAlignment-lastTextBaseline-1-iOS@2x.png)

The following code generates the image above using an [HStack](../hstack.md):

```swift
struct VerticalAlignmentLastTextBaseline: View {
    var body: some View {
        HStack(alignment: .lastTextBaseline, spacing: 0) {
            Color.red.frame(height: 1)
            Text("Last Text Baseline").font(.title).border(.gray)
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
- [firstTextBaseline](firsttextbaseline.md) — A guide that marks the top-most text baseline in a view.
