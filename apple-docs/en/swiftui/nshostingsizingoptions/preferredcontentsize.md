---
title: preferredContentSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingsizingoptions/preferredcontentsize
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingsizingoptions/preferredcontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingsizingoptions/preferredcontentsize.json'
content_hash: 'sha256:9f714d9e4a709977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSizingOptions](../nshostingsizingoptions.md)

# preferredContentSize

<sub>Type Property</sub>

The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.

<sub>macOS</sub>

```swift
static let preferredContentSize: NSHostingSizingOptions
```

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

> [!note] Note
> This option has no effect when used with an `NSHostingView` directly.

## See Also

### Geting sizing options

- [intrinsicContentSize](intrinsiccontentsize.md) — The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [maxSize](maxsize.md) — The hosting view creates and updates constraints that represent its content’s maximum size.
- [minSize](minsize.md) — The hosting view creates and updates constraints that represent its content’s minimum size.
- [standardBounds](standardbounds.md) — The hosting view creates constraints for its minimum, ideal, and maximum sizes.
