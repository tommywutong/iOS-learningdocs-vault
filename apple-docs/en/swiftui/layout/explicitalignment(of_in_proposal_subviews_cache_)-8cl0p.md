---
title: 'explicitAlignment(of:in:proposal:subviews:cache:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layout/explicitalignment(of:in:proposal:subviews:cache:)-8cl0p'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/explicitalignment(of:in:proposal:subviews:cache:)-8cl0p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/explicitalignment%28of%3Ain%3Aproposal%3Asubviews%3Acache%3A%29-8cl0p.json'
content_hash: 'sha256:4c58384055821579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# explicitAlignment(of:in:proposal:subviews:cache:)

<sub>Instance Method</sub>

Returns the result of merging the horizontal alignment guides of all subviews.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func explicitAlignment(of guide: HorizontalAlignment, in bounds: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGFloat?
```

## Discussion

If you don’t implement the [explicitAlignment(of:in:proposal:subviews:cache:)](<explicitalignment(of_in_proposal_subviews_cache_)-8cl0p.md>) method in your custom layout, the protocol uses this default implementation instead, which merges the guides of all the subviews.
