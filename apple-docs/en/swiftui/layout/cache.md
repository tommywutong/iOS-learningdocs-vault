---
title: Cache
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layout/cache
source_url: 'https://developer.apple.com/documentation/swiftui/layout/cache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/cache.json'
content_hash: 'sha256:828a265645057147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# Cache

<sub>Associated Type</sub>

Cached values associated with the layout instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Cache = Void
```

## Discussion

If you create a cache for your custom layout, you can use a type alias to define this type as your data storage type. Alternatively, you can refer to the data storage type directly in all the places where you work with the cache.

See [makeCache(subviews:)](<makecache(subviews_).md>) for more information.

## See Also

### Managing a cache

- [makeCache(subviews:)](<makecache(subviews_).md>) — Creates and initializes a cache for a layout instance.
- [updateCache(_:subviews:)](<updatecache(__subviews_).md>) — Updates the layout’s cache when something changes.
