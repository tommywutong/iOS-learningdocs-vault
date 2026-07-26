---
title: 'encode(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/encode(_:forkey:)-29jyx'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-29jyx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/encode%28_%3Aforkey%3A%29-29jyx.json'
content_hash: 'sha256:06ce3949e930177f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes an affine transform and associates it with the specified key in the receiver’s archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func encode(_ transform: CGAffineTransform, forKey key: String)
```

## Parameters

- `transform` — The transform information to encode.

- `key` — The key identifying the data.

## Discussion

When decoding the data from the archive, you pass the value in the `key` parameter to the corresponding [- decodeCGAffineTransformForKey:](<decodecgaffinetransform(forkey_).md>) method to retrieve the data.

## See Also

### Related Documentation

- [- decodeCGAffineTransformForKey:](<decodecgaffinetransform(forkey_).md>) — Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.

### Encoding Geometry-Based Data

- [- encodeCGPoint:forKey:](<encode(__forkey_)-7z9kc.md>) — Encodes a point and associates it with the specified key in the receiver’s archive.
- [- encodeCGRect:forKey:](<encode(__forkey_)-10qhm.md>) — Encodes a rectangle and associates it with the specified key in the receiver’s archive.
- [- encodeCGSize:forKey:](<encode(__forkey_)-6wq3n.md>) — Encodes size information and associates it with the specified key in the coder’s archive.
- [- encodeCGVector:forKey:](<encode(__forkey_)-26fxa.md>) — Encodes vector data and associates it with the specified key in the coder’s archive.
- [- encodeDirectionalEdgeInsets:forKey:](<encode(__forkey_)-7oo2n.md>) — Encodes directional edge inset data and associates it with the specified key in the coder’s archive.
- [- encodeUIEdgeInsets:forKey:](<encode(__forkey_)-44zsc.md>) — Encodes edge inset data and associates it with the specified key in the coder’s archive.
- [- encodeUIOffset:forKey:](<encode(__forkey_)-9d1qy.md>) — Encodes offset data and associates it with the specified key in the coder’s archive.
