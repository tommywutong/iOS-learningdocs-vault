---
title: minSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingsizingoptions/minsize
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/minsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingsizingoptions/minsize.json'
content_hash: 'sha256:c6d466212591194f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSizingOptions](../nshostingsizingoptions.md)

# minSize

<sub>Type Property</sub>

The hosting view creates and updates constraints that represent its content’s minimum size.

<sub>macOS</sub>

```swift
static let minSize: NSHostingSizingOptions
```

## Discussion

The constraints reflect the size that fits a proposal of `width: 0, height: 0`.

## See Also

### Geting sizing options

- [intrinsicContentSize](intrinsiccontentsize.md) — The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [maxSize](maxsize.md) — The hosting view creates and updates constraints that represent its content’s maximum size.
- [preferredContentSize](preferredcontentsize.md) — The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [standardBounds](standardbounds.md) — The hosting view creates constraints for its minimum, ideal, and maximum sizes.
