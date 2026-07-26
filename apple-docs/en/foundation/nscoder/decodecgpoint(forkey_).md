---
title: 'decodeCGPoint(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodecgpoint(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodecgpoint(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodecgpoint%28forkey%3A%29.json'
content_hash: 'sha256:ae845508d4cc3bba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeCGPoint(forKey:)

<sub>Instance Method</sub>

Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func decodeCGPoint(forKey key: String) -> CGPoint
```

## Parameters

- `key` — The key that identifies the point.

## Return Value

The `CGPoint` structure.

## Discussion

Use this method to decode a point that was previously encoded using the [- encodeCGPoint:forKey:](<encode(__forkey_)-7z9kc.md>) method.

## See Also

### Related Documentation

- [- encodeCGPoint:forKey:](<encode(__forkey_)-7z9kc.md>) — Encodes a point and associates it with the specified key in the receiver’s archive.

### Decoding Geometry-Based Data

- [- decodeCGAffineTransformForKey:](<decodecgaffinetransform(forkey_).md>) — Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.
- [- decodeCGRectForKey:](<decodecgrect(forkey_).md>) — Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [- decodeCGSizeForKey:](<decodecgsize(forkey_).md>) — Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [- decodeCGVectorForKey:](<decodecgvector(forkey_).md>) — Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.
- [- decodeDirectionalEdgeInsetsForKey:](<decodedirectionaledgeinsets(forkey_).md>) — Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIEdgeInsetsForKey:](<decodeuiedgeinsets(forkey_).md>) — Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIOffsetForKey:](<decodeuioffset(forkey_).md>) — Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.
