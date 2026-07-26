---
title: maxSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingsizingoptions/maxsize
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/maxsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingsizingoptions/maxsize.json'
content_hash: 'sha256:f9ed42bc06e04261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSizingOptions](../nshostingsizingoptions.md)

# maxSize

<sub>Type Property</sub>

The hosting view creates and updates constraints that represent its content’s maximum size.

<sub>macOS</sub>

```swift
static let maxSize: NSHostingSizingOptions
```

## Discussion

The constraints reflect the size that fits a proposal of `width: infinity, height: infinity`.

## See Also

### Geting sizing options

- [intrinsicContentSize](intrinsiccontentsize.md) — The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [minSize](minsize.md) — The hosting view creates and updates constraints that represent its content’s minimum size.
- [preferredContentSize](preferredcontentsize.md) — The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [standardBounds](standardbounds.md) — The hosting view creates constraints for its minimum, ideal, and maximum sizes.
