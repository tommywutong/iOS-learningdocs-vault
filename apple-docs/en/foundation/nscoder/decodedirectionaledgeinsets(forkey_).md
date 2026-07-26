---
title: 'decodeDirectionalEdgeInsets(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodedirectionaledgeinsets(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodedirectionaledgeinsets(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodedirectionaledgeinsets%28forkey%3A%29.json'
content_hash: 'sha256:8c641d343ca49c76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeDirectionalEdgeInsets(forKey:)

<sub>Instance Method</sub>

Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func decodeDirectionalEdgeInsets(forKey key: String) -> NSDirectionalEdgeInsets
```

## Parameters

- `key` — The key that identifies the edge insets.

## Discussion

Use this method to decode edge inset information that was previously encoded using the [- encodeDirectionalEdgeInsets:forKey:](<encode(__forkey_)-7oo2n.md>) method.

## See Also

### Decoding Geometry-Based Data

- [- decodeCGAffineTransformForKey:](<decodecgaffinetransform(forkey_).md>) — Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.
- [- decodeCGPointForKey:](<decodecgpoint(forkey_).md>) — Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.
- [- decodeCGRectForKey:](<decodecgrect(forkey_).md>) — Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [- decodeCGSizeForKey:](<decodecgsize(forkey_).md>) — Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [- decodeCGVectorForKey:](<decodecgvector(forkey_).md>) — Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.
- [- decodeUIEdgeInsetsForKey:](<decodeuiedgeinsets(forkey_).md>) — Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIOffsetForKey:](<decodeuioffset(forkey_).md>) — Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.
