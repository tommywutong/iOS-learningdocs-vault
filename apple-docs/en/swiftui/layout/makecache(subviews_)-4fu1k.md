---
title: 'makeCache(subviews:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layout/makecache(subviews:)-4fu1k'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/makecache(subviews:)-4fu1k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/makecache%28subviews%3A%29-4fu1k.json'
content_hash: 'sha256:cd91a4b9655dc027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# makeCache(subviews:)

<sub>Instance Method</sub>

Returns the empty value when your layout doesn’t require a cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeCache(subviews: Self.Subviews) -> Self.Cache
```

## Discussion

If you don’t implement the [makeCache(subviews:)](<makecache(subviews_)-4fu1k.md>) method in your custom layout, the protocol uses this default implementation instead, which returns an empty value.
