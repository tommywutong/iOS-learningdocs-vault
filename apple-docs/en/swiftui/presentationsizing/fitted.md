---
title: fitted
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationsizing/fitted
source_url: 'https://developer.apple.com/documentation/swiftui/presentationsizing/fitted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationsizing/fitted.json'
content_hash: 'sha256:961c2e6bdfc776e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PresentationSizing](../presentationsizing.md)

# fitted

<sub>Type Property</sub>

The presentation sizing is dictated by the ideal size of the content

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var fitted: FittedPresentationSizing { get }
```

## Discussion

On macOS, presentations with `.fitted` sizing are user-resizable by default. Because of this, is best practice to define a presentation frame with any of the `frame` modifiers, either specifying a fixed frame or minimum/maximum bounds. If you specify a [fixedSize()](<../view/fixedsize().md>) or a frame with fixed dimensions on the content, the sheet will not be user resizable.

```swift
@State private var present = true

ContentView().sheet(isPresented: $present) {
  ScrollView {
    LazyVGrid(columns: columns) {
      ForEach(0x1f600...0x1f679, id: \.self) { value in
        Text(String(format: "%x", value))
        Text(emoji(value))
          .font(.largeTitle)
        }
      }
  }
  .presentationSizing(.fitted)
  .frame(
    minWidth: 200, idealWidth: 300, maxWidth: 500,
    minHeight: 100, maxHeight: 600)
}
```

To create a view that fits the view’s size in either the horizontal or vertical dimensions, see [fitted(horizontal:vertical:)](<fitted(horizontal_vertical_).md>).

## See Also

### Getting built-in presentation size

- [automatic](automatic.md) — The default presentation sizing, appropriate for the platform.
- [form](form.md) — The size is appropriate for forms and slightly less wide than`.page`
- [page](page.md) — The size is roughly the size of a page of paper, appropriate for informational or compositional content.
