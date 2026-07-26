---
title: intrinsicContentSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingsizingoptions/intrinsiccontentsize
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/intrinsiccontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingsizingoptions/intrinsiccontentsize.json'
content_hash: 'sha256:08bef831d3376b02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSizingOptions](../nshostingsizingoptions.md)

# intrinsicContentSize

<sub>Type Property</sub>

The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.

<sub>macOS</sub>

```swift
static let intrinsicContentSize: NSHostingSizingOptions
```

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

## See Also

### Geting sizing options

- [maxSize](maxsize.md) — The hosting view creates and updates constraints that represent its content’s maximum size.
- [minSize](minsize.md) — The hosting view creates and updates constraints that represent its content’s minimum size.
- [preferredContentSize](preferredcontentsize.md) — The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [standardBounds](standardbounds.md) — The hosting view creates constraints for its minimum, ideal, and maximum sizes.
