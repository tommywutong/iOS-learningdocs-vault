---
title: displayPadding
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textrenderer/displaypadding
source_url: 'https://developer.apple.com/documentation/swiftui/textrenderer/displaypadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textrenderer/displaypadding.json'
content_hash: 'sha256:da4b281c0725ec6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextRenderer](../textrenderer.md)

# displayPadding

<sub>Instance Property</sub>

Returns the size of the extra padding added to any drawing layer used to rasterize the text. For example when drawing the text with a shadow this may be used to extend the drawing bounds to avoid clipping the shadow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var displayPadding: EdgeInsets { get }
```

## Discussion

The default implementation of this function returns an empty set of insets.

## Default Implementations

### TextRenderer Implementations

- [displayPadding](displaypadding-9l6t9.md) — Returns the size of the extra padding added to any drawing layer used to rasterize the text. For example when drawing the text with a shadow this may be used to extend the drawing bounds to avoid clipping the shadow.
