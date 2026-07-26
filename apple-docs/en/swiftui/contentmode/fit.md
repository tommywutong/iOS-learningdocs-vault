---
title: ContentMode.fit
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentmode/fit
source_url: 'https://developer.apple.com/documentation/swiftui/contentmode/fit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentmode/fit.json'
content_hash: 'sha256:e54d53bfd7f140e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentMode](../contentmode.md)

# ContentMode.fit

<sub>Case</sub>

An option that resizes the content so it’s all within the available space, both vertically and horizontally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case fit
```

## Discussion

This mode preserves the content’s aspect ratio. If the content doesn’t have the same aspect ratio as the available space, the content becomes the same size as the available space on one axis and leaves empty space on the other.

## See Also

### Getting content modes

- [ContentMode.fill](fill.md) — An option that resizes the content so it occupies all available space, both vertically and horizontally.
