---
title: thumbnail
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+（12.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcevalues/thumbnail
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/thumbnail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/thumbnail.json'
content_hash: 'sha256:5f5ba76c076a148e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# thumbnail

<sub>Instance Property</sub>

A thumbnail image of the URL.

> [!warning] Deprecated
> Use the QuickLookThumbnailing framework and extension point instead

<sub>macOS</sub>

```swift
var thumbnail: NSImage? { get }
```

## Discussion

The URL populates ths property by retrieving the [NSURLThumbnailKey](../urlresourcekey/thumbnailkey.md) from the resource values, and is `nil` if there’s no value for the key.

## See Also

### Thumbnail values

- [thumbnailDictionary](thumbnaildictionary-7jyzz.md) — A dictionary of UIKit image objects keyed by size. _(deprecated)_
- [thumbnailDictionary](thumbnaildictionary-4ztst.md) — A dictionary of AppKit image objects keyed by size. _(deprecated)_
