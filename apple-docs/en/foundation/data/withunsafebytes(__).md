---
title: 'withUnsafeBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（5.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/data/withunsafebytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/withunsafebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/withunsafebytes%28_%3A%29.json'
content_hash: 'sha256:914473ca644f94ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# withUnsafeBytes(_:)

<sub>Instance Method</sub>

Accesses the raw bytes in the data’s buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<ResultType, ContentType>(_ body: (UnsafePointer<ContentType>) throws -> ResultType) rethrows -> ResultType
```

## Discussion

> [!warning] Warning
> The byte pointer argument should not be stored and used outside of the lifetime of the call to the closure.

## See Also

### Accessing Underlying Memory

- [withUnsafeMutableBytes(_:)](<withunsafemutablebytes(__)-7ac1g.md>) — Mutates the raw bytes in the data’s buffer.
- [copyBytes(to:count:)](<copybytes(to_count_).md>) — Copies the contents of the data to memory.
- [copyBytes(to:from:)](<copybytes(to_from_)-8qk4r.md>) — Copies a subset of the contents of the data to memory.
- [copyBytes(to:from:)](<copybytes(to_from_)-4o6zj.md>) — Copies the bytes in a range from the data into a buffer.
