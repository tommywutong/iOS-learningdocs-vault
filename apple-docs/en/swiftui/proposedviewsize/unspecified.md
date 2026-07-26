---
title: unspecified
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/proposedviewsize/unspecified
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/unspecified.json'
content_hash: 'sha256:629816cd9e596da9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# unspecified

<sub>Type Property</sub>

The proposed size with both dimensions left unspecified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let unspecified: ProposedViewSize
```

## Discussion

Both dimensions contain `nil` in this size proposal. Subviews of a custom layout return their ideal size when you propose this value using the [dimensions(in:)](<../layoutsubview/dimensions(in_).md>) method. A custom layout should also return its ideal size from the [sizeThatFits(proposal:subviews:cache:)](<../layout/sizethatfits(proposal_subviews_cache_).md>) method for this value.

## See Also

### Getting standard proposals

- [zero](zero.md) — A size proposal that contains zero in both dimensions.
- [infinity](infinity.md) — A size proposal that contains infinity in both dimensions.
