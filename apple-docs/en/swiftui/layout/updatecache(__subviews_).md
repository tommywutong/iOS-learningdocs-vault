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
doc_path: '/documentation/swiftui/layout/updatecache(_:subviews:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/updatecache(_:subviews:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/updatecache%28_%3Asubviews%3A%29.json'
content_hash: 'sha256:3241c076c2d05a07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# updateCache(_:subviews:)

<sub>Instance Method</sub>

Updates the layout’s cache when something changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updateCache(_ cache: inout Self.Cache, subviews: Self.Subviews)
```

## Parameters

- `cache` — Storage for calculated data that you share among the methods of your custom layout container.

- `subviews` — A collection of proxy instances that represent the views arranged by the container. You can use the proxies in the collection to get information about the subviews as you calculate values to store in the cache.

## Discussion

If your custom layout container creates a cache by implementing the [makeCache(subviews:)](<makecache(subviews_).md>) method, SwiftUI calls the update method when your layout or its subviews change, giving you an opportunity to modify or invalidate the contents of the cache. The method’s default implementation recreates the cache by calling the [makeCache(subviews:)](<makecache(subviews_).md>) method, but you can provide your own implementation to take an incremental approach, if appropriate.

## Default Implementations

### Layout Implementations

- [updateCache(_:subviews:)](<updatecache(__subviews_)-75zac.md>) — Reinitializes a cache to a new value.

## See Also

### Managing a cache

- [makeCache(subviews:)](<makecache(subviews_).md>) — Creates and initializes a cache for a layout instance.
- [Cache](cache.md) — Cached values associated with the layout instance.
