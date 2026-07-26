---
title: 'decodeTime(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetime(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetime(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetime%28forkey%3A%29.json'
content_hash: 'sha256:49707d01fbf0890e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTime(forKey:)

<sub>Instance Method</sub>

Returns the Core Media time structure associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeTime(forKey key: String) -> CMTime
```

## Parameters

- `key` — The key for a `CMTime` structure encoded in the receiver.

## Return Value

The `CMTime` structure associated with `key` in the archive.

## See Also

### Related Documentation

- [- encodeCMTime:forKey:](<encode(__forkey_)-6wbby.md>) — Encodes a given Core Media time structure and associates it with a specified key.

### Decoding Core Media Time Structures

- [- decodeCMTimeRangeForKey:](<decodetimerange(forkey_).md>) — Returns the Core Media time range structure associated with a given key.
- [- decodeCMTimeMappingForKey:](<decodetimemapping(forkey_).md>) — Returns the Core Media time mapping structure associated with a given key.
