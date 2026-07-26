---
title: 'replaceSubrange(_:with:count:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/replacesubrange(_:with:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/replacesubrange(_:with:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/replacesubrange%28_%3Awith%3Acount%3A%29.json'
content_hash: 'sha256:ae68303bb995e8f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# replaceSubrange(_:with:count:)

<sub>Instance Method</sub>

Replaces a region of bytes in the data with bytes from memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange(_ subrange: Range<Data.Index>, with bytes: UnsafeRawPointer, count cnt: Int)
```

## See Also

### Replacing a Range of Bytes

- [replaceSubrange(_:with:)](<replacesubrange(__with_)-9u7ry.md>) — Replaces a region of bytes in the data with new bytes from a collection.
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-9nzh.md>) — Replaces a region of bytes in the data with new bytes from a buffer.
