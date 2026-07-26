---
title: thumbnailDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+（12.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcevalues/thumbnaildictionary-4ztst
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/thumbnaildictionary-4ztst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/thumbnaildictionary-4ztst.json'
content_hash: 'sha256:a6b299111c9d5567'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# thumbnailDictionary

<sub>Instance Property</sub>

A dictionary of AppKit image objects keyed by size.

> [!warning] Deprecated
> Use the QuickLookThumbnailing framework and extension point instead

<sub>macOS</sub>

```swift
var thumbnailDictionary: [URLThumbnailDictionaryItem : NSImage]? { get }
```

## See Also

### Thumbnail values

- [thumbnail](thumbnail.md) — A thumbnail image of the URL. _(deprecated)_
- [thumbnailDictionary](thumbnaildictionary-7jyzz.md) — A dictionary of UIKit image objects keyed by size. _(deprecated)_
