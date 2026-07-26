---
title: thumbnailDictionaryKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+（15.0 起废弃）, iPadOS 8.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.10+（12.0 起废弃）, tvOS 9.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（8.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcekey/thumbnaildictionarykey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/thumbnaildictionarykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/thumbnaildictionarykey.json'
content_hash: 'sha256:41a51ac4b06c34f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# thumbnailDictionaryKey

<sub>Type Property</sub>

A dictionary of NSImage/UIImage objects keyed by size (read-write). See [URLThumbnailDictionaryItem](../urlthumbnaildictionaryitem.md) for a list of possible keys.

> [!warning] Deprecated
> Use the QuickLookThumbnailing framework and extension point instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let thumbnailDictionaryKey: URLResourceKey
```

## See Also

### Thumbnail keys

- [NSURLThumbnailKey](thumbnailkey.md) — All thumbnails as a single NSImage (read-write). _(deprecated)_
- [URLThumbnailDictionaryItem](../urlthumbnaildictionaryitem.md) — Possible keys for the [NSURLThumbnailDictionaryKey](thumbnaildictionarykey.md) dictionary.
