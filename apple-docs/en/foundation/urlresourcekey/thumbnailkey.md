---
title: thumbnailKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+（12.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcekey/thumbnailkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/thumbnailkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/thumbnailkey.json'
content_hash: 'sha256:c0e72ad26cf5c109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# thumbnailKey

<sub>Type Property</sub>

All thumbnails as a single NSImage (read-write).

> [!warning] Deprecated
> Use the QuickLookThumbnailing framework and extension point instead

<sub>macOS</sub>

```swift
static let thumbnailKey: URLResourceKey
```

## See Also

### Thumbnail keys

- [NSURLThumbnailDictionaryKey](thumbnaildictionarykey.md) — A dictionary of NSImage/UIImage objects keyed by size (read-write). See [URLThumbnailDictionaryItem](../urlthumbnaildictionaryitem.md) for a list of possible keys. _(deprecated)_
- [URLThumbnailDictionaryItem](../urlthumbnaildictionaryitem.md) — Possible keys for the [NSURLThumbnailDictionaryKey](thumbnaildictionarykey.md) dictionary.
