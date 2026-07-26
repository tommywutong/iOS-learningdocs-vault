---
title: 'resetBytes(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/resetbytes(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/resetbytes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/resetbytes%28in%3A%29.json'
content_hash: 'sha256:a439a55b05eb0c0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# resetBytes(in:)

<sub>Instance Method</sub>

Sets a region of the data buffer to `0`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func resetBytes(in range: Range<Data.Index>)
```

## Parameters

- `range` — The range in the data to set to `0`.

## Discussion

If `range` exceeds the bounds of the data, then the data is resized to fit.

## See Also

### Creating Empty Data

- [init()](<init().md>) — Creates an empty data buffer.
- [init(capacity:)](<init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [init(count:)](<init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.
