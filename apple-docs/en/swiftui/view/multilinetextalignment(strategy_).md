---
title: 'multilineTextAlignment(strategy:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/multilinetextalignment(strategy:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/multilinetextalignment(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/multilinetextalignment%28strategy%3A%29.json'
content_hash: 'sha256:a76506f9e5011b3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# multilineTextAlignment(strategy:)

<sub>Instance Method</sub>

A modifier for the default text alignment strategy in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View

```

## Discussion

To control the alignment explicitly at a view level, choose the [layoutBased](../text/alignmentstrategy/layoutbased.md) mode and set the [multilineTextAlignment](../environmentvalues/multilinetextalignment.md) to the appropriate value.

## See Also

### Multiline text

- [lineLimit(_:)](<linelimit(__).md>) — Sets to a closed range the number of lines that text can occupy in this view.
- [lineLimit(_:reservesSpace:)](<linelimit(__reservesspace_).md>) — Sets a limit for the number of lines text can occupy in this view.
- [lineSpacing(_:)](<linespacing(__).md>) — Sets the amount of space between lines of text in this view.
- [multilineTextAlignment(_:)](<multilinetextalignment(__).md>) — Sets the alignment of a text view that contains multiple lines of text.
