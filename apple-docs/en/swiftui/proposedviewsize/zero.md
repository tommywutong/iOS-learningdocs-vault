---
title: zero
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/proposedviewsize/zero
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/zero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/zero.json'
content_hash: 'sha256:01fd982751193e6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# zero

<sub>Type Property</sub>

A size proposal that contains zero in both dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let zero: ProposedViewSize
```

## Discussion

Subviews of a custom layout return their minimum size when you propose this value using the [dimensions(in:)](<../layoutsubview/dimensions(in_).md>) method. A custom layout should also return its minimum size from the [sizeThatFits(proposal:subviews:cache:)](<../layout/sizethatfits(proposal_subviews_cache_).md>) method for this value.

## See Also

### Getting standard proposals

- [infinity](infinity.md) — A size proposal that contains infinity in both dimensions.
- [unspecified](unspecified.md) — The proposed size with both dimensions left unspecified.
