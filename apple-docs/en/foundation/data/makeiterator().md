---
title: makeIterator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/data/makeiterator()
source_url: 'https://developer.apple.com/documentation/foundation/data/makeiterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/makeiterator%28%29.json'
content_hash: 'sha256:67d4239ba59e0546'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# makeIterator()

<sub>Instance Method</sub>

Returns an iterator over the contents of the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeIterator() -> Data.Iterator
```

## Discussion

The iterator will increment byte-by-byte.

## See Also

### Iterating Over Bytes

- [Iterator](iterator.md) — An iterator that operates over the contents of data.
- [enumerateBytes(_:)](<enumeratebytes(__).md>) — Enumerates the contents of the data’s buffer.
