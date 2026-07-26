---
title: URLThumbnailDictionaryItem
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlthumbnaildictionaryitem
source_url: 'https://developer.apple.com/documentation/foundation/urlthumbnaildictionaryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlthumbnaildictionaryitem.json'
content_hash: 'sha256:73ebd31ece36103e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLThumbnailDictionaryItem

<sub>Structure</sub>

Possible keys for the [NSURLThumbnailDictionaryKey](urlresourcekey/thumbnaildictionarykey.md) dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLThumbnailDictionaryItem
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Thumbnail Dictionary Key

- [init(_:)](<urlthumbnaildictionaryitem/init(__).md>) — Creates a thumbnail dictionary item key from the provided constant string.
- [init(rawValue:)](<urlthumbnaildictionaryitem/init(rawvalue_).md>) — Creates a thumbnail dictionary item key from the provided raw value string.

### Constants

- [NSThumbnail1024x1024SizeKey](urlthumbnaildictionaryitem/nsthumbnail1024x1024sizekey.md) — A 1024 x 1024 pixel thumbnail as a `UIImage` on iOS or an `NSImage` in macOS. _(deprecated)_

## See Also

### Thumbnail keys

- [NSURLThumbnailKey](urlresourcekey/thumbnailkey.md) — All thumbnails as a single NSImage (read-write). _(deprecated)_
- [NSURLThumbnailDictionaryKey](urlresourcekey/thumbnaildictionarykey.md) — A dictionary of NSImage/UIImage objects keyed by size (read-write). See [URLThumbnailDictionaryItem](urlthumbnaildictionaryitem.md) for a list of possible keys. _(deprecated)_
