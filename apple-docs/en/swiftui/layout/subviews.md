---
title: Layout.Subviews
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layout/subviews
source_url: 'https://developer.apple.com/documentation/swiftui/layout/subviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/subviews.json'
content_hash: 'sha256:ce778e0a956ebe56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# Layout.Subviews

<sub>Type Alias</sub>

A collection of proxies for the subviews of a layout view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Subviews = LayoutSubviews
```

## Discussion

This collection doesn’t store views. Instead it stores instances of [LayoutSubview](../layoutsubview.md), each of which acts as a proxy for one of the views arranged by the layout. Use the proxies to get information about the views, and to tell the views where to appear.

For more information about the behavior of the underlying collection type, see [LayoutSubviews](../layoutsubviews.md).

## See Also

### Sizing the container and placing subviews

- [sizeThatFits(proposal:subviews:cache:)](<sizethatfits(proposal_subviews_cache_).md>) — Returns the size of the composite view, given a proposed size and the view’s subviews.
- [placeSubviews(in:proposal:subviews:cache:)](<placesubviews(in_proposal_subviews_cache_).md>) — Assigns positions to each of the layout’s subviews.
