---
title: infinity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/proposedviewsize/infinity
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/infinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/infinity.json'
content_hash: 'sha256:bfdf688d7495f2ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# infinity

<sub>Type Property</sub>

A size proposal that contains infinity in both dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let infinity: ProposedViewSize
```

## Discussion

Both dimensions contain doc://com.apple.documentation/documentation/CoreFoundation/swift/floatingpoint/infinity in this size proposal. Subviews of a custom layout return their maximum size when you propose this value using the [dimensions(in:)](<../layoutsubview/dimensions(in_).md>) method. A custom layout should also return its maximum size from the [sizeThatFits(proposal:subviews:cache:)](<../layout/sizethatfits(proposal_subviews_cache_).md>) method for this value.

## See Also

### Getting standard proposals

- [zero](zero.md) — A size proposal that contains zero in both dimensions.
- [unspecified](unspecified.md) — The proposed size with both dimensions left unspecified.
