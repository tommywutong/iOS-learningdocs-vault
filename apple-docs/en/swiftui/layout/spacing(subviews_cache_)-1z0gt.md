---
title: 'spacing(subviews:cache:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layout/spacing(subviews:cache:)-1z0gt'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/spacing(subviews:cache:)-1z0gt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/spacing%28subviews%3Acache%3A%29-1z0gt.json'
content_hash: 'sha256:1db2087551692ae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# spacing(subviews:cache:)

<sub>Instance Method</sub>

Returns the union of all subview spacing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func spacing(subviews: Self.Subviews, cache: inout Self.Cache) -> ViewSpacing
```

## Discussion

If you don’t implement the [spacing(subviews:cache:)](<spacing(subviews_cache_)-1z0gt.md>) method in your custom layout, the protocol uses this default implementation instead, which returns the union of the spacing preferences of all the layout’s subviews.
