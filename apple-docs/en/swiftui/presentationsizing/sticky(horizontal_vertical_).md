---
title: 'sticky(horizontal:vertical:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/presentationsizing/sticky(horizontal:vertical:)'
source_url: 'https://developer.apple.com/documentation/swiftui/presentationsizing/sticky(horizontal:vertical:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationsizing/sticky%28horizontal%3Avertical%3A%29.json'
content_hash: 'sha256:f0f914b5c0210b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PresentationSizing](../presentationsizing.md)

# sticky(horizontal:vertical:)

<sub>Instance Method</sub>

Modifies self to be sticky in the specified dimensions — growing, but not shrinking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sticky(horizontal: Bool = false, vertical: Bool = false) -> some PresentationSizing

```

## Parameters

- `horizontal` — A boolean indicating whether to maintain the largest size horizontally

- `vertical` — A boolean indicating whether to maintain the largest size vertically

## Return Value

A modified version of self sticking to dimensions specified

## Discussion

If `sticky` is `.vertical`, the presentation can grow in the vertical and horizontal dimensions when its content size grows, but will not shrink in the vertical dimension when content size shrinks.

```swift
ContentView()
  .sheet(isPresented: $presentSheet) {
    MyDynamicSheetContent()
      .presentationSizing(
        .form.sticky(horizontal: false, vertical: true))
  }
```

> [!info] See Also
> [fitted(horizontal:vertical:)](<fitted(horizontal_vertical_).md>)

## See Also

### Creating custom presentation size

- [fitted(horizontal:vertical:)](<fitted(horizontal_vertical_).md>)
- [proposedSize(for:context:)](<proposedsize(for_context_).md>)
