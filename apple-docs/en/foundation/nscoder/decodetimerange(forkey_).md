---
title: 'decodeTimeRange(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetimerange(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetimerange(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetimerange%28forkey%3A%29.json'
content_hash: 'sha256:a2468f338fb696b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTimeRange(forKey:)

<sub>Instance Method</sub>

Returns the Core Media time range structure associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeTimeRange(forKey key: String) -> CMTimeRange
```

## Parameters

- `key` — The key for a `CMTimeRange` structure encoded in the receiver.

## Return Value

The `CMTimeRange` structure associated with `key` in the archive.

## See Also

### Related Documentation

- [- encodeCMTimeRange:forKey:](<encode(__forkey_)-46lo8.md>) — Encodes a given Core Media time range structure and associates it with a specified key.

### Decoding Core Media Time Structures

- [- decodeCMTimeForKey:](<decodetime(forkey_).md>) — Returns the Core Media time structure associated with a given key.
- [- decodeCMTimeMappingForKey:](<decodetimemapping(forkey_).md>) — Returns the Core Media time mapping structure associated with a given key.
