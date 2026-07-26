---
title: 'updateCache(_:subviews:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layout/updatecache(_:subviews:)-75zac'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/updatecache(_:subviews:)-75zac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/updatecache%28_%3Asubviews%3A%29-75zac.json'
content_hash: 'sha256:22e1b2cc904507cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# updateCache(_:subviews:)

<sub>Instance Method</sub>

Reinitializes a cache to a new value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updateCache(_ cache: inout Self.Cache, subviews: Self.Subviews)
```

## Discussion

If you don’t implement the [updateCache(_:subviews:)](<updatecache(__subviews_)-75zac.md>) method in your custom layout, the protocol uses this default implementation instead, which calls [makeCache(subviews:)](<makecache(subviews_).md>).
