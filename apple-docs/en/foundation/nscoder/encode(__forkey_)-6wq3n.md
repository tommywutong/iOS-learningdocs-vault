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
doc_path: '/documentation/foundation/nscoder/encode(_:forkey:)-6wq3n'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-6wq3n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/encode%28_%3Aforkey%3A%29-6wq3n.json'
content_hash: 'sha256:32aa7f4d22c04ed5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes size information and associates it with the specified key in the coder’s archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func encode(_ size: CGSize, forKey key: String)
```

## Parameters

- `size` — The size information to encode.

- `key` — The key identifying the data.

## Discussion

When decoding the data from the archive, you pass the value in the `key` parameter to the corresponding [- decodeCGSizeForKey:](<decodecgsize(forkey_).md>) method to retrieve the data.

## See Also

### Related Documentation

- [- decodeCGSizeForKey:](<decodecgsize(forkey_).md>) — Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.

### Encoding Geometry-Based Data

- [- encodeCGAffineTransform:forKey:](<encode(__forkey_)-29jyx.md>) — Encodes an affine transform and associates it with the specified key in the receiver’s archive.
- [- encodeCGPoint:forKey:](<encode(__forkey_)-7z9kc.md>) — Encodes a point and associates it with the specified key in the receiver’s archive.
- [- encodeCGRect:forKey:](<encode(__forkey_)-10qhm.md>) — Encodes a rectangle and associates it with the specified key in the receiver’s archive.
- [- encodeCGVector:forKey:](<encode(__forkey_)-26fxa.md>) — Encodes vector data and associates it with the specified key in the coder’s archive.
- [- encodeDirectionalEdgeInsets:forKey:](<encode(__forkey_)-7oo2n.md>) — Encodes directional edge inset data and associates it with the specified key in the coder’s archive.
- [- encodeUIEdgeInsets:forKey:](<encode(__forkey_)-44zsc.md>) — Encodes edge inset data and associates it with the specified key in the coder’s archive.
- [- encodeUIOffset:forKey:](<encode(__forkey_)-9d1qy.md>) — Encodes offset data and associates it with the specified key in the coder’s archive.
