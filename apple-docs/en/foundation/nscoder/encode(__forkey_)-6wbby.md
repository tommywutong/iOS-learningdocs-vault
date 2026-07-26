---
title: 'encode(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/encode(_:forkey:)-6wbby'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-6wbby'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/encode%28_%3Aforkey%3A%29-6wbby.json'
content_hash: 'sha256:0b85b05618da2f5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes a given Core Media time structure and associates it with a specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(_ time: CMTime, forKey key: String)
```

## Parameters

- `time` — A `CMTime` structure.

- `key` — The key with which to associate `time` in the archive.

## See Also

### Related Documentation

- [- decodeCMTimeForKey:](<decodetime(forkey_).md>) — Returns the Core Media time structure associated with a given key.

### Encoding Core Media Time Structures

- [- encodeCMTimeRange:forKey:](<encode(__forkey_)-46lo8.md>) — Encodes a given Core Media time range structure and associates it with a specified key.
- [- encodeCMTimeMapping:forKey:](<encode(__forkey_)-8tefb.md>) — Encodes a given Core Media time mapping structure and associates it with a specified key.
