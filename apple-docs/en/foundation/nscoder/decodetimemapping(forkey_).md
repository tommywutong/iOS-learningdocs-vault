---
title: 'decodeTimeMapping(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodetimemapping(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodetimemapping(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodetimemapping%28forkey%3A%29.json'
content_hash: 'sha256:c112a6eb9ae0af31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeTimeMapping(forKey:)

<sub>Instance Method</sub>

Returns the Core Media time mapping structure associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeTimeMapping(forKey key: String) -> CMTimeMapping
```

## Parameters

- `key` — The key for a `CMTimeMapping` structure encoded in the receiver.

## Return Value

The `CMTimeMapping` structure associated with `key` in the archive.

## See Also

### Related Documentation

- [- encodeCMTimeMapping:forKey:](<encode(__forkey_)-8tefb.md>) — Encodes a given Core Media time mapping structure and associates it with a specified key.

### Decoding Core Media Time Structures

- [- decodeCMTimeForKey:](<decodetime(forkey_).md>) — Returns the Core Media time structure associated with a given key.
- [- decodeCMTimeRangeForKey:](<decodetimerange(forkey_).md>) — Returns the Core Media time range structure associated with a given key.
