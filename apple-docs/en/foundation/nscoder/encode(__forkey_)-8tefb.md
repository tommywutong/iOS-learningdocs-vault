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
doc_path: '/documentation/foundation/nscoder/encode(_:forkey:)-8tefb'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-8tefb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/encode%28_%3Aforkey%3A%29-8tefb.json'
content_hash: 'sha256:af32e86813f8a651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes a given Core Media time mapping structure and associates it with a specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(_ timeMapping: CMTimeMapping, forKey key: String)
```

## Parameters

- `timeMapping` — A `CMTimeMapping` structure.

- `key` — The key with which to associate `timeMapping` in the archive.

## See Also

### Related Documentation

- [- decodeCMTimeMappingForKey:](<decodetimemapping(forkey_).md>) — Returns the Core Media time mapping structure associated with a given key.

### Encoding Core Media Time Structures

- [- encodeCMTime:forKey:](<encode(__forkey_)-6wbby.md>) — Encodes a given Core Media time structure and associates it with a specified key.
- [- encodeCMTimeRange:forKey:](<encode(__forkey_)-46lo8.md>) — Encodes a given Core Media time range structure and associates it with a specified key.
