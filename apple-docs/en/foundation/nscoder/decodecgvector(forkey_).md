---
title: 'decodeCGVector(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodecgvector(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodecgvector(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodecgvector%28forkey%3A%29.json'
content_hash: 'sha256:20a5bf1f24693abb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeCGVector(forKey:)

<sub>Instance Method</sub>

Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func decodeCGVector(forKey key: String) -> CGVector
```

## Parameters

- `key` — The key that identifies the vector.

## Return Value

The vector data.

## Discussion

Use this method to decode vector information that was previously encoded using the [- encodeCGVector:forKey:](<encode(__forkey_)-26fxa.md>) method.

## See Also

### Related Documentation

- [- encodeCGVector:forKey:](<encode(__forkey_)-26fxa.md>) — Encodes vector data and associates it with the specified key in the coder’s archive.

### Decoding Geometry-Based Data

- [- decodeCGAffineTransformForKey:](<decodecgaffinetransform(forkey_).md>) — Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.
- [- decodeCGPointForKey:](<decodecgpoint(forkey_).md>) — Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.
- [- decodeCGRectForKey:](<decodecgrect(forkey_).md>) — Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [- decodeCGSizeForKey:](<decodecgsize(forkey_).md>) — Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [- decodeDirectionalEdgeInsetsForKey:](<decodedirectionaledgeinsets(forkey_).md>) — Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIEdgeInsetsForKey:](<decodeuiedgeinsets(forkey_).md>) — Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [- decodeUIOffsetForKey:](<decodeuioffset(forkey_).md>) — Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.
