---
title: lineSpacing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/linespacing
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/linespacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/linespacing.json'
content_hash: 'sha256:122f1ae308c1e9f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# lineSpacing

<sub>Instance Property</sub>

The distance in points between the bottom of one line fragment and the top of the next.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lineSpacing: CGFloat { get set }
```

## Discussion

This value is always nonnegative.

## See Also

### Formatting multiline text

- [lineSpacing(_:)](<../view/linespacing(__).md>) — Sets the amount of space between lines of text in this view.
- [multilineTextAlignment(_:)](<../view/multilinetextalignment(__).md>) — Sets the alignment of a text view that contains multiple lines of text.
- [multilineTextAlignment](multilinetextalignment.md) — An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.
