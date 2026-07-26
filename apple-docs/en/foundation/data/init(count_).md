---
title: 'init(count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(count:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28count%3A%29.json'
content_hash: 'sha256:1ef0a99e0fba3fc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(count:)

<sub>Initializer</sub>

Creates a new data buffer with the specified count of zeroed bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(count: Int)
```

## Parameters

- `count` — The number of bytes the data initially contains.

## See Also

### Creating Empty Data

- [init()](<init().md>) — Creates an empty data buffer.
- [init(capacity:)](<init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [resetBytes(in:)](<resetbytes(in_).md>) — Sets a region of the data buffer to `0`.
