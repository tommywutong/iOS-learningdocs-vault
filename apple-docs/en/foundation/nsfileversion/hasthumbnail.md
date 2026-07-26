---
title: hasThumbnail
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/hasthumbnail
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/hasthumbnail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/hasthumbnail.json'
content_hash: 'sha256:9802234777843c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# hasThumbnail

<sub>Instance Property</sub>

Whether the version has a thumbnail image available. Thumbnails for versions from +getNonlocalVersionsOfItemAtURL:completionHandler: may not immediately be available. As soon as it becomes available, this property will change from NO to YES. You can use KVO to be notified of this change. If a thumbnail is available, you can access it using NSURLThumbnailKey or NSURLThumbnailDictionaryKey.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasThumbnail: Bool { get }
```
