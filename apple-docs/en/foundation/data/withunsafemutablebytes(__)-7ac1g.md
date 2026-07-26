---
title: 'withUnsafeMutableBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（5.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/data/withunsafemutablebytes(_:)-7ac1g'
source_url: 'https://developer.apple.com/documentation/foundation/data/withunsafemutablebytes(_:)-7ac1g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/withunsafemutablebytes%28_%3A%29-7ac1g.json'
content_hash: 'sha256:3592a8ade14874fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# withUnsafeMutableBytes(_:)

<sub>Instance Method</sub>

Mutates the raw bytes in the data’s buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func withUnsafeMutableBytes<ResultType, ContentType>(_ body: (UnsafeMutablePointer<ContentType>) throws -> ResultType) rethrows -> ResultType
```

## Discussion

This function assumes that you are mutating the contents.

> [!warning] Warning
> The byte pointer argument should not be stored and used outside of the lifetime of the call to the closure.

## See Also

### Accessing Underlying Memory

- [withUnsafeBytes(_:)](<withunsafebytes(__).md>) — Accesses the raw bytes in the data’s buffer.
- [copyBytes(to:count:)](<copybytes(to_count_).md>) — Copies the contents of the data to memory.
- [copyBytes(to:from:)](<copybytes(to_from_)-8qk4r.md>) — Copies a subset of the contents of the data to memory.
- [copyBytes(to:from:)](<copybytes(to_from_)-4o6zj.md>) — Copies the bytes in a range from the data into a buffer.
